from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from applications.types import ApplicationCertificationService, ApplicationCertificationStatus
from packages.kernel.adapters import DocumentModelAdapter
from packages.kernel.utils import t


class ApplicationCertification(DocumentModelAdapter):
    service = models.CharField(t("Услуга"), choices=ApplicationCertificationService.choices, max_length=32)
    status = models.CharField(
        t("Статус"),
        choices=ApplicationCertificationStatus.choices,
        default=ApplicationCertificationStatus.SENT_TO_AUTHORITY,
        max_length=32,
    )
    registration_date = models.DateField(t("Дата регистрации"), null=True, blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(t("ID объекта"))
    target = GenericForeignKey("content_type", "object_id")

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Заявка на сертификацию")
        verbose_name_plural = t("Заявки на сертификацию")
