from django.db import models

from packages.kernel.adapters import OrganizationAdapter
from packages.kernel.utils import t


class Organization(OrganizationAdapter):
    name = models.CharField(t("Название"), max_length=255)
    role = models.ForeignKey(to="roles.Role", on_delete=models.CASCADE, related_name="organizations")

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Организация")
        verbose_name_plural = t("Организации")
