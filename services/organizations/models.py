from django.db import models

from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t
from roles.types import RoleType


class Organization(ModelAdapter):
    name = models.CharField("Название", max_length=255)
    inn = models.CharField("ИНН", max_length=12)
    kpp = models.CharField("КПП", max_length=10, blank=True, null=True)
    ogrn = models.CharField("ОГРН или ОГРНИП", max_length=15)
    legal_name = models.CharField("Наименование как в уставе", max_length=255, blank=True, null=True)
    legal_address = models.CharField("Юридический адрес", max_length=255, blank=True, null=True)
    actual_address = models.CharField("Фактический адрес", max_length=255, blank=True, null=True)
    phone = models.CharField("Телефон", max_length=20, blank=True, null=True)
    fax = models.CharField("Факс", max_length=20, blank=True, null=True)
    email = models.EmailField("Электронная почта", max_length=128, blank=True, null=True)
    role = models.CharField(t("Роль"), choices=RoleType.choices, max_length=32, unique=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Организация")
        verbose_name_plural = t("Организации")
