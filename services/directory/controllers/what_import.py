from directory.serializers import WhatImportSerializer
from directory.usecases.what_import import WhatImportUseCase
from packages.framework.controllers import BaseSetController
from packages.usecases.serializer import SerializerUseCase


class WhatImportSetController(BaseSetController):
    prefix = "what_imports"

    use_case = WhatImportUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = WhatImportSerializer
