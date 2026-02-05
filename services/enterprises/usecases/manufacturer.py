from django.db import transaction

from enterprises.models import Manufacturer
from enterprises.types import CreateManufacturerDTO, ManufacturerId, UpdateManufacturerDTO
from packages.framework.usecases import UseCaseAdapter
from packages.kernel.types import ExtendedRequest


class ManufacturerUseCase(UseCaseAdapter[Manufacturer, ManufacturerId]):
    def __init__(self):
        super().__init__(Manufacturer)

    @transaction.atomic
    def add(self, request: ExtendedRequest, data: CreateManufacturerDTO):
        pass

    @transaction.atomic
    def edit(self, request: ExtendedRequest, data: UpdateManufacturerDTO):
        pass


manufacturer_use_case = ManufacturerUseCase()
