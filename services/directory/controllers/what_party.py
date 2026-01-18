from directory.serializers import WhatPartySerializer
from directory.usecases.what_party import WhatPartyUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class WhatPartySetController(BaseSetController):
    prefix = "what_parties"

    use_case = WhatPartyUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = WhatPartySerializer
