from ast import Dict

from django.db import transaction

from packages.framework.contrib import authenticate
from packages.kernel.types import ExtendedRequest
from packages.usecases.jwt import jwt_use_case
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

        session["user"] = user.id
        session["role"] = user.member.role

        return session

    @transaction.atomic
    def register(self, data: Dict) -> Dict:
        user_use_case.create(**data)
        return data


auth_use_case = AuthUseCase()
