from organizations.adapters import OrganizationAdapter
from packages.framework.controllers import ModelSetBaseSetController
from packages.kernel.types import ExtendedRequest
from packages.usecases.serializer import SerializerUseCase
from parties.filters import ExportPartyFilter
from parties.serializers import ExportPartySerializer
from parties.usecases.export_party import ExportPartyUseCase, export_party_use_case
from users.permissions import IsMember


class ExportPartySetController(OrganizationAdapter, ModelSetBaseSetController):
    prefix = "exports"

    queryset = export_party_use_case.optimize()
    use_case = ExportPartyUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = ExportPartySerializer
    filterset_class = ExportPartyFilter
    permission_classes = (IsMember,)

    def create(self, request: ExtendedRequest, *args, **kwargs):
        serializer = self.serializer_use_case.is_valid(serializer_class=self.get_serializer_class(), data=request.data)

        result = self.use_case.add(request, serializer.validated_data)

        return self.get_response(result)

    def update(self, request: ExtendedRequest, *args, **kwargs):
        serializer = self.serializer_use_case.is_valid(serializer_class=self.get_serializer_class(), data=request.data)

        result = self.use_case.edit(request, serializer.validated_data)

        return self.get_response(result)
