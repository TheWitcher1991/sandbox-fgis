from ast import Dict

from config.settings import AUTH_TOKEN_TYPE
from packages.kernel.utils import jwt_decode, jwt_encode, jwt_is_valid


class JWTUseCase:

    def sign(user) -> Dict:
        access_token, access_token_expires = jwt_encode(user)
        refresh_token, refresh_token_expires = jwt_encode(user, is_refresh=True)

        data = {
            "user": user,
            "refresh_token": refresh_token,
            "access_token": access_token,
            "session_expires": refresh_token_expires.timestamp(),
            "access_expires": access_token_expires.timestamp(),
            "token_type": AUTH_TOKEN_TYPE,
        }

        return data

    def refresh(user) -> Dict:
        access_token, access_token_expires = jwt_encode(user)

        data = {
            "access_token": access_token,
            "access_expires": access_token_expires.timestamp(),
        }

        return data

    def decode(token):
        return jwt_decode(token)

    def verify(token) -> bool:
        return jwt_is_valid(token)

    def authenticate(token: str):
        payload = jwt_decode(token)

        return {
            "user": "",
            "token": token,
        }


jwt_use_case = JWTUseCase()
