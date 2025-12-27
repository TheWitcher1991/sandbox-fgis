from packages.framework.usecases import UseCaseAdapter
from users.models import User
from users.types import UserId


class UserUseCase(UseCaseAdapter[User, UserId]):
    def __init__(self):
        super().__init__(User)


user_use_case = UserUseCase()
