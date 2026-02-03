from directory.filters import TargetPartyFilter
from directory.serializers import TargetPartySerializer
from directory.usecases.target_patry import TargetPartyUseCase, target_party_use_case
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class TargetPartySetController(BaseSetController):
    prefix = "target_parties"

    queryset = target_party_use_case.optimize()
    use_case = TargetPartyUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = TargetPartySerializer
    filterset_class = TargetPartyFilter
