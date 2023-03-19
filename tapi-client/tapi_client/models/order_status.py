from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderStatus")


@attr.s(auto_attribs=True)
class OrderStatus:
    """Represents an order to be processed by Thibert. An account with Thibert is required.

    Attributes:
        thibert_order_number (Union[Unset, None, str]): Indicates the Thibert Order Number
        order_reference_number (Union[Unset, None, str]): Client order number reference.
        status (Union[Unset, None, str]): Indicates the Thibert status of the order
    """

    thibert_order_number: Union[Unset, None, str] = UNSET
    order_reference_number: Union[Unset, None, str] = UNSET
    status: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_order_number = self.thibert_order_number
        order_reference_number = self.order_reference_number
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_order_number is not UNSET:
            field_dict["thibertOrderNumber"] = thibert_order_number
        if order_reference_number is not UNSET:
            field_dict["orderReferenceNumber"] = order_reference_number
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        thibert_order_number = d.pop("thibertOrderNumber", UNSET)

        order_reference_number = d.pop("orderReferenceNumber", UNSET)

        status = d.pop("status", UNSET)

        order_status = cls(
            thibert_order_number=thibert_order_number,
            order_reference_number=order_reference_number,
            status=status,
        )

        return order_status
