from directory.serializers import CountrySerializer
from directory.usecases.country import CountryUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class CountrySetController(BaseSetController):
    prefix = "countries"

    use_case = CountryUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = CountrySerializer
