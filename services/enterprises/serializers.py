from enterprises.models import Authority, Consignee, Shipper
from packages.kernel.adapters import ModelSerializerAdapter


class ShipperSerializer(ModelSerializerAdapter):

    class Meta:
        model = Shipper
        fields = "__all__"


class ConsigneeSerializer(ModelSerializerAdapter):

    class Meta:
        model = Consignee
        fields = "__all__"


class AuthoritySerializer(ModelSerializerAdapter):

    class Meta:
        model = Authority
        fields = "__all__"
