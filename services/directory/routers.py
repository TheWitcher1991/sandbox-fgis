from directory.controllers.country import CountrySetController
from directory.controllers.culture import CultureSetController
from directory.controllers.district import DistrictSetController
from directory.controllers.region import RegionSetController
from directory.controllers.seed_reproduction import SeedReproductionSetController
from directory.controllers.target_party import TargetPartySetController
from directory.controllers.what_party import WhatPartySetController
from packages.framework.routers import auto_router

app_name = "directory"

router = auto_router(
    CountrySetController,
    CultureSetController,
    DistrictSetController,
    TargetPartySetController,
    RegionSetController,
    SeedReproductionSetController,
    WhatPartySetController,
)

urlpatterns = router.urls
