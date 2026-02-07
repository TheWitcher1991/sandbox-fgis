from directory.models import Country, Culture, District, Region, SeedReproduction, TargetParty, WhatParty
from packages.kernel.adapters import FilterAdapter


class SeedReproductionFilter(FilterAdapter):

    class Meta:
        model = SeedReproduction
        fields = ("name",)


class CultureFilter(FilterAdapter):

    class Meta:
        model = Culture
        fields = ("name",)


class CountryFilter(FilterAdapter):

    class Meta:
        model = Country
        fields = ("name",)


class DistrictFilter(FilterAdapter):

    class Meta:
        model = District
        fields = ("name",)


class RegionFilter(FilterAdapter):

    class Meta:
        model = Region
        fields = ("name",)


class TargetPartyFilter(FilterAdapter):

    class Meta:
        model = TargetParty
        fields = ("name",)


class WhatPartyFilter(FilterAdapter):

    class Meta:
        model = WhatParty
        fields = ("name",)
