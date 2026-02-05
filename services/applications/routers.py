from applications.controllers import ApplicationSetController
from packages.framework.routers import auto_router

app_name = "enterprises"

router = auto_router(ApplicationSetController)

urlpatterns = router.urls
