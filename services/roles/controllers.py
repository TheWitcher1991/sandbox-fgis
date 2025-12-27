from packages.framework.controllers import BaseSetController
from roles.usecases import RoleUseCase


class RoleSetController(BaseSetController):
    prefix = "roles"

    use_case = RoleUseCase()
