from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Inventory")


@attr.s(auto_attribs=True)
class Inventory:
    """Model representing the inventory of an item in one location.

    Attributes:
        thibert_part_number (Union[Unset, None, str]): Part number of the item associated with this inventory.
        quantity (Union[Unset, int]): The quantity in the location of this inventory.
        site_code (Union[Unset, None, str]): The site code of this inventory.
        is_primary_site (Union[Unset, bool]): Indicates if this is the main site for this account
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    site_code: Union[Unset, None, str] = UNSET
    is_primary_site: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        quantity = self.quantity
        site_code = self.site_code
        is_primary_site = self.is_primary_site

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if site_code is not UNSET:
            field_dict["siteCode"] = site_code
        if is_primary_site is not UNSET:
            field_dict["isPrimarySite"] = is_primary_site

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        quantity = d.pop("quantity", UNSET)

        site_code = d.pop("siteCode", UNSET)

        is_primary_site = d.pop("isPrimarySite", UNSET)

        inventory = cls(
            thibert_part_number=thibert_part_number,
            quantity=quantity,
            site_code=site_code,
            is_primary_site=is_primary_site,
        )

        return inventory
