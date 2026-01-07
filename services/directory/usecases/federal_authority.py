from directory.models import FederalAuthority
from directory.types import FederalAuthorityId
from packages.framework.usecases import UseCaseAdapter


class FederalAuthorityUseCase(UseCaseAdapter[FederalAuthority, FederalAuthorityId]):
    def __init__(self):
        super().__init__(FederalAuthority)


federal_authority_use_case = FederalAuthorityUseCase()
