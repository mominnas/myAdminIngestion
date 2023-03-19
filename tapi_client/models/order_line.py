from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderLine")


@attr.s(auto_attribs=True)
class OrderLine:
    """Represents one part and quantity within an order.

    Attributes:
        thibert_part_number (Union[Unset, None, str]): Part number in the Thibert database.
        quantity (Union[Unset, int]): Quantity to ship.
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    quantity: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        quantity = d.pop("quantity", UNSET)

        order_line = cls(
            thibert_part_number=thibert_part_number,
            quantity=quantity,
        )

        return order_line
