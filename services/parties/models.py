from django.db import models

from packages.kernel.utils import t
from parties.adapters import PartyAdapter


class ImportParty(PartyAdapter):
    target = models.ForeignKey(
        to="directory.TargetParty",
        verbose_name=t("Цель импорта"),
        on_delete=models.CASCADE,
        related_name="import_parties",
    )
    what = models.ForeignKey(
        to="directory.WhatParty",
        verbose_name=t("Тип импортируем"),
        on_delete=models.CASCADE,
        related_name="import_parties",
    )
    organization = models.ForeignKey(
        to="organizations.Organization",
        verbose_name=t("Импортер"),
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
    user = models.ForeignKey(
        to="users.User", verbose_name=t("Автор"), on_delete=models.CASCADE, related_name="import_parties"
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Импорт партии")
        verbose_name_plural = t("Импорт партий")


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
