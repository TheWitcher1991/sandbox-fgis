from enterprises.serializers import ManufacturerSerializer
from enterprises.usecases.manufacturer import ManufacturerUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class ManufacturerSetController(BaseSetController):
    prefix = "manufacturers"

    use_case = ManufacturerUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = ManufacturerSerializer
