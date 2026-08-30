# /src/domain/enums/access/resource_access_enums.py

from enum import StrEnum


class AccessResourceTypeEnum(StrEnum):
    TENANT = "tenant"
    USER = "user"
    RESIDENT = "resident"
    SENSOR = "sensor"
    GATEWAY = "gateway"


class ResourceScopeEnum(StrEnum):
    ASSIGNED = "assigned"
    TENANT = "tenant"
    PLATFORM = "platform"
