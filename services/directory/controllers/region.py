from directory.serializers import RegionSerializer
from directory.usecases.region import RegionUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class RegionSetController(BaseSetController):
    prefix = "regions"

    use_case = RegionUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = RegionSerializer
