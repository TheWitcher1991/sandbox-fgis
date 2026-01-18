from directory.models import TargetParty
from directory.types import TargetPartyId
from packages.framework.usecases import UseCaseAdapter


class TargetPartyUseCase(UseCaseAdapter[TargetParty, TargetPartyId]):
    def __init__(self):
        super().__init__(TargetParty)


target_party_use_case = TargetPartyUseCase()
