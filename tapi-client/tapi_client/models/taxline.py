from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Taxline")


@attr.s(auto_attribs=True)
class Taxline:
    """
    Attributes:
        tax_id (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        percentage (Union[Unset, float]):
        amount (Union[Unset, float]):
    """

    tax_id: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    percentage: Union[Unset, float] = UNSET
    amount: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tax_id = self.tax_id
        description = self.description
        percentage = self.percentage
        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if tax_id is not UNSET:
            field_dict["taxId"] = tax_id
        if description is not UNSET:
            field_dict["description"] = description
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tax_id = d.pop("taxId", UNSET)

        description = d.pop("description", UNSET)

        percentage = d.pop("percentage", UNSET)

        amount = d.pop("amount", UNSET)

        taxline = cls(
            tax_id=tax_id,
            description=description,
            percentage=percentage,
            amount=amount,
        )

        return taxline
