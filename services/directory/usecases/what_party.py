from directory.models import WhatParty
from directory.types import WhatPartyId
from packages.framework.usecases import UseCaseAdapter


class WhatPartyUseCase(UseCaseAdapter[WhatParty, WhatPartyId]):
    def __init__(self):
        super().__init__(WhatParty)


what_party_use_case = WhatPartyUseCase()
