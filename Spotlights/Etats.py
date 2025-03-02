from django.db.models.enums import StrEnum


class Etat(StrEnum):
    BON = "BON"
    MOYEN = "MOYEN"
    MAUVAUS = "MAUVAUS"