from packages.kernel.utils import t
from parties.adapters import PartyAdapter


class ImportParty(PartyAdapter):

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Импорт партии")
        verbose_name_plural = t("Импорт партий")


class ExportParty(PartyAdapter):

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Экспорт партии")
        verbose_name_plural = t("Экспорт партий")
