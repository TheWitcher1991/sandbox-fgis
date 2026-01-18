from packages.framework.usecases import UseCaseAdapter
from users.models import Member
from users.types import MemberId


class MemberUseCase(UseCaseAdapter[Member, MemberId]):
    def __init__(self):
        super().__init__(Member)

    def optimize(self):
        return self.objects.select_related("user", "organization")


member_use_case = MemberUseCase()
