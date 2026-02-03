from directory.filters import RegionFilter
from directory.serializers import RegionSerializer
from directory.usecases.region import RegionUseCase, region_use_case
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class RegionSetController(BaseSetController):
    prefix = "regions"

    queryset = region_use_case.optimize()
    use_case = RegionUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = RegionSerializer
    filterset_class = RegionFilter
