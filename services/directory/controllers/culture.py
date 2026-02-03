from directory.filters import CultureFilter
from directory.serializers import CultureSerializer
from directory.usecases.culture import CultureUseCase, culture_use_case
from packages.framework.controllers import ReadOnlySetController
from packages.usecases.serializer import SerializerUseCase


class CultureSetController(ReadOnlySetController):
    prefix = "culture"

    queryset = culture_use_case.optimize()
    use_case = CultureUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = CultureSerializer
    filterset_class = CultureFilter
