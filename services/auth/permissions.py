from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser

from packages.kernel.types import ExtendedRequest
from roles.types import RoleType
from users.types import MemberRole


class IsAuthenticated(BasePermission):

    def has_permission(self, request: ExtendedRequest, view):
        return bool(request.user and request.user.is_authenticated)


class IsSuperUser(IsAuthenticated):

    def has_permission(self, request: ExtendedRequest, view):
        return bool(request.user.is_superuser)
