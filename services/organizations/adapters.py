from typing import Optional

from rest_framework.exceptions import NotFound

from organizations.models import Organization
from organizations.types import OrganizationId
from packages.kernel.context import RequestContext
from packages.kernel.types import ExtendedRequest
from roles.types import RoleType
from users.models import Member, User
from users.types import MemberRole


class OrganizationAdapter:
    user: Optional[User] = None
    member: Optional[Member] = None
    organization: Optional[Organization] = None

    member_role: Optional[MemberRole] = None
    organization_role: Optional[RoleType] = None

    organization_id: Optional[OrganizationId] = None
    _organization_loaded: bool = False

    organization_kwarg_names = (
        "organization_id",
        "org_id",
        "organization_pk",
        "pk",
    )
    organization_query_param = "organization_id"

    strict_organization = False

    def _cast_org_id(self, value) -> Optional[OrganizationId]:
        try:
            return OrganizationId(int(value))
        except (TypeError, ValueError):
            return None

    def _resolve_user(self, request: ExtendedRequest):
        self.user = request.user if getattr(request, "user", None) and request.user.is_authenticated else None

    def _resolve_member(self):
        if self.user and hasattr(self.user, "member"):
            self.member = self.user.member
            self.member_role = self.member.role
        else:
            self.member = None
            self.member_role = None

    def resolve_organization_id(self, request: ExtendedRequest, **kwargs) -> Optional[OrganizationId]:
        for key in self.organization_kwarg_names:
            value = kwargs.get(key)
            org_id = self._cast_org_id(value)
            if org_id is not None:
                return org_id

        value = request.query_params.get(self.organization_query_param)
        return self._cast_org_id(value)

    def resolve_effective_organization_id(self) -> Optional[OrganizationId]:
        return self.organization_id or (self.member.organization_id if self.member else None)

    def get_organization(self) -> Optional[Organization]:
        if self._organization_loaded:
            return self.organization

        self._organization_loaded = True
        org_id = self.resolve_effective_organization_id()
        if not org_id:
            self.organization = None
            self.organization_role = None
            return None

        self.organization = Organization.objects.select_related("role").filter(id=org_id).first()
        self.organization_role = self.organization.role.code if self.organization else None
        return self.organization

    def enforce_organization(self):
        if self.strict_organization and self.get_organization() is None:
            raise NotFound("Organization not found")

    def get_context(self) -> RequestContext:
        self.get_organization()
        return RequestContext(
            user=self.user,
            member=self.member,
            organization=self.organization,
            member_role=self.member_role,
            organization_role=self.organization_role,
        )

    def setup(self, request: ExtendedRequest, *args, **kwargs):
        if hasattr(super(), "setup"):
            super().setup(request, *args, **kwargs)

        self._resolve_user(request)
        self._resolve_member()
        self.organization_id = self.resolve_organization_id(request, **kwargs)

        if self.strict_organization:
            self.enforce_organization()
