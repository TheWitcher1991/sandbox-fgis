from typing import NewType

from django.db import models

from packages.kernel.utils import t

UserId = NewType("UserId", int)
MemberId = NewType("MemberId", int)


class MemberRole(models.TextChoices):
    superadmin = "superadmin", t("Супер-администратор")
    admin = "admin", t("Администратор")
    operator = "operator", t("Оператор")
    viewer = "viewer", t("Просмотр")
    instructor = "instructor", t("Преподаватель")
    student = "student", t("Студент")
