from directory.serializers import FederalAuthoritySerializer
from directory.usecases.federal_authority import FederalAuthorityUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class FederalAuthoritySetController(BaseSetController):
    prefix = "federal_authorities"

    use_case = FederalAuthorityUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = FederalAuthoritySerializer
