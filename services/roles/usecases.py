from packages.framework.usecases import UseCaseAdapter
from roles.models import Role
from roles.types import RoleId


class RoleUseCase(UseCaseAdapter[Role, RoleId]):
    def __init__(self):
        super().__init__(Role)


role_use_case = RoleUseCase()
