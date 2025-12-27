from typing import NewType

from django.db import models

from packages.kernel.utils import t

UserId = NewType("UserId", int)
EmployeeId = NewType("EmployeeId", int)


class EmployeeRole(models.TextChoices):
    admin = "admin", t("Администратор")
    operator = "operator", t("Оператор")
    viewer = "viewer", t("Просмотр")
