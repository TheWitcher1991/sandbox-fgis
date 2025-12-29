from django.db import transaction

from organizations.models import Organization
from organizations.types import CreateOrganizationDTO, OrganizationId
from packages.framework.usecases import UseCaseAdapter
from roles.types import RoleType
from services.users.usecases.member import member_use_case
from services.users.usecases.user import user_use_case
from users.types import MemberId, MemberRole


class OrganizationUseCase(UseCaseAdapter[Organization, OrganizationId]):
    def __init__(self):
        super().__init__(Organization)

    def optimize(self):
        return self.objects.prefetch_related("members").select_related("role")

    def get_by_member(self, member_id: MemberId) -> Organization:
        return self.optimize().filter(members__id=member_id).first()

    def get_role_by_member(self, member_id: MemberId) -> RoleType:
        return self.get_by_member(member_id).role.code

    @transaction.atomic
    def register(self, data: CreateOrganizationDTO):

        org = self.create(name=data.name, inn=data.inn, role_id=data.role)

        user = user_use_case.create(
            email=data.email,
            phone=data.phone,
            password=data.password,
            first_name=data.first_name,
            last_name=data.last_name,
            surname=data.surname,
        )

        member_use_case.create(user=user, organization=org, position=data.position, role=MemberRole.superadmin)

        return org


organization_use_case = OrganizationUseCase()
