from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase
from parties.serializers import ExportPartySerializer
from parties.usecases.export_party import ExportPartyUseCase


class ExportPartySetController(BaseSetController):
    prefix = "exports"

    use_case = ExportPartyUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = ExportPartySerializer
