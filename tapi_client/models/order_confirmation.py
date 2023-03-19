import datetime
from typing import Any, Dict, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderConfirmation")


@attr.s(auto_attribs=True)
class OrderConfirmation:
    """Represents what is returned once an order has been confirmed.

    Attributes:
        order_number (Union[Unset, None, str]): Internal identifier for the order. Example: CO0009999.
        creation_date (Union[Unset, datetime.datetime]): Date when the order was processed. Example:
            2020-12-02T14:50:24.960372-05:00.
    """

    order_number: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_number = self.order_number
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_number is not UNSET:
            field_dict["orderNumber"] = order_number
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_number = d.pop("orderNumber", UNSET)

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        order_confirmation = cls(
            order_number=order_number,
            creation_date=creation_date,
        )

        return order_confirmation
