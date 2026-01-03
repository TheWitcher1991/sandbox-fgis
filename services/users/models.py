from django.db import models

from config.settings import CHAR_MAX_LENGTH
from packages.kernel.adapters import ModelAdapter, UserModelAdapter
from packages.kernel.utils import t
from users.managers import UserManager
from users.types import MemberRole


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

    objects = UserManager()

    class Meta:
        ordering = ("-date_joined",)
        verbose_name = t("Пользователь")
        verbose_name_plural = t("Пользователи")


class Member(ModelAdapter):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    organization = models.ForeignKey(to="organizations.Organization", on_delete=models.CASCADE, related_name="members")
    role = models.CharField(t("Роль"), max_length=20, choices=MemberRole.choices, default=MemberRole.operator)
    position = models.CharField(t("Должность"), max_length=CHAR_MAX_LENGTH, blank=True, null=True)
    inn = models.CharField(t("ИНН"), max_length=12, blank=True, null=True)
    snils = models.CharField(t("СНИЛС"), max_length=11, blank=True, null=True)
    esia = models.CharField(t("ЕСИА"), max_length=255, blank=True, null=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Сотрудник")
        verbose_name_plural = t("Сотрудники")
