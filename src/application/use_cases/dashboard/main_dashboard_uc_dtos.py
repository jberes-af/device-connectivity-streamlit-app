# /src/application/use_cases/dashboard/main_dashboard_uc_dtos.py

from dataclasses import dataclass
from datetime import datetime

from src.domain.enums.priority_items.priority_item_enums import (
    PriorityItemLevelEnum,
)


@dataclass(frozen=True)
class DashboardResidentAttentionDTO:
    resident_id: str
    resident_name: str
    issue_summary: str
    priority: PriorityItemLevelEnum
    occurred_at: datetime | None


@dataclass(frozen=True)
class MainDashboardDTO:
    residents_requiring_attention_count: int
    residents_requiring_attention_delta: int | None

    priority_items_today_count: int
    priority_items_today_delta: int | None

    care_plans_current_rate: float
    care_plans_current_delta: float | None

    care_exception_count: int
    care_exception_delta: int | None

    residents_requiring_attention: tuple[DashboardResidentAttentionDTO, ...]

    residents_with_care_changes_count: int
    care_routine_exception_count: int
    care_routine_change_delta: int

    overdue_assessment_count: int
    assessments_due_today_count: int
    assessments_due_week_count: int

    monitored_resident_count: int
    total_monitorable_resident_count: int
    online_sensor_count: int
    total_sensor_count: int
    sensor_issue_count: int

    appointments_today_count: int
    provider_review_count: int
    follow_up_count: int


@dataclass(frozen=True)
class BuildDashboardMainPageRequestDTO:
    ...


@dataclass(frozen=True)
class BuildDashboardMainPageResultDTO:
    dashboard: MainDashboardDTO
