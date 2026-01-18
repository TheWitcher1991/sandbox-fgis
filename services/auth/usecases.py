from django.db import transaction

from auth.types import LoginData, LoginSession
from organizations.types import CreateOrganizationData, CreateOrganizationDTO
from organizations.usecases import organization_use_case
from packages.framework.contrib import authenticate
from packages.kernel.types import ExtendedRequest, JWTRefreshSession
from packages.usecases.jwt import jwt_use_case


class AuthUseCase:
    def refresh(self, request: ExtendedRequest) -> JWTRefreshSession:
        return jwt_use_case.refresh(request.user)

    @transaction.atomic
    def login(self, request: ExtendedRequest, data: LoginData) -> LoginSession:
        user = authenticate(
            request=request,
            email=data["email"],
            password=data["password"],
        )

        session = jwt_use_case.sign(user)

        member = user.member

        session["user"] = user.id
        session["role"] = member.role
        session["org"] = organization_use_case.get_role_by_member(member_id=member.id)

        return session

    @transaction.atomic
    def register(self, data: CreateOrganizationData) -> CreateOrganizationData:
        dto = CreateOrganizationDTO(**data)

        organization_use_case.register(dto)

        return data


auth_use_case = AuthUseCase()
