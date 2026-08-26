# /src/domain/entities/contact/tenant_enums.py

from enum import StrEnum


class TenantTypeEnum(StrEnum):
    SINGLE_FAMILY_HOME = "Single Family Home"
    RESIDENTIAL_CARE_HOME = "Residential Care Home"
    ASSISTED_LIVING_FACILITY = "Assisted Living Facility"
    SKILLED_NURSING_FACILITY = "Skilled Nursing Facility"
    RETIREMENT_COMMUNITY = "Retirement Community"
    INDEPENDENT_LIVING_COMMUNITY = "Independent Living Community"
    THERAPY_CLINIC = "Therapy Clinic"
    RESEARCH_FACILITY = "Research Facility"
    HOSPITAL = "Hospital"
    MEMORY_CARE_FACILITY = "Memory Care Facility"
    DAY_CARE_FACILITY = "Day Care Facility"
    OTHER = "Other"


class PermissionEnum(StrEnum):
    CREATE_NOTES = "Create Notes"
    CONFIGURE_RESIDENT = "Configure Resident"
    MANAGE_PRIORITY_ITEMS = "Manage Priority Items"
    CONFIGURE_SENSOR = "Configure Sensor"
    VIEW_ANALYTICS = "View Analytics"
    VIEW_NOTES = "View Notes"
    VIEW_PRIORITY_ITEMS = "View Priority Items"
    VIEW_RESIDENT = "View Resident"
    VIEW_SENSORS = "View Sensors"
    VIEW_SENSOR_EVENTS = "View Sensor Events"
    VIEW_THERAPEUTIC_PLANS = "View Therapeutic Plans"
    MANAGE_THERAPEUTIC_PLANS = "Manage Therapeutic Plans"
    MANAGE_ADLS = "Manage Adls"
    VIEW_ADLS = "View Adls"



class UserRoleEnum(StrEnum):
    ADMINISTRATOR = "Administrator"
    CARE_MANAGER = "Care Manager"
    CAREGIVER = "Caregiver"
    CLINICIAN = "Clinician"
    EXECUTIVE_DIRECTOR = "Executive Director"
    OWNER = "Owner"
    TECHNICIAN = "Technician"
    VIEWER = "Viewer"