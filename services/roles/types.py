from re import A
from typing import NewType

from django.db import models

from packages.kernel.utils import t

RoleId = NewType("RoleId", int)


class RoleType(models.TextChoices):
    participant_in_turnover = "participant_in_turnover", t("Участник оборота")
    accredited_organization = "accredited_organization", t("Аккредитованная организация")
    scientific_organization = "scientific_organization", t("Научная организация")
