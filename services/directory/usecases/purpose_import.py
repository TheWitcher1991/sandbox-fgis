from directory.models import PurposeImport
from directory.types import PurposeImportId
from packages.framework.usecases import UseCaseAdapter


class PurposeImportUseCase(UseCaseAdapter[PurposeImport, PurposeImportId]):
    def __init__(self):
        super().__init__(PurposeImport)


purpose_import_use_case = PurposeImportUseCase()
