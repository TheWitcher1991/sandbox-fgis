from django.db import models
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from packages.kernel.utils import t


class DocumentNumberField(models.CharField):
    """
    Поле для хранения номера документа в формате с ведущими нулями.
    Пример: 000000212, 000001234, 000056789
    """

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 9)
        kwargs.setdefault("unique", True)
        kwargs.setdefault("verbose_name", "Номер документа")
        kwargs.setdefault("help_text", "Формат: 000000212 (9 символов, ведущие нули)")

        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if kwargs.get("max_length") == 9:
            del kwargs["max_length"]
        if kwargs.get("unique") is True:
            del kwargs["unique"]
        return name, path, args, kwargs

    def validate(self, value, model_instance):
        super().validate(value, model_instance)

        # Проверка формата
        if not value.isdigit():
            raise ValidationError(t("Номер документа должен содержать только цифры."), code="invalid_format")

        if len(value) != 9:
            raise ValidationError(t("Номер документа должен содержать ровно 9 цифр."), code="invalid_length")

    def get_prep_value(self, value):
        if value is None:
            return value
        value = str(value).strip()
        if value.isdigit():
            return value.zfill(9)

        return value

    def from_db_value(self, value, expression, connection):
        return value

    def to_python(self, value):
        if value is None:
            return value

        if isinstance(value, int):
            value = str(value)

        if isinstance(value, str):
            value = value.strip()
            if value.isdigit():
                return value.zfill(9)

        return value


class NullableIntegerField(serializers.IntegerField):
    def to_internal_value(self, data):
        if data in ("", None):
            return None
        return super().to_internal_value(data)


class ContentTypeField(serializers.RelatedField):
    def to_representation(self, value):
        if not value:
            return None
        return {
            "id": value.id,
            "app_label": value.app_label,
            "model": value.model,
        }
