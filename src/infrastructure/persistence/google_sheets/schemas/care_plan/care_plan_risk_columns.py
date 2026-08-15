# /src/infrastructure/persistence/schemas

class CarePlanRiskColumns:
    RISK_ID: str = "risk_id"
    CARE_PLAN_ID: str = "care_plan_id"
    RISK_TYPE: str = "risk_type"
    SEVERITY: str = "severity"
    DESCRIPTION: str = "description"
    MITIGATION_PLAN: str = "mitigation_plan"
    ACTIVE: str = "active"
    ORDER = (
RISK_ID,
CARE_PLAN_ID,
RISK_TYPE,
SEVERITY,
DESCRIPTION,
MITIGATION_PLAN,
ACTIVE,
)