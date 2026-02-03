from organizations.adapters import OrganizationAdapter
from packages.framework.controllers import ModelSetBaseSetController
from packages.usecases.serializer import SerializerUseCase
from parties.filters import ImportPartyFilter
from parties.serializers import ImportPartySerializer
from parties.usecases.import_party import ImportPartyUseCase, import_party_use_case
from users.permissions import IsMember


class ImportPartySetController(OrganizationAdapter, ModelSetBaseSetController):
    prefix = "imports"

    queryset = import_party_use_case.optimize()
    use_case = ImportPartyUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = ImportPartySerializer
    filterset_class = ImportPartyFilter
    permission_classes = (IsMember,)
