from django.db import models

from config.settings.base import CHAR_MAX_LENGTH
from packages.kernel.adapters import ModelAdapter, UserModelAdapter
from packages.kernel.utils import t
from users.types import EmployeeRole


class User(UserModelAdapter):
    email = models.EmailField(t("Email"), max_length=CHAR_MAX_LENGTH, unique=True)
    phone = models.TextField(t("Телефон"), max_length=36, unique=True)
    password = models.CharField(t("Пароль"), max_length=CHAR_MAX_LENGTH)
    first_name = models.CharField(t("Имя"), max_length=CHAR_MAX_LENGTH)
    last_name = models.CharField(t("Фамилия"), max_length=CHAR_MAX_LENGTH)
    surname = models.CharField(t("Отчество"), max_length=CHAR_MAX_LENGTH, blank=True, null=True)
    date_joined = models.DateTimeField(t("Дата регистрации"), auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone"]

    class Meta:
        ordering = ("-date_joined",)
        verbose_name = t("Пользователь")
        verbose_name_plural = t("Пользователи")


class Employee(ModelAdapter):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    organization = models.ForeignKey(
        to="organizations.Organization", on_delete=models.CASCADE, related_name="employees"
    )
    role = models.CharField(max_length=20, choices=EmployeeRole.choices, default=EmployeeRole.OPERATOR)
    position = models.CharField(t(), max_length=CHAR_MAX_LENGTH, blank=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Сотрудник")
        verbose_name_plural = t("Сотрудники")
