from rest_framework.exceptions import AuthenticationFailed

from packages.framework.authentication import BaseAPIAuthentication
from packages.kernel.utils import t
from packages.usecases.jwt import jwt_use_case
from users.usecases import user_use_case


class APIAuthentication(BaseAPIAuthentication):
    def authenticate(self, request):
        auth_header = self.get_auth_header(request)

        if not auth_header:
            raise AuthenticationFailed(t("Authorization header not found"))

        prefix, token = self.get_prefix_and_token(auth_header)

        if not prefix or not token:
            raise AuthenticationFailed(t(f"Invalid authorization header. Expected '{self.keyword} <access_token>'"))

        if prefix.lower() != self.keyword.lower():
            raise AuthenticationFailed(t(f'Invalid authorization header. Expected "{self.keyword} <access_token>"'))

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, key):
        decoded_payload = jwt_use_case.decode(key)

        if not decoded_payload:
            raise AuthenticationFailed(t("Access token not valid"))

        user_id = decoded_payload.get("user_id")
        if not user_id:
            raise AuthenticationFailed(t("Invalid token payload: missing user_id"))

        user = self.get_user(user_id)

        try:
            user = self.get_user(user_id)
        except user_use_case.DoesNotExist:
            raise AuthenticationFailed(t("No user matching this token"))

        return user, decoded_payload

    def get_user(self, user_id):
        return user_use_case.get_by_id(user_id)
