from rest_framework import status
from rest_framework.decorators import action

from auth.serializers import LoginSerializer, RegisterSerializer
from auth.usecases import AuthUseCase
from config.settings import REFRESH_TOKEN_NAME, SESSION_EXPIRE_TIMEOUT
from packages.framework.controllers import BaseSetController
from packages.framework.mixins import AllowAnyMixin
from packages.kernel.types import ExtendedRequest
from packages.usecases.serializer import SerializerUseCase
from users.usecases.user import user_use_case


class AuthSetController(AllowAnyMixin, BaseSetController):
    prefix = "auth"

    use_case = AuthUseCase()
    serializer_use_case = SerializerUseCase()

    @action(methods=["post"], url_path="login", serializer_class=LoginSerializer)
    def login(self, request: ExtendedRequest, *args, **kwargs):
        serializer = self.serializer_use_case.save(serializer_class=self.get_serializer_class(), data=request.data)

        result = self.use_case.login(request, serializer.validated_data)

        response = self.get_response(result, status=status.HTTP_200_OK)

        response.set_cookie(
            REFRESH_TOKEN_NAME,
            result.get("refresh_token"),
            httponly=True,
            secure=True,
            samesite="Strict",
            expires=SESSION_EXPIRE_TIMEOUT,
        )

        return response

    @action(methods=["post"], url_path="register", serializer_class=RegisterSerializer)
    def register(self, request: ExtendedRequest, *args, **kwargs):
        serializer = self.serializer_use_case.save(serializer_class=self.get_serializer_class(), data=request.data)

        result = self.use_case.register(serializer.validated_data)

        return self.get_response(result, status=status.HTTP_201_CREATED)

    @action(methods=["post"], url_path="logout")
    def logout(self, *args, **kwargs):
        response = self.get_response(status=status.HTTP_204_NO_CONTENT)

        response.delete_cookie(REFRESH_TOKEN_NAME)

        self.request.user = user_use_case.anonymous()

        return response

    @action(methods=["post"], url_path="refresh")
    def refresh(self, request: ExtendedRequest, *args, **kwargs):
        result = self.use_case.refresh(request)

        response = self.get_response(result)

        # response.set_cookie(
        #     REFRESH_TOKEN_NAME,
        #     result.get("refresh_token"),
        #     httponly=True,
        #     secure=True,
        #     samesite="Strict",
        #     expires=SESSION_EXPIRE_TIMEOUT
        # )

        return response
