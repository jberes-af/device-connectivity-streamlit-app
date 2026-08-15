# /src/domain/entities/monitoring_entities.py

from dataclasses import dataclass
from datetime import date, datetime

from src.domain.enums.sensing.analytics_enums import TrendDirectionEnum

@dataclass(frozen=True)
class MonitoringSummary:
    monitoring_summary_id: str
    patient_id: str
    monitoring_period_id: str
    measurement_period_start: date
    measurement_period_end: date
    generated_at: datetime


@dataclass(frozen=True)
class Device:
    device_id: str | None
    device_type: str | None
    monitoring_days: int
    days_with_data: int
    days_without_data: int
    data_completeness_pct: float


@dataclass(frozen=True)
class FunctionalActivitySummary:
    average_daily_activity: float | None
    average_daily_mobility_score: float | None
    average_daily_transfers: float | None
    average_daily_bed_exits: float | None
    average_daily_chair_transfers: float | None
    average_nighttime_activity: float | None


@dataclass(frozen=True)
class TrendIndicators:
    mobility_trend: TrendDirectionEnum
    transfer_trend: TrendDirectionEnum
    activity_trend: TrendDirectionEnum
    nighttime_activity_trend: TrendDirectionEnum


@dataclass(frozen=True)
class Adherence:
    exercise_adherence_pct: float | None
    device_usage_pct: float | None
    monitoring_adherence_pct: float | None


@dataclass(frozen=True)
class SignificantChanges:
    significant_improvement_detected: bool
    significant_decline_detected: bool
    new_fall_risk_detected: bool
    new_behavior_change_detected: bool


@dataclass(frozen=True)
class OutcomeProgress:
    goals_on_track: int
    goals_off_track: int
    goals_achieved: int


@dataclass(frozen=True)
class MonitoringQualification:
    meets_monitoring_requirement: bool
    qualifies_for_monthly_review: bool


@dataclass(frozen=True)
class ProviderReview:
    reviewed_by_provider: bool
    last_review_date: date | None


@dataclass(frozen=True)
class MonitoringSummary:
    monitoring_summary_id: str
    patient_id: str
    monitoring_period_id: str
    measurement_period_start: date
    measurement_period_end: date
    device_id: str | None
    device_type: str | None
    monitoring_days: int
    days_with_data: int
    days_without_data: int
    data_completeness_pct: float

    average_daily_activity: float | None
    average_daily_mobility_score: float | None
    average_daily_transfers: float | None
    average_daily_bed_exits: float | None
    average_daily_chair_transfers: float | None
    average_nighttime_activity: float | None

    mobility_trend: TrendDirectionEnum
    activity_trend: TrendDirectionEnum
    transfer_trend: TrendDirectionEnum
    nighttime_activity_trend: TrendDirectionEnum

    exercise_adherence_pct: float | None
    monitoring_adherence_pct: float | None

    total_alerts: int
    high_priority_alerts: int
    unresolved_alerts: int

    goals_on_track: int
    goals_off_track: int
    goals_achieved: int

    significant_improvement_detected: bool
    significant_decline_detected: bool

    meets_monitoring_requirement: bool
    qualifies_for_monthly_review: bool

    clinical_summary: str

    reviewed_by_provider: bool
    last_review_date: date | None

    billing_ready: bool

    generated_at: datetime
