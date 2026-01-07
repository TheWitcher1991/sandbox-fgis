from directory.models import WhatImport
from directory.types import WhatImportId
from packages.framework.usecases import UseCaseAdapter


class WhatImportUseCase(UseCaseAdapter[WhatImport, WhatImportId]):
    def __init__(self):
        super().__init__(WhatImport)


what_import_use_case = WhatImportUseCase()
