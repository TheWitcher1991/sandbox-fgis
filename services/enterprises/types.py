from typing import NewType

from django.db import models

from packages.kernel.utils import t

ManufacturerId = NewType("ManufacturerId", int)
ShipperId = NewType("ShipperId", int)
ConsigneeId = NewType("ConsigneeId", int)
AuthorityId = NewType("FederalAuthorityId", int)


class AuthorityType(models.TextChoices):
    MINISTRY = ("ministry", t("Федеральное министерство"))
    SERVICE = ("service", t("Федеральная служба"))
    AGENCY = ("agency", t("Федеральное агентство"))
