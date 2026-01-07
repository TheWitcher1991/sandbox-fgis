from directory.models import Culture
from directory.types import CultureId
from packages.framework.usecases import UseCaseAdapter


class CultureUseCase(UseCaseAdapter[Culture, CultureId]):
    def __init__(self):
        super().__init__(Culture)


culture_use_case = CultureUseCase()
