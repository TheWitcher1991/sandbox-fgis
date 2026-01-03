from organizations.models import Organization
from packages.kernel.adapters import ModelSerializerAdapter


class OrganizationSerializer(ModelSerializerAdapter):

    class Meta:
        model = Organization
        fields = "__all__"
