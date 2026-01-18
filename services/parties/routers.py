from packages.framework.routers import auto_router
from parties.controllers.export_party import ExportPartySetController
from parties.controllers.import_party import ImportPartySetController

app_name = "enterprises"

router = auto_router(ExportPartySetController, ImportPartySetController)

urlpatterns = router.urls
