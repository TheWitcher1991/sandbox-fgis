from enterprises.filters import AuthorityFilter
from enterprises.serializers import AuthoritySerializer
from enterprises.usecases.authority import AuthorityUseCase, authority_use_case
from packages.framework.controllers import ReadOnlySetController
from packages.usecases.serializer import SerializerUseCase


class AuthoritySetController(ReadOnlySetController):
    prefix = "authorities"

    queryset = authority_use_case.optimize()
    use_case = AuthorityUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = AuthoritySerializer
    filterset_class = AuthorityFilter
