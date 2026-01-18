from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase
from parties.serializers import ImportPartySerializer
from parties.usecases.import_party import ImportPartyUseCase


class ImportPartySetController(BaseSetController):
    prefix = "imports"

    use_case = ImportPartyUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = ImportPartySerializer
