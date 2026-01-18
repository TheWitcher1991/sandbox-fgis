from enterprises.models import Shipper
from enterprises.types import ShipperId
from packages.framework.usecases import UseCaseAdapter


class ShipperUseCase(UseCaseAdapter[Shipper, ShipperId]):
    def __init__(self):
        super().__init__(Shipper)


shipper_use_case = ShipperUseCase()
