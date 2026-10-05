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
    TREATMENT_REVIEW_VIEW = "treatment_review.view"
    TREATMENT_REVIEW_CREATE = "treatment_review.create"

    # RTM / CLINICAL
    RTM_VIEW = "rtm.view"
    RTM_MANAGE = "rtm.manage"
    RTM_TIME_ENTRY_CORRECT_OWN = "rtm_time_entry.correct_own"
    RTM_TIME_ENTRY_CREATE_SELF = "rtm_time_entry.create_self"
    RTM_TIME_ENTRY_VIEW = "rtm_time_entry.view"
    RTM_TIME_ENTRY_VOID_OWN = "rtm_time_entry.void_own"

    # PROVIDER
    PROVIDER_VIEW = "provider.view"
    PROVIDER_CREATE = "provider.create"
    PROVIDER_UPDATE = "provider.update"

    # COMMUNICATION
    COMMUNICATION_VIEW = "communication.view"
    COMMUNICATION_CREATE = "communication.create"
    COMMUNICATION_CORRECT_OWN = "communication.correct_own"
    COMMUNICATION_PARTICIPANT_MANAGE = "communication.participant_manage"
    COMMUNICATION_REVIEWED_ITEM_LINK = "communication.reviewed_item_link"
    COMMUNICATION_VOID_OWN = "communication.void_own"

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

    APPLICATION_USER_STATUS_VIEW = "application_user_status.view"
    APPLICATION_USER_STATUS_MANAGE = "application_user_status.manage"
    IDENTITY_LINK_VIEW = "identity_link.view"
    IDENTITY_LINK_INITIATE = "identity_link.initiate"
    IDENTITY_LINK_REVOKE = "identity_link.revoke"
    IDENTITY_LINK_VERIFY = "identity_link.verify"

    # TENANT
    TENANT_VIEW = "tenant.view"
    TENANT_UPDATE = "tenant.update"
    TENANT_CREATE = "tenant.create"
