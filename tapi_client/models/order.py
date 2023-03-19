from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.contact import Contact
    from ..models.order_line import OrderLine


T = TypeVar("T", bound="Order")


@attr.s(auto_attribs=True)
class Order:
    """Represents an order to be processed by Thibert. An account with Thibert is required.

    Attributes:
        order_reference_number (Union[Unset, None, str]): User inputed for personnal reference.
        shipping_address (Union[Unset, Address]): Represents a physical address.
        contact_info (Union[Unset, Contact]): Represents differents ways to contact an identity.
        order_lines (Union[Unset, None, List['OrderLine']]): Parts in the order.
    """

    order_reference_number: Union[Unset, None, str] = UNSET
    shipping_address: Union[Unset, "Address"] = UNSET
    contact_info: Union[Unset, "Contact"] = UNSET
    order_lines: Union[Unset, None, List["OrderLine"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        order_reference_number = self.order_reference_number
        shipping_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shipping_address, Unset):
            shipping_address = self.shipping_address.to_dict()

        contact_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact_info, Unset):
            contact_info = self.contact_info.to_dict()

        order_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_lines, Unset):
            if self.order_lines is None:
                order_lines = None
            else:
                order_lines = []
                for order_lines_item_data in self.order_lines:
                    order_lines_item = order_lines_item_data.to_dict()

                    order_lines.append(order_lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if order_reference_number is not UNSET:
            field_dict["orderReferenceNumber"] = order_reference_number
        if shipping_address is not UNSET:
            field_dict["shippingAddress"] = shipping_address
        if contact_info is not UNSET:
            field_dict["contactInfo"] = contact_info
        if order_lines is not UNSET:
            field_dict["orderLines"] = order_lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.contact import Contact
        from ..models.order_line import OrderLine

        d = src_dict.copy()
        order_reference_number = d.pop("orderReferenceNumber", UNSET)

        _shipping_address = d.pop("shippingAddress", UNSET)
        shipping_address: Union[Unset, Address]
        if isinstance(_shipping_address, Unset):
            shipping_address = UNSET
        else:
            shipping_address = Address.from_dict(_shipping_address)

        _contact_info = d.pop("contactInfo", UNSET)
        contact_info: Union[Unset, Contact]
        if isinstance(_contact_info, Unset):
            contact_info = UNSET
        else:
            contact_info = Contact.from_dict(_contact_info)

        order_lines = []
        _order_lines = d.pop("orderLines", UNSET)
        for order_lines_item_data in _order_lines or []:
            order_lines_item = OrderLine.from_dict(order_lines_item_data)

            order_lines.append(order_lines_item)

        order = cls(
            order_reference_number=order_reference_number,
            shipping_address=shipping_address,
            contact_info=contact_info,
            order_lines=order_lines,
        )

        return order
