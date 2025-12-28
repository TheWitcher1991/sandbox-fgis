from typing import NewType

from django.db import models

from packages.kernel.utils import t

RoleId = NewType("RoleId", int)


class RoleType(models.TextChoices):
    seed_org = "seed_org", t("Участник оборота")
    accred_org = "accred_org", t("Аккредитованное лицо")
    science_org = "science_org", t("Научная организация")
    gov_org = "gov_org", t("Государственное учреждение")
