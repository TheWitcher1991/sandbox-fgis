from packages.framework.usecases import UseCaseAdapter
from parties.models import ImportParty
from parties.types import ImportPartyId


class ImportPartyUseCase(UseCaseAdapter[ImportParty, ImportPartyId]):
    def __init__(self):
        super().__init__(ImportParty)


import_party_use_case = ImportPartyUseCase()
