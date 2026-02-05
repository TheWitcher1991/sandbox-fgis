from typing import NewType, TypedDict

from django.db import models

from packages.kernel.utils import t

ManufacturerId = NewType("ManufacturerId", int)
ShipperId = NewType("ShipperId", int)
ConsigneeId = NewType("ConsigneeId", int)
AuthorityId = NewType("AuthorityId", int)


class AuthorityType(models.TextChoices):
    MINISTRY = ("ministry", t("Федеральное министерство"))
    SERVICE = ("service", t("Федеральная служба"))
    AGENCY = ("agency", t("Федеральное агентство"))


class CreateManufacturerDTO(TypedDict):
    pass


class UpdateManufacturerDTO(TypedDict):
    pass


class CreateShipperDTO(TypedDict):
    pass


class UpdateShipperDTO(TypedDict):
    pass


class CreateConsigneeDTO(TypedDict):
    pass


class UpdateConsigneeDTO(TypedDict):
    pass
