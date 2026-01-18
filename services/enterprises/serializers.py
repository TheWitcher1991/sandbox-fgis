from enterprises.models import Authority, Consignee, Shipper, Manufacturer
from packages.kernel.adapters import ModelSerializerAdapter


class ManufacturerSerializer(ModelSerializerAdapter):

    class Meta:
        model = Manufacturer
        fields = "__all__"


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
