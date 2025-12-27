from typing import Generic, Type, TypeVar

from django.db import models, transaction
from rest_framework.generics import get_object_or_404

from packages.kernel.utils import get_content_type_for_model

T = TypeVar("T", bound=models.Model)
K = TypeVar("K", bound=int)


class UseCaseAdapter(Generic[T, K]):
    """
    Базовый адаптер для работы с моделями Django.
    """

    def __init__(self, model: Type[T]):
        self.model: Type[T] = model

    @property
    def DoesNotExist(self):
        return self.model.DoesNotExist

    def optimize(self) -> models.QuerySet[T]:
        raise NotImplementedError()

    def content_type(self):
        return get_content_type_for_model(self.model)

    def count(self) -> int:
        return self.model.objects.count()

    def get_queryset(self) -> models.QuerySet[T]:
        return self.model.objects.get_queryset()

    def all(self) -> models.QuerySet[T]:
        return self.get_queryset().all()

    def filter(self, *args, **kwargs) -> models.QuerySet[T]:
        return self.get_queryset().filter(*args, **kwargs)

    def exclude(self, *args, **kwargs) -> models.QuerySet[T]:
        return self.get_queryset().exclude(*args, **kwargs)

    def get_by_id(self, pk: K) -> T:
        return self.get_queryset().get(id=pk)

    @transaction.atomic
    def get_by_id_for_update(self, pk: K) -> T:
        return self.get_queryset().select_for_update(skip_locked=True).get(id=pk)

    def get_by_key(self, key: str, value: any) -> T:
        return self.get_queryset().get(**{key: value})

    def get(self, **kwargs) -> T:
        return self.get_queryset().get(**kwargs)

    def ids(self, queryset: models.QuerySet) -> list[int]:
        return list(queryset.values_list("id", flat=True))

    def get_object_or_404(self, pk: int) -> T:
        return get_object_or_404(self.model, pk=pk)

    def create(self, **kwargs) -> T:
        return self.model.objects.create(**kwargs)

    def update(self, pk: K, **kwargs) -> int:
        return self.get_queryset().filter(id=pk).update(**kwargs)

    def get_or_create(self, **kwargs) -> models.QuerySet[T]:
        return self.get_queryset().get_or_create(**kwargs)

    def update_or_create(self, **kwargs) -> models.QuerySet[T]:
        return self.get_queryset().update_or_create(**kwargs)

    def delete(self, pk: K) -> tuple[int, dict]:
        return self.get_queryset().filter(id=pk).delete()
