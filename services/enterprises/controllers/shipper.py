from enterprises.filters import ShipperFilter
from enterprises.serializers import ShipperSerializer
from enterprises.usecases.shipper import ShipperUseCase, shipper_use_case
from organizations.adapters import OrganizationAdapter
from packages.framework.controllers import ModelSetBaseSetController
from packages.kernel.types import ExtendedRequest
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

    def create(self, request: ExtendedRequest, *args, **kwargs):
        serializer = self.serializer_use_case.is_valid(serializer_class=self.get_serializer_class(), data=request.data)

        result = self.use_case.add(request, serializer.validated_data)

        return self.get_response(result)

    def update(self, request: ExtendedRequest, *args, **kwargs):
        serializer = self.serializer_use_case.is_valid(serializer_class=self.get_serializer_class(), data=request.data)

        result = self.use_case.edit(request, serializer.validated_data)

        return self.get_response(result)
