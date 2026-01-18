from enterprises.serializers import AuthoritySerializer
from enterprises.usecases.authority import AuthorityUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class AuthoritySetController(BaseSetController):
    prefix = "authorities"

    use_case = AuthorityUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = AuthoritySerializer
