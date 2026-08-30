# /src/domain/enums/access/resource_access_enums.py

from dataclasses import dataclass
from datetime import datetime

from src.domain.enums.access.resource_access_enums import AccessResourceTypeEnum


@dataclass(frozen=True)
class UserResourceAssignment:
    assignment_id: str
    user_id: str
    tenant_id: str
    resource_type: AccessResourceTypeEnum
    resource_id: str
    granted_by_user_id: str
    granted_at: datetime
    is_active: bool = True
