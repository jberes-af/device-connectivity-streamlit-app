# /src/domain/entities/sensing/routine_entities.py

from dataclasses import dataclass

from src.domain.enums.sensing.analytics_enums import (
    AnalysisIntervalEnum,
    AnalysisTimeframeEnum,
)
from src.domain.enums.sensing.routine_enums import *
from src.domain.enums.sensing.device_enums import SensorStateDefinitionEnum


@dataclass(frozen=True)
class AlertaRoutineRule:
    sensor_id: str
    expected_sensor_state: SensorStateDefinitionEnum


@dataclass(frozen=True)
class AlertaRoutineState:
    routine_id: str
    timeframe_state: AlertaRoutineTimeframeStateEnum
    outcome_state: AlertaRoutineOutcomeStateEnum


@dataclass(frozen=True)
class AlertaRoutineProfile:
    routine_id: str
    tenant_id: str
    name: str
    start_time: str
    end_time: str
    rules: tuple[AlertaRoutineRule, ...]
    routine_state: AlertaRoutineState
    success_message: str = "Routine Occurred"
    failure_message: str = "Routine did not occur!"


@dataclass(frozen=True)
class AlertaRoutineOccurrence:
    occurrence_id: str
    tenant_id: str
    routine_id: str
    scheduled_start_iso: str
    scheduled_end_iso: str
    outcome_state: AlertaRoutineOutcomeStateEnum
    occurred_at_iso: str | None = None


@dataclass(frozen=True)
class AlertaRoutineSuccessRateMetric:
    tenant_id: str
    routine_id: str
    period: AnalysisTimeframeEnum
    scheduled_count: int
    occurred_count: int
    missed_count: int
    success_rate: float


@dataclass(frozen=True)
class AlertaRoutineSuccessRateDataPoint:
    routine_id: str
    period_start_iso: str
    period_end_iso: str
    scheduled_count: int
    occurred_count: int
    missed_count: int
    success_rate: float


@dataclass(frozen=True)
class AlertaRoutineSuccessRateSeriesDTO:
    tenant_id: str
    routine_id: str
    period: AnalysisTimeframeEnum
    interval: AnalysisIntervalEnum
    values: tuple[AlertaRoutineSuccessRateDataPoint, ...]
