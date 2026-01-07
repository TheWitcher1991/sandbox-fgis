from directory.models import (
    Country,
    Culture,
    District,
    FederalAuthority,
    PurposeImport,
    Region,
    SeedReproduction,
    WhatImport,
)
from packages.kernel.adapters import ModelSerializerAdapter


class SeedReproductionSerializer(ModelSerializerAdapter):

    class Meta:
        model = SeedReproduction
        fields = "__all__"


class PurposeImportSerializer(ModelSerializerAdapter):

    class Meta:
        model = PurposeImport
        fields = "__all__"


class WhatImportSerializer(ModelSerializerAdapter):

    class Meta:
        model = WhatImport
        fields = "__all__"


class CultureSerializer(ModelSerializerAdapter):

    class Meta:
        model = Culture
        fields = "__all__"


class CountrySerializer(ModelSerializerAdapter):

    class Meta:
        model = Country
        fields = "__all__"


class DistrictSerializer(ModelSerializerAdapter):

    class Meta:
        model = District
        fields = "__all__"


class RegionSerializer(ModelSerializerAdapter):

    class Meta:
        model = Region
        fields = "__all__"


class FederalAuthoritySerializer(ModelSerializerAdapter):

    class Meta:
        model = FederalAuthority
        fields = "__all__"
