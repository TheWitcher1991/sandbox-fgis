from rest_framework.permissions import BasePermission

from packages.kernel.types import ExtendedRequest


class IsAuthenticated(BasePermission):

    def has_permission(self, request: ExtendedRequest, view):
        return bool(request.user and request.user.is_authenticated)


class IsSuperUser(IsAuthenticated):

    def has_permission(self, request: ExtendedRequest, view):
        return bool(request.user.is_superuser)
