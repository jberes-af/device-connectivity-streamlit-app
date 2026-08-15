# care_plan_enums

from enum import StrEnum


class CarePlanStatus(StrEnum):
    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    DISCONTINUED = "discontinued"


class GoalPriority(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class GoalStatus(StrEnum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    ACHIEVED = "achieved"
    DISCONTINUED = "discontinued"


class CaregiverRole(StrEnum):
    FAMILY = "family"
    HOME_HEALTH_AIDE = "home_health_aide"
    CNA = "cna"
    NURSE = "nurse"
    THERAPIST = "therapist"
    CARE_MANAGER = "care_manager"
    OTHER = "other"


class TaskFrequency(StrEnum):
    CONTINUOUS = "continuous"
    EVERY_SHIFT = "every_shift"
    DAILY = "daily"
    WEEKLY = "weekly"
    AS_NEEDED = "as_needed"


class RiskSeverity(StrEnum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"


class CarePlanRiskType(StrEnum):
    FALL = "fall"
    WANDERING = "wandering"
    DEHYDRATION = "dehydration"
    MALNUTRITION = "malnutrition"
    PRESSURE_INJURY = "pressure_injury"
    MEDICATION = "medication"
    ELOPEMENT = "elopement"
    OTHER = "other"


class InstructionCategory(StrEnum):
    MOBILITY = "mobility"
    TRANSFERS = "transfers"
    ADLS = "adls"
    HYGIENE = "hygiene"
    NUTRITION = "nutrition"
    MEDICATION = "medication"
    SAFETY = "safety"
    COMMUNICATION = "communication"
    OTHER = "other"


class FunctionalLevel(StrEnum):
    INDEPENDENT = "independent"
    SETUP_ASSISTANCE = "setup_assistance"
    SUPERVISION = "supervision"
    LIMITED_ASSISTANCE = "limited_assistance"
    EXTENSIVE_ASSISTANCE = "extensive_assistance"
    TOTAL_ASSISTANCE = "total_assistance"
    NOT_APPLICABLE = "not_applicable"


class RiskLevel(StrEnum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    VERY_HIGH = "very_high"






"""
    class CarePlanTypeEnum(StrEnum):
        CARE_PLAN = "Care Plan"
        THERAPY_PLAN = "Therapy Plan"


    class PlanStatusEnum(StrEnum):
        ACTIVE = "Active"
        INACTIVE = "Inactive"
        DISCONTINUED = "Discontinued"
        REPLACED = "Replaced"


    class ProgressStatusEnum(StrEnum):
        ON_TRACK = "On Track"
        AT_RISK = "At Risk"
        OFF_TRACK = "Off Track"
        COMPLETED = "Completed"


"""