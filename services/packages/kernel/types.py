from enum import StrEnum, auto

from django.http import HttpRequest
from rest_framework.views import Request


class ExtendedRequest(HttpRequest, Request):
    pass


class LoggerResource(StrEnum):
    kernel = auto()
