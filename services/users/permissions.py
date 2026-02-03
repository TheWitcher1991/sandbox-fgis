from rest_framework.permissions import BasePermission

from packages.kernel.types import ExtendedRequest
from users.types import MemberRole


class IsAuthenticated(BasePermission):

    def has_permission(self, request: ExtendedRequest, view):
        return bool(request.user and request.user.is_authenticated)


class IsSuperUser(IsAuthenticated):

    def has_permission(self, request: ExtendedRequest, view):
        return bool(request.user.is_superuser)


class IsMember(IsAuthenticated):
    def has_permission(self, request: ExtendedRequest, view):
        if not super().has_permission(request, view):
            return False

        return bool(request.user.member)


class IsMemberRole(IsMember):
    member_roles: set[MemberRole] = set()

    def has_permission(self, request: ExtendedRequest, view):
        if not super().has_permission(request, view):
            return False

        return request.user.member.role in self.member_roles


class IsMemberAdminOrReadonly(IsMember):

    def has_permission(self, request: ExtendedRequest, view):
        has_permission = super().has_permission(request, view)

        if has_permission:
            if request.method in ["GET", "HEAD", "OPTIONS"]:
                return True
            else:
                return request.user.member.role in {
                    MemberRole.superadmin,
                    MemberRole.admin,
                }
        else:
            return False


class IsAdmin(IsMemberRole):
    member_roles = {
        MemberRole.superadmin,
        MemberRole.admin,
    }


class IsOperator(IsMemberRole):
    member_roles = {
        MemberRole.superadmin,
        MemberRole.admin,
        MemberRole.operator,
    }


class IsInstructor(IsMemberRole):
    member_roles = {
        MemberRole.superadmin,
        MemberRole.admin,
        MemberRole.instructor,
    }


class IsStudent(IsMemberRole):
    member_roles = {
        MemberRole.student,
    }


class IsViewer(IsMemberRole):
    member_roles = {
        MemberRole.viewer,
    }
