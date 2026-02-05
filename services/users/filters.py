from packages.kernel.adapters import FilterAdapter
from users.models import Member, User


class UserFilter(FilterAdapter):

    class Meta:
        model = User
        fields = ("first_name",)


class MemberFilter(FilterAdapter):

    class Meta:
        model = Member
        fields = ("role",)
