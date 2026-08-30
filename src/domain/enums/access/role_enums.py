# /src/domain/enums/access/role_enums.py

from enum import StrEnum


class UserRoleEnum(StrEnum):
    OWNER = "owner"
    EXECUTIVE_DIRECTOR = "executive_director"
    CARE_MANAGER = "care_manager"
    CAREGIVER = "caregiver"
    CLINICIAN = "clinician"
    BILLING_SPECIALIST = "billing_specialist"
    ADMINISTRATIVE_STAFF = "administrative_staff"
    DEVICE_TECHNICIAN = "device_technician"
    TENANT_ADMINISTRATOR = "tenant_administrator"
    PLATFORM_ADMINISTRATOR = "platform_administrator"
