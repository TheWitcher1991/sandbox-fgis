from directory.filters import CountryFilter
from directory.serializers import CountrySerializer
from directory.usecases.country import CountryUseCase, country_use_case
from packages.framework.controllers import ReadOnlySetController
from packages.usecases.serializer import SerializerUseCase


class CountrySetController(ReadOnlySetController):
    prefix = "countries"

    queryset = country_use_case.optimize()
    use_case = CountryUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = CountrySerializer
    filterset_class = CountryFilter
