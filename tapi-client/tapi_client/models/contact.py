from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Contact")


@attr.s(auto_attribs=True)
class Contact:
    """Represents differents ways to contact an identity.

    Attributes:
        name (str):
        phone_number (str):
        email (Union[Unset, None, str]):
    """

    name: str
    phone_number: str
    email: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        phone_number = self.phone_number
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "phoneNumber": phone_number,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        phone_number = d.pop("phoneNumber")

        email = d.pop("email", UNSET)

        contact = cls(
            name=name,
            phone_number=phone_number,
            email=email,
        )

        return contact
