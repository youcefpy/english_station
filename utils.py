from django.db import models


def lesson_upload_path(instance, filename):
    return f"lesson/acadimic-level{instance.stream.level}/{instance.stream.name}/{instance.unit.name}/{filename}"


class AcadimicLevelChoices(models.IntegerChoices):
    FIRST_YEAR = 1
    SECOND_YEAR = 2
    THIRD_LEVEL = 3

class StreamNameChoices(models.TextChoices):
    # Common core (first year)
    COMMON_CORE_SCIENCE_TECH = "common_core_st", "Tronc commun Sciences et Technologie"
    COMMON_CORE_LETTERS = "common_core_letters", "Tronc commun Lettres"

    # Sciences et Technologie branch
    EXPERIMENTAL_SCIENCES = "experimental_sciences", "Sciences expérimentales"
    MATHEMATICS = "mathematics", "Mathématiques"
    TECHNICAL_MATHEMATICS = "technical_mathematics", "Technique mathématique"
    MANAGEMENT_ECONOMICS = "management_economics", "Gestion et économie"

    # Technique mathématique options
    MECHANICAL_ENGINEERING = "mechanical_engineering", "Génie mécanique"
    ELECTRICAL_ENGINEERING = "electrical_engineering", "Génie électrique"
    CIVIL_ENGINEERING = "civil_engineering", "Génie civil"
    PROCESS_ENGINEERING = "process_engineering", "Génie des procédés"

    # Lettres branch
    LITERATURE_PHILOSOPHY = "literature_philosophy", "Lettres et philosophie"
    FOREIGN_LANGUAGES = "foreign_languages", "Langues étrangères"