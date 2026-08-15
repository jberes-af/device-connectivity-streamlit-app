# care_plan_entities

from dataclasses import dataclass
from datetime import datetime, date

from src.domain.enums.care.care_plan_enums import *


@dataclass(frozen=True)
class CarePlan:
    care_plan_id: str
    patient_id: str
    title: str
    summary: str | None
    created_by_user_id: str
    responsible_coordinator_id: str | None
    start_date: date
    target_review_date: date | None
    status: CarePlanStatus
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class FunctionalStatus:
    functional_status_id: str
    patient_id: str
    assessment_date: date
    assessed_by_user_id: str
    mobility: FunctionalLevel
    transfers: FunctionalLevel
    bathing: FunctionalLevel
    dressing: FunctionalLevel
    toileting: FunctionalLevel
    eating: FunctionalLevel
    continence: FunctionalLevel
    cognition: FunctionalLevel
    fall_risk: RiskLevel
    notes: str | None


@dataclass(frozen=True)
class CarePlanGoal:
    goal_id: str
    care_plan_id: str
    title: str
    description: str
    priority: GoalPriority
    target_date: date | None
    status: GoalStatus
    success_criteria: str | None


@dataclass(frozen=True)
class CarePlanTask:
    task_id: str
    care_plan_id: str
    related_goal_id: str | None
    title: str
    description: str
    assigned_role: CaregiverRole
    frequency: TaskFrequency
    preferred_time_of_day: str | None
    active: bool


@dataclass(frozen=True)
class CarePlanRisk:
    risk_id: str
    care_plan_id: str
    risk_type: CarePlanRiskType
    severity: RiskSeverity
    description: str
    mitigation_plan: str
    active: bool


@dataclass(frozen=True)
class CarePlanInstruction:
    instruction_id: str
    care_plan_id: str
    category: InstructionCategory
    title: str
    instruction: str
    applies_to_goal_id: str | None
    active: bool


"""

#### CP-04: Session Note DTO

@dataclass(frozen=True)
class SessionNoteDTO:
    note_id: str
    plan_id: str
    author_user_id: str
    note_type: str
    note_text: str
    created_at: str


#### CP-05: Plan Action DTO

@dataclass(frozen=True)
class PlanActionDTO:
    action_id: str
    title: str
    description: str
    category: str
    frequency: str
    assigned_role: str
    start_date: str
    end_date: str | None
    is_required: bool


#### CP-06: Plan Milestone DTO

@dataclass(frozen=True)
class PlanMilestoneDTO:
    milestone_id: str
    description: str
    date: str
    expected_outcome_metric: str


#### CP-07: Plan Schedule DTO

@dataclass(frozen=True)
class PlanScheduleDTO:
    start_date: str
    end_date: str
    review_frequency: str


#### CP-08: Plan Metric DTO

@dataclass(frozen=True)
class PlanMetricDTO:
    metric_id: str
    name: str
    unit: str
    source: str
    sensor_id: str | None = None


#### CP-09: Plan Progress Entry DTO

@dataclass(frozen=True)
class PlanProgressEntryDTO:
    progress_id: str
    metric_id: str
    target_value: float
    actual_value: float
    status: ProgressStatusEnum
    timestamp: str
    notes: str | None = None


#### CP-10: Plan Review DTO

@dataclass(frozen=True)
class PlanReviewDTO:
    review_id: str
    reviewed_by_user_id: str
    review_date: str
    summary: str
    changes_needed: bool
    next_review_date: str



#### CP-11: Plan Record DTO

@dataclass(frozen=True)
class PlanRecordDTO:
    plan_id: str
    tenant_id: str
    resident_id: str
    plan_type: CarePlanTypeEnum
    title: str
    problem: str
    baseline_status: str
    goal_description: str
    actions: tuple[PlanActionDTO, ...]
    metrics: tuple[PlanMetricDTO, ...]
    milestones: tuple[PlanMilestoneDTO, ...]
    progress_entries: tuple[PlanProgressEntryDTO, ...]
    session_notes: tuple[SessionNoteDTO, ...]
    plan_schedule: PlanScheduleDTO
    plan_status: PlanStatusEnum
    created_at: str
    updated_at: str


"""
