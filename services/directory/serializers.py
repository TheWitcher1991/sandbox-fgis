from directory.models import (
    Country,
    Culture,
    District,
    Region,
    SeedReproduction,
    TargetParty,
    WhatParty,
)
from packages.kernel.adapters import ModelSerializerAdapter


class SeedReproductionSerializer(ModelSerializerAdapter):

    class Meta:
        model = SeedReproduction
        fields = "__all__"


class TargetPartySerializer(ModelSerializerAdapter):

    class Meta:
        model = TargetParty
        fields = "__all__"


class WhatPartySerializer(ModelSerializerAdapter):

    class Meta:
        model = WhatParty
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
