from packages.kernel.adapters import ModelAdapter
from packages.kernel.utils import t


class Application(ModelAdapter):

    class Meta:
        ordering = ("-created_at",)
        verbose_name = t("Заявки")
        verbose_name_plural = t("Заявка")
