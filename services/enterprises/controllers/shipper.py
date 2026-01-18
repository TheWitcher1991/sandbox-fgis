from enterprises.serializers import ShipperSerializer
from enterprises.usecases.shipper import ShipperUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class ShipperSetController(BaseSetController):
    prefix = "shippers"

    use_case = ShipperUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = ShipperSerializer
