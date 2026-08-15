# /src/domain/enums/sensing/analytics_enums.py

from enum import StrEnum


class AnalysisIntervalEnum(StrEnum):
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"


class AnalysisSubjectTypeEnum(StrEnum):
    SENSOR = "Sensor"
    SENSOR_GROUP = "Sensor Group"
    RESIDENT = "Resident"
    ADL_CATEGORY = "Adl Category"
    ALERTA_ROUTINE = "Alerta Routine"


class AnalysisMetricTypeEnum(StrEnum):
    SENSOR_NOTIFICATION_COUNT = "Sensor Notification Count"
    SENSOR_EVENT_COUNT = "Sensor Event Count"
    MOVEMENT_COUNT = "Movement Count"
    ADL_SCORE = "Adl Score"
    ROUTINE_SUCCESS_RATE = "Routine Success Rate"


class AnalysisTimeframeEnum(StrEnum):
    TODAY = "Today"
    YESTERDAY = "Yesterday"
    NIGHTTIME = "Nighttime"
    LAST_7_DAYS = "Last 7 Days"
    LAST_14_DAYS = "Last 14 Days"
    LAST_30_DAYS = "Last 30 Days"
    LAST_60_DAYS = "Last 60 Days"
    CUSTOM = "Custom"


class AnalysisComparisonTargetEnum(StrEnum):
    PREVIOUS_DAY = "Previous Day"
    BASELINE = "Baseline"
    SEVEN_DAY_AVERAGE = "Seven Day Average"
    FOURTEEN_DAY_AVERAGE = "Fourteen Day Average"
    THIRTY_DAY_AVERAGE = "Thirty Day Average"
    SIXTY_DAY_AVERAGE = "Sixty Day Average"
    PRIOR_PERIOD = "Prior Period"
    NONE = "None"


class AnalysisAggregationMethodEnum(StrEnum):
    COUNT = "Count"
    SUM = "Sum"
    AVERAGE = "Average"
    PERCENTAGE = "Percentage"
    RATE = "Rate"


class AnalysisMethodEnum(StrEnum):
    PERCENT_CHANGE = "Percent Change"
    REGRESSION_TREND = "Regression Trend"
    ROLLING_AVERAGE = "Rolling Average"
    RAW_SERIES = "Raw Series"


class TrendDirectionEnum(StrEnum):
    UP = "Up"
    DOWN = "Down"
    STABLE = "Stable"
    CANNOT_ASSESS = "Cannot Assess"


class AnalysisResponseFormatEnum(StrEnum):
    DESCRIPTIVE_TEXT = "Descriptive Text"
    TIME_SERIES = "Time Series"
    DESCRIPTIVE_TEXT_WITH_SPARKLINE = "Descriptive Text With Sparkline"
