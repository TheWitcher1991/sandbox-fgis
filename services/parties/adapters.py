from django.db import models

from directory.types import DocumentStatus
from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class PartyAdapter(ModelAdapter):
    status = models.CharField(t("Статус"), choices=DocumentStatus.choices, default=DocumentStatus.draft, max_length=32)

    class Meta:
        abstract = True
