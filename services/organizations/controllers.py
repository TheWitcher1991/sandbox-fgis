from organizations.usecases import OrganizationUseCase
from packages.framework.controllers import BaseSetController


class OrganizationSetController(BaseSetController):
    prefix = "organizations"

    use_case = OrganizationUseCase()
