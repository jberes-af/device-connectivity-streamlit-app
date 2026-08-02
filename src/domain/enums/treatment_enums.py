from dataclasses import dataclass
from datetime import date
from enum import StrEnum


class TreatmentPlanEntityType(StrEnum):
    PLAN = "plan"
    DIAGNOSIS = "diagnosis"
    GOAL = "goal"
    INTERVENTION = "intervention"
    OUTCOME_MEASURE = "outcome_measure"


class TreatmentPlanStatus(StrEnum):
    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    DISCONTINUED = "discontinued"


class TreatmentType(StrEnum):
    PHYSICAL_THERAPY = "physical_therapy"
    OCCUPATIONAL_THERAPY = "occupational_therapy"
    HOME_EXERCISE = "home_exercise"
    MEDICATION_MANAGEMENT = "medication_management"
    OTHER = "other"


class InterventionStatus(StrEnum):
    PLANNED = "planned"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class MeasurementPeriodStatus(StrEnum):
    OPEN = "open"
    CLOSED = "closed"
    BILLED = "billed"
    LOCKED = "locked"



class TreatmentPlanChangeAction(StrEnum):
    CREATED = "created"
    DIAGNOSIS_UPDATED = "diagnosis_updated"
    GOAL_ADDED = "goal_added"
    GOAL_UPDATED = "goal_updated"
    GOAL_DISCONTINUED = "goal_discontinued"
    INTERVENTION_ADDED = "intervention_added"
    INTERVENTION_UPDATED = "intervention_updated"
    INTERVENTION_DISCONTINUED = "intervention_discontinued"
    STATUS_CHANGED = "status_changed"
    OTHER = "other"

