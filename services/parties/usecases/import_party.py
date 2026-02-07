from django.db import transaction

from packages.framework.usecases import UseCaseAdapter
from packages.kernel.types import ExtendedRequest
from parties.models import ImportParty
from parties.types import CreateImportPartyDTO, ImportPartyId, UpdateImportPartyDTO


class ImportPartyUseCase(UseCaseAdapter[ImportParty, ImportPartyId]):
    def __init__(self):
        super().__init__(ImportParty)

    @transaction.atomic
    def add(self, request: ExtendedRequest, data: CreateImportPartyDTO):
        pass

    @transaction.atomic
    def edit(self, request: ExtendedRequest, data: UpdateImportPartyDTO):
        pass


import_party_use_case = ImportPartyUseCase()
