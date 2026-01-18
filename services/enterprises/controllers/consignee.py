from enterprises.serializers import ConsigneeSerializer
from enterprises.usecases.consignee import ConsigneeUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class ConsigneeSetController(BaseSetController):
    prefix = "consignees"

    use_case = ConsigneeUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = ConsigneeSerializer
