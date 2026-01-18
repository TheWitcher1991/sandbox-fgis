from rest_framework.permissions import BasePermission

from packages.kernel.types import ExtendedRequest
from roles.types import RoleType


class IsOrganization(BasePermission):
    def has_permission(self, request: ExtendedRequest, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        return hasattr(user, "member") and user.member.organization_id is not None


class IsOrganizationRole(IsOrganization):
    org_roles: set[RoleType] = set()

    def has_permission(self, request: ExtendedRequest, view):
        if not super().has_permission(request, view):
            return False

        org_role = request.user.member.organization.role.code
        return org_role in self.org_roles


class IsSeedOrganization(IsOrganizationRole):
    org_roles = {RoleType.seed_org}


class IsAccreditedOrganization(IsOrganizationRole):
    org_roles = {RoleType.accred_org}


class IsScienceOrganization(IsOrganizationRole):
    org_roles = {RoleType.science_org}


class IsGovernmentOrganization(IsOrganizationRole):
    org_roles = {RoleType.gov_org}
