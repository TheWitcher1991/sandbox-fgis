from django.db import transaction

from applications.models import Application
from applications.types import ApplicationId, CreateApplicationDTO, UpdateApplicationDTO
from packages.framework.usecases import UseCaseAdapter
from packages.kernel.types import ExtendedRequest


class ApplicationUseCase(UseCaseAdapter[Application, ApplicationId]):
    def __init__(self):
        super().__init__(Application)

    @transaction.atomic
    def add(self, request: ExtendedRequest, data: CreateApplicationDTO):
        pass

    @transaction.atomic
    def edit(self, request: ExtendedRequest, data: UpdateApplicationDTO):
        pass


application_use_case = ApplicationUseCase()
