from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    """Represents a physical address.

    Attributes:
        name (Union[Unset, None, str]): Name asssociated to the address.
        address1 (Union[Unset, None, str]): Number and street name combination.
        address2 (Union[Unset, None, str]): Alternative number and street name combination.
        zip_code (Union[Unset, None, str]): AKA Postal code
        city (Union[Unset, None, str]): Town associated with the address.
        state (Union[Unset, None, str]): State or province depending on the country.
        country_code (Union[Unset, None, str]): CA or USA
    """

    name: Union[Unset, None, str] = UNSET
    address1: Union[Unset, None, str] = UNSET
    address2: Union[Unset, None, str] = UNSET
    zip_code: Union[Unset, None, str] = UNSET
    city: Union[Unset, None, str] = UNSET
    state: Union[Unset, None, str] = UNSET
    country_code: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        address1 = self.address1
        address2 = self.address2
        zip_code = self.zip_code
        city = self.city
        state = self.state
        country_code = self.country_code

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        address1 = d.pop("address1", UNSET)

        address2 = d.pop("address2", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country_code = d.pop("countryCode", UNSET)

        address = cls(
            name=name,
            address1=address1,
            address2=address2,
            zip_code=zip_code,
            city=city,
            state=state,
            country_code=country_code,
        )

        return address
