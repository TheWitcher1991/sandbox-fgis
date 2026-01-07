from directory.serializers import PurposeImportSerializer
from directory.usecases.purpose_import import PurposeImportUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class PurposeImportSetController(BaseSetController):
    prefix = "purpose_imports"

    use_case = PurposeImportUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = PurposeImportSerializer
