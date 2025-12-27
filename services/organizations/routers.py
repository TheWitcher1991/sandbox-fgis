from organizations.controllers import OrganizationSetController
from packages.framework.routers import auto_router

app_name = "organizations"

router = auto_router(OrganizationSetController)

urlpatterns = router.urls
