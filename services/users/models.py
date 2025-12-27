from django.db import models

from config.settings.base import CHAR_MAX_LENGTH
from packages.kernel.adapters import UserModelAdapter
from packages.kernel.utils import t


class User(UserModelAdapter):
    email = models.EmailField(t("Email"), max_length=CHAR_MAX_LENGTH, unique=True, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [""]

    class Meta:
        ordering = ("-date_joined",)
        verbose_name = t("Пользователь")
        verbose_name_plural = t("Пользователи")
