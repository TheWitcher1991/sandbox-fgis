from enterprises.models import Shipper, Authority
from packages.kernel.adapters import ModelSerializerAdapter


class ShipperSerializer(ModelSerializerAdapter):

    class Meta:
        model = Shipper
        fields = "__all__"


class AuthoritySerializer(ModelSerializerAdapter):

    class Meta:
        model = Authority
        fields = "__all__"
