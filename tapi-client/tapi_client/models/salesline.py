from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Salesline")


@attr.s(auto_attribs=True)
class Salesline:
    """
    Attributes:
        line_no (Union[Unset, int]):
        product_id (Union[Unset, None, str]):
        variant_id (Union[Unset, None, str]):
        product_title (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        quantity (Union[Unset, int]):
        price (Union[Unset, float]):
        tax_percent (Union[Unset, float]):
        inventory (Union[Unset, int]):
        line_amount (Union[Unset, float]):
        parent_line_no (Union[Unset, int]):
        is_read_only_line (Union[Unset, int]):
        line_type (Union[Unset, None, str]):
        unit_of_measure_id (Union[Unset, None, str]):
        unit_of_measure_description (Union[Unset, None, str]):
        shipment_date (Union[Unset, None, str]):
        quantity_shipped (Union[Unset, int]):
        quantity_invoiced (Union[Unset, int]):
        quantity_outstanding (Union[Unset, int]):
        service_charge_id (Union[Unset, None, str]):
    """

    line_no: Union[Unset, int] = UNSET
    product_id: Union[Unset, None, str] = UNSET
    variant_id: Union[Unset, None, str] = UNSET
    product_title: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    tax_percent: Union[Unset, float] = UNSET
    inventory: Union[Unset, int] = UNSET
    line_amount: Union[Unset, float] = UNSET
    parent_line_no: Union[Unset, int] = UNSET
    is_read_only_line: Union[Unset, int] = UNSET
    line_type: Union[Unset, None, str] = UNSET
    unit_of_measure_id: Union[Unset, None, str] = UNSET
    unit_of_measure_description: Union[Unset, None, str] = UNSET
    shipment_date: Union[Unset, None, str] = UNSET
    quantity_shipped: Union[Unset, int] = UNSET
    quantity_invoiced: Union[Unset, int] = UNSET
    quantity_outstanding: Union[Unset, int] = UNSET
    service_charge_id: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        line_no = self.line_no
        product_id = self.product_id
        variant_id = self.variant_id
        product_title = self.product_title
        title = self.title
        quantity = self.quantity
        price = self.price
        tax_percent = self.tax_percent
        inventory = self.inventory
        line_amount = self.line_amount
        parent_line_no = self.parent_line_no
        is_read_only_line = self.is_read_only_line
        line_type = self.line_type
        unit_of_measure_id = self.unit_of_measure_id
        unit_of_measure_description = self.unit_of_measure_description
        shipment_date = self.shipment_date
        quantity_shipped = self.quantity_shipped
        quantity_invoiced = self.quantity_invoiced
        quantity_outstanding = self.quantity_outstanding
        service_charge_id = self.service_charge_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if line_no is not UNSET:
            field_dict["lineNo"] = line_no
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if variant_id is not UNSET:
            field_dict["variantId"] = variant_id
        if product_title is not UNSET:
            field_dict["productTitle"] = product_title
        if title is not UNSET:
            field_dict["title"] = title
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if price is not UNSET:
            field_dict["price"] = price
        if tax_percent is not UNSET:
            field_dict["taxPercent"] = tax_percent
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if line_amount is not UNSET:
            field_dict["lineAmount"] = line_amount
        if parent_line_no is not UNSET:
            field_dict["parentLineNo"] = parent_line_no
        if is_read_only_line is not UNSET:
            field_dict["isReadOnlyLine"] = is_read_only_line
        if line_type is not UNSET:
            field_dict["lineType"] = line_type
        if unit_of_measure_id is not UNSET:
            field_dict["unitOfMeasureId"] = unit_of_measure_id
        if unit_of_measure_description is not UNSET:
            field_dict["unitOfMeasureDescription"] = unit_of_measure_description
        if shipment_date is not UNSET:
            field_dict["shipmentDate"] = shipment_date
        if quantity_shipped is not UNSET:
            field_dict["quantityShipped"] = quantity_shipped
        if quantity_invoiced is not UNSET:
            field_dict["quantityInvoiced"] = quantity_invoiced
        if quantity_outstanding is not UNSET:
            field_dict["quantityOutstanding"] = quantity_outstanding
        if service_charge_id is not UNSET:
            field_dict["serviceChargeId"] = service_charge_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line_no = d.pop("lineNo", UNSET)

        product_id = d.pop("productId", UNSET)

        variant_id = d.pop("variantId", UNSET)

        product_title = d.pop("productTitle", UNSET)

        title = d.pop("title", UNSET)

        quantity = d.pop("quantity", UNSET)

        price = d.pop("price", UNSET)

        tax_percent = d.pop("taxPercent", UNSET)

        inventory = d.pop("inventory", UNSET)

        line_amount = d.pop("lineAmount", UNSET)

        parent_line_no = d.pop("parentLineNo", UNSET)

        is_read_only_line = d.pop("isReadOnlyLine", UNSET)

        line_type = d.pop("lineType", UNSET)

        unit_of_measure_id = d.pop("unitOfMeasureId", UNSET)

        unit_of_measure_description = d.pop("unitOfMeasureDescription", UNSET)

        shipment_date = d.pop("shipmentDate", UNSET)

        quantity_shipped = d.pop("quantityShipped", UNSET)

        quantity_invoiced = d.pop("quantityInvoiced", UNSET)

        quantity_outstanding = d.pop("quantityOutstanding", UNSET)

        service_charge_id = d.pop("serviceChargeId", UNSET)

        salesline = cls(
            line_no=line_no,
            product_id=product_id,
            variant_id=variant_id,
            product_title=product_title,
            title=title,
            quantity=quantity,
            price=price,
            tax_percent=tax_percent,
            inventory=inventory,
            line_amount=line_amount,
            parent_line_no=parent_line_no,
            is_read_only_line=is_read_only_line,
            line_type=line_type,
            unit_of_measure_id=unit_of_measure_id,
            unit_of_measure_description=unit_of_measure_description,
            shipment_date=shipment_date,
            quantity_shipped=quantity_shipped,
            quantity_invoiced=quantity_invoiced,
            quantity_outstanding=quantity_outstanding,
            service_charge_id=service_charge_id,
        )

        return salesline
