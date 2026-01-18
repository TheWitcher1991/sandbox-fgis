from directory.serializers import CultureSerializer
from directory.usecases.culture import CultureUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class CultureSetController(BaseSetController):
    prefix = "culture"

    use_case = CultureUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = CultureSerializer
