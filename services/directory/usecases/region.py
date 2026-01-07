from directory.models import Region
from directory.types import RegionId
from packages.framework.usecases import UseCaseAdapter


class RegionUseCase(UseCaseAdapter[Region, RegionId]):
    def __init__(self):
        super().__init__(Region)


region_use_case = RegionUseCase()
