from enum import StrEnum, auto

from django.http import HttpRequest
from rest_framework.request import wrap_attributeerrors
from rest_framework.views import Request

from users.models import User


class ExtendedRequest(HttpRequest, Request):

    @property
    def user(self) -> User:
        """
        Returns the user associated with the current request, as authenticated
        by the authentication classes provided to the request.
        """
        if not hasattr(self, "_user"):
            with wrap_attributeerrors():
                self._authenticate()
        return self._user


class LoggerResource(StrEnum):
    kernel = auto()
