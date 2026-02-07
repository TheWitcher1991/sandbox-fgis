from directory.filters import WhatPartyFilter
from directory.serializers import WhatPartySerializer
from directory.usecases.what_party import WhatPartyUseCase, what_party_use_case
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class WhatPartySetController(BaseSetController):
    prefix = "what_parties"

    queryset = what_party_use_case.optimize()
    use_case = WhatPartyUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = WhatPartySerializer
    filterset_class = WhatPartyFilter
