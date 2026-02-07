from directory.filters import DistrictFilter
from directory.serializers import DistrictSerializer
from directory.usecases.district import DistrictUseCase, district_use_case
from packages.framework.controllers import ReadOnlySetController
from packages.usecases.serializer import SerializerUseCase


class DistrictSetController(ReadOnlySetController):
    prefix = "districts"

    queryset = district_use_case.optimize()
    use_case = DistrictUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = DistrictSerializer
    filterset_class = DistrictFilter
