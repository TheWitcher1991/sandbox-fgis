from directory.models import SeedReproduction
from directory.types import SeedReproductionId
from packages.framework.usecases import UseCaseAdapter


class SeedReproductionUseCase(UseCaseAdapter[SeedReproduction, SeedReproductionId]):
    def __init__(self):
        super().__init__(SeedReproduction)


seed_reproduction_use_case = SeedReproductionUseCase()
