from django.db import models

from config.settings.base import TEXT_MAX_LENGTH
from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t
from roles.types import RoleType


class Role(ModelAdapter):
    code = models.CharField(t("Роль"), choices=RoleType.choices, max_length=32, unique=True)
    description = models.TextField(t("Описание"), max_length=TEXT_MAX_LENGTH, black=True, null=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Роль")
        verbose_name_plural = t("Роли")
