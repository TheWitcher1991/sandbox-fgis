import re
import threading

from django.db import transaction
from django.db.models import Max


class DocumentNumberGenerator:
    """
    Продвинутый генератор номеров документов.
    Поддерживает:
    - Префиксы (INV-, CONT-, etc.)
    - Год/месяц в номере
    - Резервирование номеров
    - Работу в многопоточной среде
    """

    def __init__(self, model_class, field_name="doc_number", format_str="{number:09d}"):
        self.model_class = model_class
        self.field_name = field_name
        self.format_str = format_str
        self._lock = threading.Lock()

    def _extract_number(self, value):
        if not value:
            return 0

        numbers = re.findall(r"\d+", str(value))
        if numbers:
            return int(numbers[-1])
        return 0

    def get_next_number(self, prefix="", year=None, month=None):
        with self._lock:
            filter_kwargs = {}

            if prefix:
                filter_kwargs[f"{self.field_name}__startswith"] = prefix

            queryset = self.model_class.objects.all()
            if filter_kwargs:
                queryset = queryset.filter(**filter_kwargs)

            max_value = queryset.aggregate(max_val=Max(self.field_name))["max_val"]

            if max_value:
                current_number = self._extract_number(max_value)
                next_number = current_number + 1
            else:
                next_number = 1

            parts = []

            if prefix:
                parts.append(prefix)

            if year:
                parts.append(str(year)[-2:])

            if month:
                parts.append(str(month).zfill(2))

            number_part = self.format_str.format(number=next_number)
            parts.append(number_part)

            return "".join(parts)

    @transaction.atomic
    def reserve_next_number(self, **kwargs):
        next_number = self.get_next_number(**kwargs)
        obj = self.model_class(**{self.field_name: next_number})
        obj.save(force_insert=True)
        return next_number
