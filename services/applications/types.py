from typing import NewType, TypedDict

from django.db import models

from packages.kernel.utils import t

ApplicationId = NewType("ApplicationId", int)


class ApplicationCertificationService(models.TextChoices):
    RESEARCH_GMO = "research_gmo", t("Заявка на предоставление услуг (на исследование на ГМО)")
    SEEDS_QUALITY = "seed_quality", t("Заявка на определение сортовых качеств семян")
    SEEDS_SOWING = "seeds_sowing", t("Заявка на определение посевных (посадочных) качеств семян")
    SEEDS_VOLUMES = "seeds_volumes", t("Заявка на досмотр объема ввозимых семян")


class ApplicationCertificationStatus(models.TextChoices):
    DRAFT = "draft", t("Черновик")
    FORMED = "formed", t("Сформировано")
    SENT_TO_AUTHORITY = "sent_to_authority", t("Направлена в ведомство")
    REGISTERED_BY_AUTHORITY = "registered_by_authority", t("Зарегистрировано ведомством")
    UNDER_REVIEW = "under_review", t("На рассмотрении")
    IN_PROGRESS = "in_progress", t("В работе")
    NEEDS_REVISION = "needs_revision", t("На доработку")
    APPROBATION_DATE_APPROVED = "approbation_date_approved", t("Согласована дата апробации")
    DECISION_PENDING = "decision_pending", t("Ожидается принятие решения")
    PROCESSED = "processed", t("Обработана")
    APPROVED = "approved", t("Закрыт")
    REJECTED = "rejected", t("Отказано")
    REJECTED_BY_AUTHORITY = "rejected_by_authority", t("Отказано ведомством")
    CANCELLED = "cancelled", t("Аннулирован")


class CreateApplicationDTO(TypedDict):
    pass


class UpdateApplicationDTO(TypedDict):
    pass
