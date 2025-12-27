from packages.framework.routers import auto_router
from roles.controllers import RoleSetController

app_name = "roles"

router = auto_router(RoleSetController)

urlpatterns = router.urls
