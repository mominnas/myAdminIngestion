from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderTracking")


@attr.s(auto_attribs=True)
class OrderTracking:
    """
    Attributes:
        thibert_order_number (Union[Unset, None, str]):
        web_order_reference (Union[Unset, None, str]):
        tracking_number (Union[Unset, None, str]):
        tracking_url (Union[Unset, None, str]):
        carrier (Union[Unset, None, str]):
        thibert_part_number (Union[Unset, None, str]):
        shiped_quantity (Union[Unset, int]):
    """

    thibert_order_number: Union[Unset, None, str] = UNSET
    web_order_reference: Union[Unset, None, str] = UNSET
    tracking_number: Union[Unset, None, str] = UNSET
    tracking_url: Union[Unset, None, str] = UNSET
    carrier: Union[Unset, None, str] = UNSET
    thibert_part_number: Union[Unset, None, str] = UNSET
    shiped_quantity: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_order_number = self.thibert_order_number
        web_order_reference = self.web_order_reference
        tracking_number = self.tracking_number
        tracking_url = self.tracking_url
        carrier = self.carrier
        thibert_part_number = self.thibert_part_number
        shiped_quantity = self.shiped_quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_order_number is not UNSET:
            field_dict["thibertOrderNumber"] = thibert_order_number
        if web_order_reference is not UNSET:
            field_dict["webOrderReference"] = web_order_reference
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if tracking_url is not UNSET:
            field_dict["trackingURL"] = tracking_url
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if shiped_quantity is not UNSET:
            field_dict["shipedQuantity"] = shiped_quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        thibert_order_number = d.pop("thibertOrderNumber", UNSET)

        web_order_reference = d.pop("webOrderReference", UNSET)

        tracking_number = d.pop("trackingNumber", UNSET)

        tracking_url = d.pop("trackingURL", UNSET)

        carrier = d.pop("carrier", UNSET)

        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        shiped_quantity = d.pop("shipedQuantity", UNSET)

        order_tracking = cls(
            thibert_order_number=thibert_order_number,
            web_order_reference=web_order_reference,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            carrier=carrier,
            thibert_part_number=thibert_part_number,
            shiped_quantity=shiped_quantity,
        )

        return order_tracking
