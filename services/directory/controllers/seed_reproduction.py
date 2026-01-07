from directory.serializers import SeedReproductionSerializer
from directory.usecases.seed_reproduction import SeedReproductionUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class SeedReproductionSetController(BaseSetController):
    prefix = "seed_reproductions"

    use_case = SeedReproductionUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = SeedReproductionSerializer
