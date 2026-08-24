# /src/infrastructure/persistence/google_sheets/schemas/treatment/treatment_monitoring_parameter_columns.py

class TreatmentMonitoringParameterColumns:
    MONITORING_PARAMETER_ID: str = "monitoring_parameter_id"
    TREATMENT_PLAN_ID: str = "treatment_plan_id"
    GOAL_ID: str = "goal_id"
    MEASURE_DEFINITION_ID: str = "measure_definition_id"
    BASELINE_VALUE: str = "baseline_value"
    TARGET_VALUE: str = "target_value"
    UNIT: str = "unit"
    ORDER = (
        MONITORING_PARAMETER_ID,
        TREATMENT_PLAN_ID,
        GOAL_ID,
        MEASURE_DEFINITION_ID,
        BASELINE_VALUE,
        TARGET_VALUE,
        UNIT,
    )
