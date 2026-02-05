from django.db import transaction

from enterprises.models import Consignee
from enterprises.types import ConsigneeId, CreateConsigneeDTO, UpdateConsigneeDTO
from packages.framework.usecases import UseCaseAdapter
from packages.kernel.types import ExtendedRequest


class ConsigneeUseCase(UseCaseAdapter[Consignee, ConsigneeId]):
    def __init__(self):
        super().__init__(Consignee)

    @transaction.atomic
    def add(self, request: ExtendedRequest, data: CreateConsigneeDTO):
        pass

    @transaction.atomic
    def edit(self, request: ExtendedRequest, data: UpdateConsigneeDTO):
        pass


consignee_use_case = ConsigneeUseCase()
