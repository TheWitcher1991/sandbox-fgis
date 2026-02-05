from django.db import transaction

from packages.framework.usecases import UseCaseAdapter
from packages.kernel.types import ExtendedRequest
from parties.models import ExportParty
from parties.types import CreateExportPartyDTO, ExportPartyId, UpdateExportPartyDTO


class ExportPartyUseCase(UseCaseAdapter[ExportParty, ExportPartyId]):
    def __init__(self):
        super().__init__(ExportParty)

    @transaction.atomic
    def add(self, request: ExtendedRequest, data: CreateExportPartyDTO):
        pass

    @transaction.atomic
    def edit(self, request: ExtendedRequest, data: UpdateExportPartyDTO):
        pass


export_party_use_case = ExportPartyUseCase()
