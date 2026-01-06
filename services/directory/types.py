from django.db import models

from packages.kernel.utils import t


class CultureType(models.TextChoices):
    ARID = "arid", t("Аридные")
    MELON = "melon", t("Бахчевые")
    LEGUMINOUS_GRASSES = "leguminous_grasses", t("Бобовые травы")
    GRAPE = "grape", t("Виноград")
    MUSHROOMS = "mushrooms", t("Грибы")

    LEGUMES = "legumes", t("Зернобобовые")
    FORAGE_LEGUMES = "forage_legumes", t("Зернобобовые кормовые")
    CEREALS = "cereals", t("Зерновые")
    FORAGE_CEREALS = "forage_cereals", t("Зернокормовые")
    FEED_GRAIN = "feed_grain", t("Зернофуражные")
    GRASS_CROPS = "grass_crops", t("Злаковые травы")

    POTATO = "potato", t("Картофель")
    FORAGE_ROOTS = "forage_roots", t("Корнеплоды кормовые")
    GROATS = "groats", t("Крупяные")
    MEDICINAL = "medicinal", t("Лекарственные")
    FOREST = "forest", t("Лесные")

    OILSEEDS = "oilseeds", t("Масличные")
    HONEY = "honey", t("Медоносные")
    VEGETABLE = "vegetable", t("Овощные")
    NUT = "nut", t("Орехоплодные")

    STONE_FRUIT = "stone_fruit", t("Плодовые косточковые")
    POME_FRUIT = "pome_fruit", t("Плодовые семечковые")
    TROPICAL_FRUIT = "tropical_fruit", t("Плодовые тропические")

    FIBER = "fiber", t("Прядильные")
    SILAGE = "silage", t("Силосные")
    TECHNICAL = "technical", t("Технические")
    ORNAMENTAL = "ornamental", t("Цветочно-декоративные")

    CITRUS = "citrus", t("Цитрусовые и субтропические")
    ESSENTIAL_OIL = "essential_oil", t("Эфиромасличные")
    BERRY = "berry", t("Ягодные")

    OTHER = "other", t("Другое")


class SeedReproductionType(models.TextChoices):
    uncategorized = "uncategorized", t("Без категории")
    original = "original", t("Оригинальные")
    reproductive = "reproductive", t("Репродукционные")
    elite = "elite", t("Элитные")


class PurposeImportType(models.TextChoices):
    SCIENTIFIC_RESEARCH = ("scientific_research", t("Для проведения научных исследований"))
    EXPERT_EXAMINATION = ("expert_examination", t("Для проведения экспертиз"))
    COMMERCIAL_PRODUCTION = ("commercial_production", t("Для производства товарной продукции"))
    RETAIL_PACKAGING = ("retail_packaging", t("Для реализации в потребительской упаковке"))
    FEED_PURPOSE = ("feed_purpose", t("Кормовые цели"))
    EDUCATIONAL_PURPOSE = ("educational_purpose", t("Образовательные цели"))
    FOOD_PURPOSE = ("food_purpose", t("Пищевые цели"))
    SEED_PURPOSE = ("seed_purpose", t("Семенные"))
    TECHNICAL_PURPOSE = ("technical_purpose", t("Технические цели"))
    COMMODITY_PURPOSE = ("commodity_purpose", t("Товарные"))


class WhatImportType(models.TextChoices):
    TRANSIT_VIA_EAEU = ("transit_via_eaeu", t("Ввоз семян транзитом через страну ЕАЭС"))
    TRANSIT_VIA_EAEU_WITH_CUSTOMS = (
        "transit_via_eaeu_with_customs",
        t("Ввоз семян транзитом через страну ЕАЭС с проведением таможенного контроля в стране ЕАЭС"),
    )
    IMPORT_FROM_EAEU = ("import_from_eaeu", t("Ввоз семян из страны ЕАЭС"))
    IMPORT_FROM_NON_EAEU = ("import_from_non_eaeu", t("Ввоз семян из страны, не входящей в ЕАЭС"))


class DocumentStatus(models.TextChoices):
    draft = "draft", t("Черновик")
    at_work = "at_work", t("В работе")
    prepared = "prepared", t("Подготовлен")
    wait_sign = "wait_sign", t("Ожидает подписания")
    signed = "signed", t("Подписан")
    completed = "completed", t("Завершен")


class BatchUnit(models.TextChoices):
    gram = "g", t("Грамм")
    kilogram = "kg", t("Килограмм")
    liter = "l", t("Литр")
    piece = "pcs", t("Штука")
    package = "pkg", t("Упаковка")


class TypeSelection(models.TextChoices):
    variety = "variety", t("Сорт")
    hybrid = "hybrid", t("Гибрид")
    line = "line", t("Линия")
