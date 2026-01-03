from typing import TypedDict

from packages.kernel.types import JWTSignedSession


class LoginData(TypedDict):
    email: str
    password: str


class LoginSession(JWTSignedSession):
    role: str
    org: int
