from enterprises.models import Manufacturer
from enterprises.types import ManufacturerId
from packages.framework.usecases import UseCaseAdapter


class ManufacturerUseCase(UseCaseAdapter[Manufacturer, ManufacturerId]):
    def __init__(self):
        super().__init__(Manufacturer)


manufacturer_use_case = ManufacturerUseCase()
