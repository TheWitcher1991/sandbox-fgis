from directory.models import Country
from directory.types import CountryId
from packages.framework.usecases import UseCaseAdapter


class CountryUseCase(UseCaseAdapter[Country, CountryId]):
    def __init__(self):
        super().__init__(Country)


country_use_case = CountryUseCase()
