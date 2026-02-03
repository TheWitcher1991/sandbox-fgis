from enterprises.filters import ConsigneeFilter
from enterprises.serializers import ConsigneeSerializer
from enterprises.usecases.consignee import ConsigneeUseCase, consignee_use_case
from organizations.adapters import OrganizationAdapter
from packages.framework.controllers import ModelSetBaseSetController
from packages.usecases.serializer import SerializerUseCase
from users.permissions import IsMemberAdminOrReadonly


class ConsigneeSetController(OrganizationAdapter, ModelSetBaseSetController):
    prefix = "consignees"

    queryset = consignee_use_case.optimize()
    use_case = ConsigneeUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = ConsigneeSerializer
    filterset_class = ConsigneeFilter
    permission_classes = (IsMemberAdminOrReadonly,)
