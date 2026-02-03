from directory.filters import SeedReproductionFilter
from directory.serializers import SeedReproductionSerializer
from directory.usecases.seed_reproduction import SeedReproductionUseCase, seed_reproduction_use_case
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class SeedReproductionSetController(BaseSetController):
    prefix = "seed_reproductions"

    queryset = seed_reproduction_use_case.optimize()
    use_case = SeedReproductionUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = SeedReproductionSerializer
    filterset_class = SeedReproductionFilter
