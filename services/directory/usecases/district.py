from directory.models import District
from directory.types import DistrictId
from packages.framework.usecases import UseCaseAdapter


class DistrictUseCase(UseCaseAdapter[District, DistrictId]):
    def __init__(self):
        super().__init__(District)


district_use_case = DistrictUseCase()
