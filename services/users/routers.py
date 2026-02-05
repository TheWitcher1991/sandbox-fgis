from packages.framework.routers import auto_router
from users.controllers import MemberSetController, UserSetController

app_name = "users"

router = auto_router(UserSetController, MemberSetController)

urlpatterns = router.urls
