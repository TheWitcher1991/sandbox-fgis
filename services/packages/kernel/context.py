from dataclasses import dataclass
from typing import Optional

from organizations.models import Organization
from roles.types import RoleType
from users.models import Member, User
from users.types import MemberRole


@dataclass(frozen=True)
class RequestContext:
    user: User
    member: Optional[Member]
    organization: Optional[Organization]

    member_role: Optional[MemberRole]
    organization_role: Optional[RoleType]
