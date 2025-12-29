from django.db import models

from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t
from roles.types import RoleType


class Organization(ModelAdapter):
    name = models.CharField(t("Название"), max_length=255)
    inn = models.CharField(t("ИНН"), max_length=12)
    kpp = models.CharField(t("КПП"), max_length=9, blank=True, null=True)
    ogrn = models.CharField(t("ОГРН"), max_length=13, blank=True, null=True)
    oktmo = models.CharField(t("ОКТМО"), max_length=11, blank=True, null=True)
    legal_name = models.CharField(t("Наименование как в уставе"), max_length=255, blank=True, null=True)
    legal_address = models.CharField(t("Юридический адрес"), max_length=255, blank=True, null=True)
    actual_address = models.CharField(t("Фактический адрес"), max_length=255, blank=True, null=True)
    phone = models.CharField(t("Телефон"), max_length=20, blank=True, null=True)
    fax = models.CharField(t("Факс"), max_length=20, blank=True, null=True)
    email = models.EmailField(t("Электронная почта"), max_length=128, blank=True, null=True)
    role = models.ForeignKey(to="roles.Role", on_delete=models.CASCADE, related_name="organizations")

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Организация")
        verbose_name_plural = t("Организации")
