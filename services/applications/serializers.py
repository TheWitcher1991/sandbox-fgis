from applications.models import Application
from packages.kernel.adapters import ModelSerializerAdapter


class ApplicationSerializer(ModelSerializerAdapter):

    class Meta:
        model = Application
        fields = "__all__"
