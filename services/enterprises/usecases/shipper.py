from django.db import transaction

from enterprises.models import Shipper
from enterprises.types import CreateShipperDTO, ShipperId, UpdateShipperDTO
from packages.framework.usecases import UseCaseAdapter
from packages.kernel.types import ExtendedRequest


class ShipperUseCase(UseCaseAdapter[Shipper, ShipperId]):
    def __init__(self):
        super().__init__(Shipper)

    @transaction.atomic
    def add(self, request: ExtendedRequest, data: CreateShipperDTO):
        pass

    @transaction.atomic
    def edit(self, request: ExtendedRequest, data: UpdateShipperDTO):
        pass


shipper_use_case = ShipperUseCase()
