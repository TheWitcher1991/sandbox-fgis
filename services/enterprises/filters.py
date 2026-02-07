from enterprises.models import Authority, Consignee, Manufacturer, Shipper
from packages.kernel.adapters import FilterAdapter


class ManufacturerFilter(FilterAdapter):

    class Meta:
        model = Manufacturer
        fields = ("name",)


class ShipperFilter(FilterAdapter):

    class Meta:
        model = Shipper
        fields = ("name",)


class ConsigneeFilter(FilterAdapter):

    class Meta:
        model = Consignee
        fields = ("name",)


class AuthorityFilter(FilterAdapter):

    class Meta:
        model = Authority
        fields = ("name",)
