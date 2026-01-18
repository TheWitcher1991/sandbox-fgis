from enterprises.models import Authority
from enterprises.types import AuthorityId
from packages.framework.usecases import UseCaseAdapter


class AuthorityUseCase(UseCaseAdapter[Authority, AuthorityId]):
    def __init__(self):
        super().__init__(Authority)


authority_use_case = AuthorityUseCase()
