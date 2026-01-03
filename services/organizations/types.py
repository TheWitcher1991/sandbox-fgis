from dataclasses import dataclass
from typing import NewType, Optional, TypedDict

from services.roles.types import RoleId

OrganizationId = NewType("OrganizationId", int)


class UpdateOrganizationData(TypedDict):
    pass


@dataclass(frozen=True)
class CreateOrganizationDTO:
    name: str
    inn: str
    email: str
    phone: str
    first_name: str
    last_name: str
    surname: Optional[str]
    position: str
    password: str
    role: RoleId


class CreateOrganizationData(TypedDict):
    name: str
    inn: str
    email: str
    phone: str
    first_name: str
    last_name: str
    surname: Optional[str]
    position: str
    password: str
    role: RoleId
