from django.db import models

from directory.models import CultureTypeSelection
from directory.types import BatchUnit, PartyRefusalSolution, TypeSelection
from packages.kernel.utils import t
from parties.adapters import PartyAdapter, PartySeedAdapter


class ImportParty(PartyAdapter):
    target = models.ForeignKey(
        to="directory.TargetParty",
        verbose_name=t("Цель импорта"),
        on_delete=models.CASCADE,
        related_name="import_parties",
    )
    what = models.ForeignKey(
        to="directory.WhatParty",
        verbose_name=t("Тип импорта"),
        on_delete=models.CASCADE,
        related_name="import_parties",
    )
    manufacturer = models.ForeignKey(
        to="enterprises.Manufacturer",
        verbose_name=t("Производитель"),
        on_delete=models.CASCADE,
        related_name="import_parties",
    )
    shipper = models.ForeignKey(
        to="enterprises.Shipper",
        verbose_name=t("Грузоотправитель"),
        on_delete=models.CASCADE,
        related_name="import_parties",
    )
    authority = models.ForeignKey(
        to="enterprises.Authority",
        verbose_name=t("Орган власти"),
        on_delete=models.CASCADE,
        related_name="import_parties",
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Импорт партии")
        verbose_name_plural = t("Импорт партий")


class ImportPartySeed(PartySeedAdapter):
    culture = models.ForeignKey(
        to="directory.Culture",
        verbose_name=t("Культура"),
        on_delete=models.CASCADE,
        related_name="import_seeds",
    )
    selection = models.ForeignKey(
        to="directory.CultureTypeSelection",
        verbose_name=t("Сорт/гибрид"),
        on_delete=models.CASCADE,
        related_name="import_seeds",
    )
    reproduction = models.ForeignKey(
        to="directory.SeedReproduction",
        verbose_name=t("Репродукция"),
        on_delete=models.CASCADE,
        related_name="import_seeds",
    )
    country = models.ForeignKey(
        to="directory.Country",
        verbose_name=t("Страна"),
        on_delete=models.CASCADE,
        related_name="import_seeds",
    )
    quantity = models.PositiveIntegerField(t("Количество"))
    type_selection = models.CharField("Тип селекции", choices=TypeSelection.choices, max_length=32)
    unit = models.CharField("Единица измерения", choices=BatchUnit.choices, max_length=32)
    solution = models.CharField(t("Решение в случае отказа"), choices=PartyRefusalSolution.choices, max_length=32)
    admitted = models.BooleanField(t("Допущено"), default=False)
    party = models.ForeignKey(
        to=ImportParty,
        verbose_name=t("Импорт партии"),
        on_delete=models.CASCADE,
        related_name="import_seeds",
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Семена импорта")
        verbose_name_plural = t("Семена импорта")


class ExportParty(PartyAdapter):
    target = models.ForeignKey(
        to="directory.TargetParty",
        verbose_name=t("Цель экспорта"),
        on_delete=models.CASCADE,
        related_name="export_parties",
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Экспорт партии")
        verbose_name_plural = t("Экспорт партий")
