# src/domain/entities/care/adl_entities.py

"""

def get_adl_score_label(
    category: AdlCategoryEnum,
    score: int,
) -> str:
    return ADL_SCORE_LABELS[category][score]


def get_adl_score_definition(
    category: AdlCategoryEnum,
    score: int,
) -> str:
    return ADL_SCORE_DEFINITIONS[category][score]


definition = get_adl_score_definition(
    AdlCategoryEnum.BATHING,
    3,
)

"""

from dataclasses import dataclass

from src.domain.enums.care.adl_enums import (
    AdlCategoryEnum,
    AdlObservationCategoryEnum,
)


@dataclass(frozen=True)
class AdlScoreDefinition:
    adl_category: AdlCategoryEnum
    numeric_value: int
    score_label: str
    score_definition: str


@dataclass(frozen=True)
class AdlAssessmentRecordDTO:
    assessment_id: str
    tenant_id: str
    resident_id: str
    adl_category: AdlCategoryEnum
    adl_category_definition: str
    score_value: AdlScoreDefinition
    observed_at_iso: str
    recorded_at_iso: str
    recorded_by_user_id: str
    assessment_note: str | None = None


@dataclass(frozen=True)
class AdlObservationRecordDTO:
    observation_id: str
    resident_id: str
    category: AdlObservationCategoryEnum
    category_definition: str
    observation_note: str
    observed_at_iso: str
    recorded_at_iso: str
    recorded_by_user_id: str
