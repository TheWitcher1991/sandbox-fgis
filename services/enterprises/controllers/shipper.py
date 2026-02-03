from enterprises.filters import ShipperFilter
from enterprises.serializers import ShipperSerializer
from enterprises.usecases.shipper import ShipperUseCase, shipper_use_case
from organizations.adapters import OrganizationAdapter
from packages.framework.controllers import ModelSetBaseSetController
from packages.usecases.serializer import SerializerUseCase
from users.permissions import IsMemberAdminOrReadonly


class ShipperSetController(OrganizationAdapter, ModelSetBaseSetController):
    prefix = "shippers"

    queryset = shipper_use_case.optimize()
    use_case = ShipperUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = ShipperSerializer
    filterset_class = ShipperFilter
    permission_classes = (IsMemberAdminOrReadonly,)
