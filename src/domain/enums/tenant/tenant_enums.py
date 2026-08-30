# tenant_enums.py
from enum import StrEnum


class TenantTypeEnum(StrEnum):
    SINGLE_FAMILY_HOME = "Single Family Home"
    RESIDENTIAL_CARE_HOME = "Residential Care Home"
    ASSISTED_LIVING_FACILITY = "Assisted Living Facility"
    SKILLED_NURSING_FACILITY = "Skilled Nursing Facility"
    RETIREMENT_COMMUNITY = "Retirement Community"
    INDEPENDENT_LIVING_COMMUNITY = "Independent Living Community"
    HEALTHCARE_CLINIC = "Healthcare Clinic"
    THERAPY_CLINIC = "Therapy Clinic"
    RESEARCH_FACILITY = "Research Facility"
    HOSPITAL = "Hospital"
    MEMORY_CARE_FACILITY = "Memory Care Facility"
    DAY_CARE_FACILITY = "Day Care Facility"
    OTHER = "Other"
