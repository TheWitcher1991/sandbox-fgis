from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import QuerySet
from django_filters.rest_framework import CharFilter, FilterSet
from rest_framework import serializers

from packages.kernel.utils import t


class ModelAdapter(models.Model):
    created_at = models.DateTimeField(t("Дата создания"), auto_now_add=True)
    updated_at = models.DateTimeField(t("Дата обновления"), auto_now=True)

    class Meta:
        abstract = True


class UserModelAdapter(AbstractUser):
    objects = UserManager()

    class Meta:
        abstract = True


class OrganizationAdapter(ModelAdapter):
    inn = models.CharField(t("ИНН"), max_length=12)
    kpp = models.CharField(t("КПП"), max_length=9, blank=True, null=True)
    ogrn = models.CharField(t("ОГРН"), max_length=13, blank=True, null=True)
    oktmo = models.CharField(t("ОКТМО"), max_length=11, blank=True, null=True)
    legal_name = models.CharField(t("Наименование как в уставе"), max_length=255, blank=True, null=True)
    legal_date = models.DateField(t("Дата внесения в ЕГРЮЛ/ЕГРИП"), blank=True, null=True)
    legal_address = models.CharField(t("Юридический адрес"), max_length=255, blank=True, null=True)
    actual_address = models.CharField(t("Фактический адрес"), max_length=255, blank=True, null=True)
    phone = models.CharField(t("Телефон"), max_length=20, blank=True, null=True)
    fax = models.CharField(t("Факс"), max_length=20, blank=True, null=True)
    email = models.EmailField(t("Электронная почта"), max_length=128, blank=True, null=True)

    class Meta:
        abstract = True


class FilterAdapter(FilterSet):
    ordering = CharFilter(field_name="ordering", method="filter_ordering")

    def filter_ordering(self, queryset: QuerySet, name, value):
        return queryset.order_by(value)


class SerializerAdapter(serializers.Serializer):
    def to_dto(self, dto_class):
        return dto_class(**self.validated_data)


class ModelSerializerAdapter(serializers.ModelSerializer):
    def to_dto(self, dto_class):
        return dto_class(**self.validated_data)
