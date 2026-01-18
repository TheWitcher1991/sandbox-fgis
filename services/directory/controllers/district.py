from directory.serializers import DistrictSerializer
from directory.usecases.district import DistrictUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class DistrictSetController(BaseSetController):
    prefix = "districts"

    use_case = DistrictUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = DistrictSerializer
