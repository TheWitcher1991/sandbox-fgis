from directory.serializers import TargetPartySerializer
from directory.usecases.target_patry import TargetPartyUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class TargetPartySetController(BaseSetController):
    prefix = "target_parties"

    use_case = TargetPartyUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = TargetPartySerializer
