from auth.controllers import AuthSetController
from packages.framework.routers import auto_router

app_name = "auth"

router = auto_router(AuthSetController)

urlpatterns = router.urls
