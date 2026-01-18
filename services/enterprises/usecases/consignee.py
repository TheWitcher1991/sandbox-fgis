from enterprises.models import Consignee
from enterprises.types import ConsigneeId
from packages.framework.usecases import UseCaseAdapter


class ConsigneeUseCase(UseCaseAdapter[Consignee, ConsigneeId]):
    def __init__(self):
        super().__init__(Consignee)


consignee_use_case = ConsigneeUseCase()
