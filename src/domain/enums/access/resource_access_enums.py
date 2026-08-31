# /src/domain/enums/access/resource_access_enums.py

from enum import StrEnum


class AccessResourceTypeEnum(StrEnum):
    TENANT = "tenant"
    USER = "user"
    RESIDENT = "resident"
    SENSOR = "sensor"
    GATEWAY = "gateway"


class ResourceScopeEnum(StrEnum):
    ASSIGNED = "assigned"  # by resource ID only
    TENANT = "tenant"  # all resources or specific resources for a tenant ID
    PLATFORM = "platform"  # all resources for all tenants


"""
#### 1. For resident resources, user_001 can access only residents specifically assigned to them.
The actual residents would then be in your existing user_resource_assignment table:

`user_001 | tenant_01 | resident | assigned`

user_id  | tenant_id | resource_type | resource_id
---------|-----------|---------------|------------
user_001 | tenant_01 | resident      | resident_101
user_001 | tenant_01 | resident      | resident_102


#### 2. User_002 can access all residents belonging to tenant_01.

Therefore, you do not need individual resident rows in user_resource_assignment for that user.

`user_002 | tenant_01 | resident | tenant`


#### 3. The user's resident access can extend across tenants.
`admin_01 | tenant_01 | resident | platform`

-----

ASSIGNED
    ids populated
    tenant_ids populated as applicable

TENANT
    resource ids empty
    tenant_ids contains allowed tenant(s)

PLATFORM
    resource ids empty
    tenant_ids empty

"""
