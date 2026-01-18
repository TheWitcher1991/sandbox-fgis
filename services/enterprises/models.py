from django.db import models

from config.settings import CHAR_MAX_LENGTH
from packages.kernel.adapters import OrganizationAdapter
from packages.kernel.utils import t


class Shipper(OrganizationAdapter):
    name = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Грузоотправитель")
        verbose_name_plural = t("Грузоотправители")


class Authority(OrganizationAdapter):
    name = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)
    district = models.ForeignKey(
        to="directory.District",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Федеральный орган исполнительной власти")
        verbose_name_plural = t("Федеральные органы исполнительной власти")
