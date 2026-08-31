# /src/domain/enums/access/permission_enums.py

# capability oriented

from enum import StrEnum


class PermissionEnum(StrEnum):
    # RESIDENT
    RESIDENT_VIEW = "resident.view"
    RESIDENT_CREATE = "resident.create"
    RESIDENT_UPDATE = "resident.update"
    RESIDENT_ARCHIVE = "resident.archive"

    # PRIORITY ITEMS
    PRIORITY_ITEM_VIEW = "priority_item.view"
    PRIORITY_ITEM_CREATE = "priority_item.create"
    PRIORITY_ITEM_UPDATE = "priority_item.update"
    PRIORITY_ITEM_RESOLVE = "priority_item.resolve"

    # ADL
    ADL_VIEW = "adl.view"
    ADL_CREATE = "adl.create"
    ADL_UPDATE = "adl.update"

    # TREATMENT
    TREATMENT_PLAN_VIEW = "treatment_plan.view"
    TREATMENT_PLAN_CREATE = "treatment_plan.create"
    TREATMENT_PLAN_UPDATE = "treatment_plan.update"

    # RTM / CLINICAL
    RTM_VIEW = "rtm.view"
    RTM_MANAGE = "rtm.manage"

    # PROVIDER
    PROVIDER_VIEW = "provider.view"
    PROVIDER_CREATE = "provider.create"
    PROVIDER_UPDATE = "provider.update"

    # COMMUNICATION
    COMMUNICATION_VIEW = "communication.view"
    COMMUNICATION_CREATE = "communication.create"

    # CLINICAL DOCUMENTS
    CLINICAL_DOCUMENT_VIEW = "clinical_document.view"
    CLINICAL_DOCUMENT_UPLOAD = "clinical_document.upload"
    CLINICAL_DOCUMENT_DELETE = "clinical_document.delete"

    # BILLING
    BILLING_VIEW = "billing.view"
    BILLING_CREATE = "billing.create"
    BILLING_UPDATE = "billing.update"

    # SENSOR ADMINISTRATION
    SENSOR_PROFILE_VIEW = "sensor_profile.view"
    SENSOR_PROFILE_CONFIGURE = "sensor_profile.configure"

    # SENSOR STATUS / HEALTH
    SENSOR_STATUS_VIEW = "sensor_status.view"

    # SENSOR EVENTS
    SENSOR_EVENT_VIEW = "sensor_event.view"

    # SENSOR ANALYTICS
    SENSOR_ANALYTICS_VIEW = "sensor_analytics.view"

    # GATEWAYS
    GATEWAY_VIEW = "gateway.view"
    GATEWAY_CONFIGURE = "gateway.configure"

    # USERS
    USER_VIEW = "user.view"
    USER_CREATE = "user.create"
    USER_UPDATE = "user.update"

    # ACCESS CONTROL
    ACCESS_VIEW = "access.view"
    ACCESS_MANAGE = "access.manage"

    # TENANT
    TENANT_VIEW = "tenant.view"
    TENANT_UPDATE = "tenant.update"

