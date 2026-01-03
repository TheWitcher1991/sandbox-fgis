from rest_framework.decorators import action

from organizations.serializers import OrganizationSerializer
from organizations.usecases import OrganizationUseCase
from packages.framework.controllers import BaseSetController
from packages.kernel.types import ExtendedRequest
from packages.usecases.serializer import SerializerUseCase


class OrganizationSetController(BaseSetController):
    prefix = "organizations"

    use_case = OrganizationUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = OrganizationSerializer

    @action(methods=["get"], url_path="obtain")
    def obtain(self, request: ExtendedRequest, *args, **kwargs):
        serializer = self.get_serializer(self.use_case.obtain(request))
        return self.get_response(serializer.data)

    @action(methods=["put"], url_path="update")
    def update(self, request: ExtendedRequest, *args, **kwargs):
        org_id = self.use_case.get_by_request(request)

        serializer = self.serializer_use_case.is_valid(serializer_class=self.get_serializer_class(), data=request.data)

        result = self.use_case.edit(id=org_id, data=serializer.validated_data)

        return self.get_response(result)
