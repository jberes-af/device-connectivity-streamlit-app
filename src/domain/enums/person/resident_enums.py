# resident_enums.py

from enum import StrEnum


class ResidentAccessLevelEnum(StrEnum):
    READ_ONLY = "Read Only"
    CAREGIVER = "Caregiver"
    MANAGER = "Manager"
    ADMIN = "Admin"
