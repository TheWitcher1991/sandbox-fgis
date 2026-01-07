from django.db import models

from config.settings import CHAR_MAX_LENGTH
from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class SeedReproduction(ModelAdapter):
    name = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Репродукция семян")
        verbose_name_plural = t("Репродукции семян")


class PurposeImport(ModelAdapter):
    name = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Цель импорта")
        verbose_name_plural = t("Цели импорта")


class WhatImport(ModelAdapter):
    name = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Тип импорта")
        verbose_name_plural = t("Типы импорта")


class Culture(ModelAdapter):
    name = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Культура")
        verbose_name_plural = t("Культуры")


class Country(models.Model):
    name = models.CharField("Название", max_length=CHAR_MAX_LENGTH)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Страна")
        verbose_name_plural = t("Страны")


class District(models.Model):
    name = models.CharField("Название", max_length=CHAR_MAX_LENGTH)
    country = models.ForeignKey(
        to=Country,
        on_delete=models.SET_NULL,
        related_name="districts",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Округ")
        verbose_name_plural = t("Округи")


class Region(models.Model):
    name = models.CharField("Название", max_length=CHAR_MAX_LENGTH)
    country = models.ForeignKey(
        to=Country,
        on_delete=models.SET_NULL,
        related_name="regions",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Субъект")
        verbose_name_plural = t("Субъекты")


class FederalAuthority(ModelAdapter):
    name = models.CharField(t("Название"), max_length=CHAR_MAX_LENGTH)
    district = models.ForeignKey(
        to=District,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Федеральный орган исполнительной власти")
        verbose_name_plural = t("Федеральные органы исполнительной власти")
