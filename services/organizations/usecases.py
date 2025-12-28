from organizations.models import Organization
from organizations.types import OrganizationId
from packages.framework.usecases import UseCaseAdapter


class OrganizationUseCase(UseCaseAdapter[Organization, OrganizationId]):
    def __init__(self):
        super().__init__(Organization)


щrganization_use_case = OrganizationUseCase()
