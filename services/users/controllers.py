from packages.framework.controllers import BaseSetController
from users.usecases import UserUseCase


class UserSetController(BaseSetController):
    prefix = "users"

    use_case = UserUseCase()
