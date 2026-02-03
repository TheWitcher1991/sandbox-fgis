from packages.kernel.adapters import FilterAdapter
from parties.models import ExportParty, ImportParty


class ImportPartyFilter(FilterAdapter):

    class Meta:
        model = ImportParty
        fields = ("status",)


class ExportPartyFilter(FilterAdapter):

    class Meta:
        model = ExportParty
        fields = ("status",)
