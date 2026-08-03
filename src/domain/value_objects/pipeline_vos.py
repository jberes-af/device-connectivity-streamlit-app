# /src/domain/value_objects/facility_texas_vos

from enum import StrEnum
from typing import Iterable


class EntityTypes(StrEnum):
    FACILITY = "Care Facility"
    CARE_SERVICE = "Care Service Agency"
    PACE = "PACE Program"

    @classmethod
    def options(cls) -> list["EntityTypes"]:
        return [*cls]

    @classmethod
    def name_to_database_key(cls, name: str) -> str:
        m: dict[str, str] = {
            "Care Facility": "facility",
            "Care Service Agency": "service",
            "PACE Program": "pace_program",
        }

        return m.get(name, None)


class States(StrEnum):
    AL = "Alabama"
    AK = "Alaska"
    AZ = "Arizona"
    AR = "Arkansas"
    CA = "California"
    CO = "Colorado"
    CT = "Connecticut"
    DE = "Delaware"
    FL = "Florida"
    GA = "Georgia"
    HI = "Hawaii"
    ID = "Idaho"
    IL = "Illinois"
    IN = "Indiana"
    IA = "Iowa"
    KS = "Kansas"
    KY = "Kentucky"
    LA = "Louisiana"
    ME = "Maine"
    MD = "Maryland"
    MA = "Massachusetts"
    MI = "Michigan"
    FM = "Micronesia"
    MN = "Minnesota"
    MS = "Mississippi"
    MO = "Missouri"
    MT = "Montana"
    NE = "Nebraska"
    NV = "Nevada"
    NH = "New Hampshire"
    NJ = "New Jersey"
    NM = "New Mexico"
    NY = "New York"
    NC = "North Carolina"
    ND = "North Dakota"
    MP = "Northern Marianas"
    OH = "Ohio"
    OK = "Oklahoma"
    OR = "Oregon"
    PA = "Pennsylvania"
    RI = "Rhode Island"
    SC = "South Carolina"
    SD = "South Dakota"
    TN = "Tennessee"
    TX = "Texas"
    UT = "Utah"
    VT = "Vermont"
    VI = "Virgin Islands"
    VA = "Virginia"
    WA = "Washington"
    WV = "West Virginia"
    WI = "Wisconsin"
    WY = "Wyoming"

    @classmethod
    def names(cls) -> list[str]:
        return ["All", *(state.value for state in cls)]

    @classmethod
    def name_to_code(cls) -> dict[str, str]:
        return {
            state.value: state.name
            for state in cls
        }

    @classmethod
    def code_to_name(cls) -> dict[str, str]:
        return {
            state.name: state.value
            for state in cls
        }


class TexasCounties(StrEnum):
    # BEXAR = "Bexar"
    COLLIN = "Collin"
    DALLAS = "Dallas"
    # HARRIS = "Harris"
    TARRANT = "Tarrant"
    # TRAVIS = "Travis"
