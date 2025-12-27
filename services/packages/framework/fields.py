from rest_framework import serializers


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
