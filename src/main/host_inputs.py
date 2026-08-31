# /src/main/host_inputs.py

"""
Living Well:
user_id="FlEl9LLqpBcFX7xyLcE8OYfTvZ73", tenant_id="b77891d5e60d40789698e8a9d4187fe9",

el perro:
user ID: 1hB6CrpvpgMzQ5KF6v0igsAROFa2; tenant ID: cbaac9b44af248b18f4833494f042c3b


"""

from dataclasses import dataclass

from src.domain.enums.access.role_enums import UserRoleEnum
from src.domain.enums.access.permission_enums import PermissionEnum
from src.domain.enums.access.resource_access_enums import ResourceScopeEnum

from src.application.context import (
    SessionContext,
    UserContext,
    AccessScope,
)


@dataclass(frozen=True, slots=True)
class HostInputs:
    bypass_authentication: bool
    session_context: SessionContext


def load_host_inputs() -> HostInputs:
    user_id = "1hB6CrpvpgMzQ5KF6v0igsAROFa2"
    tenant_id = "cbaac9b44af248b18f4833494f042c3b"

    return HostInputs(
        bypass_authentication=True,
        session_context=SessionContext(
            user_context=UserContext(
                user_id=user_id,
                tenant_id=tenant_id,
            ),
            access_scope=AccessScope(
                user_id=user_id,

                roles=frozenset({
                    UserRoleEnum.PLATFORM_ADMINISTRATOR,
                }),

                permissions=frozenset({
                    PermissionEnum.RESIDENT_VIEW,
                    PermissionEnum.RESIDENT_CREATE,
                    PermissionEnum.RESIDENT_UPDATE,
                    PermissionEnum.RESIDENT_ARCHIVE,
                    PermissionEnum.PRIORITY_ITEM_VIEW,
                    PermissionEnum.PRIORITY_ITEM_CREATE,
                    PermissionEnum.PRIORITY_ITEM_UPDATE,
                    PermissionEnum.PRIORITY_ITEM_RESOLVE,
                    PermissionEnum.ADL_VIEW,
                    PermissionEnum.ADL_CREATE,
                    PermissionEnum.ADL_UPDATE,
                    PermissionEnum.TREATMENT_PLAN_VIEW,
                    PermissionEnum.TREATMENT_PLAN_CREATE,
                    PermissionEnum.TREATMENT_PLAN_UPDATE,
                    PermissionEnum.RTM_VIEW,
                    PermissionEnum.RTM_MANAGE,
                    PermissionEnum.PROVIDER_VIEW,
                    PermissionEnum.PROVIDER_CREATE,
                    PermissionEnum.PROVIDER_UPDATE,
                    PermissionEnum.COMMUNICATION_VIEW,
                    PermissionEnum.COMMUNICATION_CREATE,
                    PermissionEnum.CLINICAL_DOCUMENT_VIEW,
                    PermissionEnum.CLINICAL_DOCUMENT_UPLOAD,
                    PermissionEnum.CLINICAL_DOCUMENT_DELETE,
                    PermissionEnum.BILLING_VIEW,
                    PermissionEnum.BILLING_CREATE,
                    PermissionEnum.BILLING_UPDATE,
                    PermissionEnum.SENSOR_PROFILE_VIEW,
                    PermissionEnum.SENSOR_PROFILE_CONFIGURE,
                    PermissionEnum.SENSOR_STATUS_VIEW,
                    PermissionEnum.SENSOR_EVENT_VIEW,
                    PermissionEnum.SENSOR_ANALYTICS_VIEW,
                    PermissionEnum.GATEWAY_VIEW,
                    PermissionEnum.GATEWAY_CONFIGURE,
                    PermissionEnum.USER_VIEW,
                    PermissionEnum.USER_CREATE,
                    PermissionEnum.USER_UPDATE,
                    PermissionEnum.ACCESS_VIEW,
                    PermissionEnum.ACCESS_MANAGE,
                    PermissionEnum.TENANT_VIEW,
                    PermissionEnum.TENANT_UPDATE,
                }),

                resident_scope=ResourceScopeEnum.PLATFORM,
                sensor_scope=ResourceScopeEnum.PLATFORM,
                gateway_scope=ResourceScopeEnum.PLATFORM,

                tenant_ids=frozenset(),
                resident_ids=frozenset(),
                sensor_ids=frozenset(),
                gateway_ids=frozenset(),
            ),
        ),
    )


def load_host_inputs_2() -> HostInputs:
    user_id = "FlEl9LLqpBcFX7xyLcE8OYfTvZ73"
    tenant_id = "b77891d5e60d40789698e8a9d4187fe9"

    return HostInputs(
        bypass_authentication=True,
        session_context=SessionContext(
            user_context=UserContext(
                user_id=user_id,
                tenant_id=tenant_id,
            ),
            access_scope=AccessScope(
                user_id=user_id,

                roles=frozenset({
                    UserRoleEnum.OWNER,
                }),

                permissions=frozenset({
                    PermissionEnum.RESIDENT_VIEW,
                    PermissionEnum.RESIDENT_CREATE,
                    PermissionEnum.RESIDENT_UPDATE,
                    PermissionEnum.RESIDENT_ARCHIVE,

                    PermissionEnum.PRIORITY_ITEM_VIEW,
                    PermissionEnum.PRIORITY_ITEM_CREATE,
                    PermissionEnum.PRIORITY_ITEM_UPDATE,
                    PermissionEnum.PRIORITY_ITEM_RESOLVE,

                    PermissionEnum.ADL_VIEW,
                    PermissionEnum.ADL_CREATE,
                    PermissionEnum.ADL_UPDATE,

                    PermissionEnum.PROVIDER_VIEW,
                    PermissionEnum.PROVIDER_CREATE,
                    PermissionEnum.PROVIDER_UPDATE,

                    PermissionEnum.COMMUNICATION_VIEW,
                    PermissionEnum.COMMUNICATION_CREATE,

                    PermissionEnum.CLINICAL_DOCUMENT_VIEW,
                    PermissionEnum.CLINICAL_DOCUMENT_UPLOAD,
                    PermissionEnum.CLINICAL_DOCUMENT_DELETE,

                    PermissionEnum.SENSOR_PROFILE_VIEW,
                    PermissionEnum.SENSOR_STATUS_VIEW,
                    PermissionEnum.SENSOR_EVENT_VIEW,
                    PermissionEnum.SENSOR_ANALYTICS_VIEW,

                    PermissionEnum.GATEWAY_VIEW,
                }),

                resident_scope=ResourceScopeEnum.TENANT,
                sensor_scope=ResourceScopeEnum.TENANT,
                gateway_scope=ResourceScopeEnum.TENANT,

                tenant_ids=frozenset({
                    tenant_id,
                }),

                resident_ids=frozenset(),
                sensor_ids=frozenset(),
                gateway_ids=frozenset(),
            ),
        ),
    )
