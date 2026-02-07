from applications.models import Application
from packages.kernel.adapters import FilterAdapter


class ApplicationFilter(FilterAdapter):

    class Meta:
        model = Application
        fields = ()
