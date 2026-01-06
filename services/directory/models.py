from django.db import models

from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class SeedReproduction(ModelAdapter):
    name = models.CharField(t("Название"), max_length=255)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Репродукция семян")
        verbose_name_plural = t("Репродукции семян")


class PurposeImport(ModelAdapter):
    name = models.CharField(t("Название"), max_length=255)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Цель импорта")
        verbose_name_plural = t("Цели импорта")


class WhatImport(ModelAdapter):
    name = models.CharField(t("Название"), max_length=255)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Тип импорта")
        verbose_name_plural = t("Типы импорта")


class Culture(ModelAdapter):
    name = models.CharField(t("Название"), max_length=255)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Культура")
        verbose_name_plural = t("Культуры")
