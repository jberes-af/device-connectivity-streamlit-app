# analytics_entities.py

from dataclasses import dataclass

from src.domain.enums.sensing.analytics_enums import *

"""
# this goes in application/use_case:

@dataclass(frozen=True)
class AnalysisRequestDTO:
    tenant_id: str
    subject_type: AnalysisSubjectTypeEnum
    subject_ids: tuple[str, ...]
    metric_type: AnalysisMetricTypeEnum
    timeframe: AnalysisTimeframeEnum
    comparison_target: AnalysisComparisonTargetEnum
    aggregation_method: AnalysisAggregationMethodEnum
    analysis_methods: tuple[AnalysisMethodEnum, ...]
    response_format: AnalysisResponseFormatEnum


@dataclass(frozen=True)
class AnalysisResponse:
    request: AnalysisRequestDTO
    count_metric: CountMetric | None = None
    comparison_metric: ComparisonMetric | None = None
    trend_metric: TrendMetric | None = None
    period_statistics: PeriodStatistics | None = None
    trend_series: TrendSeries | None = None
    insight: AnalysisInsight | None = None

"""


@dataclass(frozen=True)
class DataPoint:
    timestamp: str
    value: float


@dataclass(frozen=True)
class MetricTimePeriod:
    days: int
    period_start_date: str
    period_end_date: str


@dataclass(frozen=True)
class CountMetric:
    name: str
    subject: str
    period: MetricTimePeriod
    value: float


@dataclass(frozen=True)
class RollingAverageConfiguration:
    source_period_days: int
    rolling_window_days: int
    output_point_count: int


#### ANL-18: Regression Trend 


@dataclass(frozen=True)
class RegressionTrend:
    slope: float
    intercept: float
    r_squared: float | None
    direction: TrendDirectionEnum


@dataclass(frozen=True)
class TrendMetric:
    name: str
    subject: str
    source_period: MetricTimePeriod
    rolling_average_config: RollingAverageConfiguration
    raw_values: tuple[DataPoint, ...]
    smoothed_values: tuple[DataPoint, ...]
    regression: RegressionTrend


@dataclass(frozen=True)
class ComparisonMetric:
    name: str
    subject: str
    current_period: MetricTimePeriod
    comparison_period: MetricTimePeriod
    current_value: float
    comparison_value: float
    percent_change: float | None
    direction: TrendDirectionEnum


@dataclass(frozen=True)
class PeriodStatistics:
    subject: str
    period: MetricTimePeriod
    minimum: float
    maximum: float
    average: float
    total: int


@dataclass(frozen=True)
class TrendSeries:
    name: str
    subject: str
    window_days: MetricTimePeriod
    raw_values: tuple[DataPoint, ...]
    rolling_average_values: tuple[DataPoint, ...]


@dataclass(frozen=True)
class AnalysisBaseline:
    baseline_id: str
    tenant_id: str
    subject_type: AnalysisSubjectTypeEnum
    subject_id: str
    metric_type: AnalysisMetricTypeEnum
    baseline_period: MetricTimePeriod
    baseline_value: float
    source_record_count: int
    created_by_user_id: str
    created_at_iso: str
    name: str | None = None
    notes: str | None = None


@dataclass(frozen=True)
class AnalysisInsight:
    insight_id: str
    tenant_id: str
    subject_type: AnalysisSubjectTypeEnum
    subject_id: str
    metric_type: AnalysisMetricTypeEnum
    generated_at_iso: str
    title: str
    summary: str
    trend_direction: TrendDirectionEnum | None
    severity: str | None


@dataclass(frozen=True)
class AnalysisComparison:
    comparison_target: AnalysisComparisonTargetEnum
    comparison_period: MetricTimePeriod | None = None
    baseline_id: str | None = None
