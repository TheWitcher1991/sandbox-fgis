from packages.framework.usecases import UseCaseAdapter
from packages.kernel.types import ExtendedRequest
from users.models import User
from users.types import UserId


class UserUseCase(UseCaseAdapter[User, UserId]):
    def __init__(self):
        super().__init__(User)

    def optimize(self):
        return self.objects.select_related("member")

    def obtain(self, request: ExtendedRequest) -> User:
        return request.user

    def anonymous(self):
        from django.contrib.auth.models import AnonymousUser

        return AnonymousUser()


user_use_case = UserUseCase()
