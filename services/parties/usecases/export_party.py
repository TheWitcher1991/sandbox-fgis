from packages.framework.usecases import UseCaseAdapter
from parties.models import ExportParty
from parties.types import ExportPartyId


class ExportPartyUseCase(UseCaseAdapter[ExportParty, ExportPartyId]):
    def __init__(self):
        super().__init__(ExportParty)


export_party_use_case = ExportPartyUseCase()
