from organizations.adapters import OrganizationAdapter
from packages.framework.controllers import ModelSetBaseSetController
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
