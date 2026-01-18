from enterprises.controllers.authority import AuthoritySetController
from enterprises.controllers.consignee import ConsigneeSetController
from enterprises.controllers.shipper import ShipperSetController
from packages.framework.routers import auto_router

app_name = "enterprises"

router = auto_router(AuthoritySetController, ShipperSetController, ConsigneeSetController)

urlpatterns = router.urls
