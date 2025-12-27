from ast import Dict
from typing import Any, Optional, Type

from packages.kernel.adapters import SerializerAdapter


class SerializerUseCase:
    """
    Базовый use case для работы с сериализаторами.
    Позволяет валидировать и сохранять данные через абстрактный SerializerAdapter.
    """

    def _get_valid_serializer(
        self, serializer_class: Type[SerializerAdapter], data: Any, context: Optional[Dict] = None
    ):
        serializer = serializer_class(data=data, context=context)
        serializer.is_valid(raise_exception=True)
        return serializer

    def save(self, serializer_class: Type[SerializerAdapter], data: Any, context: Optional[Dict] = None):
        serializer = self._get_valid_serializer(serializer_class, data, context)
        serializer.save()
        return serializer

    def is_valid(self, serializer_class: Type[SerializerAdapter], data: Any, context: Optional[Dict] = None):
        return self._get_valid_serializer(serializer_class, data, context)


serializer_use_case = SerializerUseCase()
