from packages.kernel.adapters import ModelSerializerAdapter
from parties.models import ExportParty, ImportParty


class ImportPartySerializer(ModelSerializerAdapter):

    class Meta:
        model = ImportParty
        fields = "__all__"


class ExportPartySerializer(ModelSerializerAdapter):

    class Meta:
        model = ExportParty
        fields = "__all__"
