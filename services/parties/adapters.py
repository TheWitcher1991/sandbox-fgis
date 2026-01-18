from django.db import models

from packages.kernel.adapters import DocumentModelAdapter, ModelAdapter
from packages.kernel.utils import t


class PartyAdapter(DocumentModelAdapter):
    organization = models.ForeignKey(
        to="organizations.Organization",
        verbose_name=t("Организация"),
        on_delete=models.CASCADE,
        related_name="import_parties",
    )
    user = models.ForeignKey(
        to="users.User", verbose_name=t("Автор"), on_delete=models.CASCADE, related_name="import_parties"
    )

    class Meta:
        abstract = True


class PartySeedAdapter(ModelAdapter):

    class Meta:
        abstract = True
