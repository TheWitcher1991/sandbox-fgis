from ast import Dict

from django.db import transaction

from organizations.usecases import organization_use_case
from packages.framework.contrib import authenticate
from packages.kernel.types import ExtendedRequest
from packages.usecases.jwt import jwt_use_case
from services.organizations.types import CreateOrganizationDTO
from users.usecases.user import user_use_case


class AuthUseCase:
    def refresh(self, request: ExtendedRequest) -> Dict:
        return jwt_use_case.refresh(request.user)

    @transaction.atomic
    def login(self, request: ExtendedRequest, data: Dict) -> Dict:
        email = data.get("email")
        password = data.get("password")

        user = authenticate(request=request, email=email, password=password)

        session = jwt_use_case.sign(user)

        member = user.member

        session["user"] = user.id
        session["role"] = member.role
        session["org"] = organization_use_case.get_role_by_member(member_id=member.id)

        return session

    @transaction.atomic
    def register(self, data: Dict) -> Dict:
        dto = CreateOrganizationDTO(
            name=data.get("name"),
            inn=data.get("inn"),
            email=data.get("email"),
            phone=data.get("phone"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            surname=data.get("surname"),
            position=data.get("position"),
            password=data.get("password"),
            role=data.get("role"),
        )

        organization_use_case.register(dto)

        return data


auth_use_case = AuthUseCase()
