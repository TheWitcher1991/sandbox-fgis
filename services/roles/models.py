from django.db import models

from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t
from roles.types import RoleType


class Role(ModelAdapter):
    role = models.CharField(t("Роль"), choices=RoleType.choices, max_length=32, unique=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Роль")
        verbose_name_plural = t("Роли")
