from directory.controllers.country import CountrySetController
from directory.controllers.culture import CultureSetController
from directory.controllers.district import DistrictSetController
from directory.controllers.federal_authority import FederalAuthoritySetController
from directory.controllers.purpose_import import PurposeImportSetController
from directory.controllers.region import RegionSetController
from directory.controllers.seed_reproduction import SeedReproductionSetController
from directory.controllers.what_import import WhatImportSetController
from packages.framework.routers import auto_router

app_name = "directory"

router = auto_router(
    CountrySetController,
    CultureSetController,
    DistrictSetController,
    FederalAuthoritySetController,
    PurposeImportSetController,
    RegionSetController,
    SeedReproductionSetController,
    WhatImportSetController,
)

urlpatterns = router.urls
