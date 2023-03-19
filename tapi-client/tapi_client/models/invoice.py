from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.salesline import Salesline
    from ..models.taxline import Taxline


T = TypeVar("T", bound="Invoice")


@attr.s(auto_attribs=True)
class Invoice:
    """
    Attributes:
        document_id (Union[Unset, None, str]):
        document_type (Union[Unset, None, str]):
        original_order_id (Union[Unset, None, str]):
        currency_id (Union[Unset, None, str]):
        prices_incl_tax (Union[Unset, float]):
        status (Union[Unset, None, str]):
        sales_person_id (Union[Unset, None, str]):
        sales_person_name (Union[Unset, None, str]):
        contact_id (Union[Unset, None, str]):
        contact_name (Union[Unset, None, str]):
        tax_percent (Union[Unset, float]):
        tax_amount (Union[Unset, float]):
        invoice_discount (Union[Unset, float]):
        subtotal (Union[Unset, float]):
        total_excl_tax (Union[Unset, float]):
        total_incl_tax (Union[Unset, float]):
        order_date (Union[Unset, None, str]):
        posting_date (Union[Unset, None, str]):
        document_date (Union[Unset, None, str]):
        due_date (Union[Unset, None, str]):
        shipment_date (Union[Unset, None, str]):
        payment_terms_code (Union[Unset, None, str]):
        payment_method_name (Union[Unset, None, str]):
        payment_status (Union[Unset, None, str]):
        payment_transaction_id (Union[Unset, None, str]):
        location_code (Union[Unset, None, str]):
        shipping_method_code (Union[Unset, None, str]):
        customer_id (Union[Unset, None, str]):
        reference_no (Union[Unset, None, str]):
        shop_account_email (Union[Unset, None, str]):
        outstanding_amount (Union[Unset, float]):
        shipping_method_name (Union[Unset, None, str]):
        order_lines_count (Union[Unset, int]):
        sell_to_address (Union[Unset, Address]): Represents a physical address.
        bill_to_address (Union[Unset, Address]): Represents a physical address.
        ship_to_address (Union[Unset, Address]): Represents a physical address.
        sales_lines (Union[Unset, None, List['Salesline']]):
        tax_lines (Union[Unset, None, List['Taxline']]):
    """

    document_id: Union[Unset, None, str] = UNSET
    document_type: Union[Unset, None, str] = UNSET
    original_order_id: Union[Unset, None, str] = UNSET
    currency_id: Union[Unset, None, str] = UNSET
    prices_incl_tax: Union[Unset, float] = UNSET
    status: Union[Unset, None, str] = UNSET
    sales_person_id: Union[Unset, None, str] = UNSET
    sales_person_name: Union[Unset, None, str] = UNSET
    contact_id: Union[Unset, None, str] = UNSET
    contact_name: Union[Unset, None, str] = UNSET
    tax_percent: Union[Unset, float] = UNSET
    tax_amount: Union[Unset, float] = UNSET
    invoice_discount: Union[Unset, float] = UNSET
    subtotal: Union[Unset, float] = UNSET
    total_excl_tax: Union[Unset, float] = UNSET
    total_incl_tax: Union[Unset, float] = UNSET
    order_date: Union[Unset, None, str] = UNSET
    posting_date: Union[Unset, None, str] = UNSET
    document_date: Union[Unset, None, str] = UNSET
    due_date: Union[Unset, None, str] = UNSET
    shipment_date: Union[Unset, None, str] = UNSET
    payment_terms_code: Union[Unset, None, str] = UNSET
    payment_method_name: Union[Unset, None, str] = UNSET
    payment_status: Union[Unset, None, str] = UNSET
    payment_transaction_id: Union[Unset, None, str] = UNSET
    location_code: Union[Unset, None, str] = UNSET
    shipping_method_code: Union[Unset, None, str] = UNSET
    customer_id: Union[Unset, None, str] = UNSET
    reference_no: Union[Unset, None, str] = UNSET
    shop_account_email: Union[Unset, None, str] = UNSET
    outstanding_amount: Union[Unset, float] = UNSET
    shipping_method_name: Union[Unset, None, str] = UNSET
    order_lines_count: Union[Unset, int] = UNSET
    sell_to_address: Union[Unset, "Address"] = UNSET
    bill_to_address: Union[Unset, "Address"] = UNSET
    ship_to_address: Union[Unset, "Address"] = UNSET
    sales_lines: Union[Unset, None, List["Salesline"]] = UNSET
    tax_lines: Union[Unset, None, List["Taxline"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        document_id = self.document_id
        document_type = self.document_type
        original_order_id = self.original_order_id
        currency_id = self.currency_id
        prices_incl_tax = self.prices_incl_tax
        status = self.status
        sales_person_id = self.sales_person_id
        sales_person_name = self.sales_person_name
        contact_id = self.contact_id
        contact_name = self.contact_name
        tax_percent = self.tax_percent
        tax_amount = self.tax_amount
        invoice_discount = self.invoice_discount
        subtotal = self.subtotal
        total_excl_tax = self.total_excl_tax
        total_incl_tax = self.total_incl_tax
        order_date = self.order_date
        posting_date = self.posting_date
        document_date = self.document_date
        due_date = self.due_date
        shipment_date = self.shipment_date
        payment_terms_code = self.payment_terms_code
        payment_method_name = self.payment_method_name
        payment_status = self.payment_status
        payment_transaction_id = self.payment_transaction_id
        location_code = self.location_code
        shipping_method_code = self.shipping_method_code
        customer_id = self.customer_id
        reference_no = self.reference_no
        shop_account_email = self.shop_account_email
        outstanding_amount = self.outstanding_amount
        shipping_method_name = self.shipping_method_name
        order_lines_count = self.order_lines_count
        sell_to_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sell_to_address, Unset):
            sell_to_address = self.sell_to_address.to_dict()

        bill_to_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bill_to_address, Unset):
            bill_to_address = self.bill_to_address.to_dict()

        ship_to_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ship_to_address, Unset):
            ship_to_address = self.ship_to_address.to_dict()

        sales_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sales_lines, Unset):
            if self.sales_lines is None:
                sales_lines = None
            else:
                sales_lines = []
                for sales_lines_item_data in self.sales_lines:
                    sales_lines_item = sales_lines_item_data.to_dict()

                    sales_lines.append(sales_lines_item)

        tax_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tax_lines, Unset):
            if self.tax_lines is None:
                tax_lines = None
            else:
                tax_lines = []
                for tax_lines_item_data in self.tax_lines:
                    tax_lines_item = tax_lines_item_data.to_dict()

                    tax_lines.append(tax_lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if document_id is not UNSET:
            field_dict["documentId"] = document_id
        if document_type is not UNSET:
            field_dict["documentType"] = document_type
        if original_order_id is not UNSET:
            field_dict["originalOrderId"] = original_order_id
        if currency_id is not UNSET:
            field_dict["currencyId"] = currency_id
        if prices_incl_tax is not UNSET:
            field_dict["pricesInclTax"] = prices_incl_tax
        if status is not UNSET:
            field_dict["status"] = status
        if sales_person_id is not UNSET:
            field_dict["salesPersonId"] = sales_person_id
        if sales_person_name is not UNSET:
            field_dict["salesPersonName"] = sales_person_name
        if contact_id is not UNSET:
            field_dict["contactId"] = contact_id
        if contact_name is not UNSET:
            field_dict["contactName"] = contact_name
        if tax_percent is not UNSET:
            field_dict["taxPercent"] = tax_percent
        if tax_amount is not UNSET:
            field_dict["taxAmount"] = tax_amount
        if invoice_discount is not UNSET:
            field_dict["invoiceDiscount"] = invoice_discount
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if total_excl_tax is not UNSET:
            field_dict["totalExclTax"] = total_excl_tax
        if total_incl_tax is not UNSET:
            field_dict["totalInclTax"] = total_incl_tax
        if order_date is not UNSET:
            field_dict["orderDate"] = order_date
        if posting_date is not UNSET:
            field_dict["postingDate"] = posting_date
        if document_date is not UNSET:
            field_dict["documentDate"] = document_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if shipment_date is not UNSET:
            field_dict["shipmentDate"] = shipment_date
        if payment_terms_code is not UNSET:
            field_dict["paymentTermsCode"] = payment_terms_code
        if payment_method_name is not UNSET:
            field_dict["paymentMethodName"] = payment_method_name
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status
        if payment_transaction_id is not UNSET:
            field_dict["paymentTransactionId"] = payment_transaction_id
        if location_code is not UNSET:
            field_dict["locationCode"] = location_code
        if shipping_method_code is not UNSET:
            field_dict["shippingMethodCode"] = shipping_method_code
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if reference_no is not UNSET:
            field_dict["referenceNo"] = reference_no
        if shop_account_email is not UNSET:
            field_dict["shopAccountEmail"] = shop_account_email
        if outstanding_amount is not UNSET:
            field_dict["outstandingAmount"] = outstanding_amount
        if shipping_method_name is not UNSET:
            field_dict["shippingMethodName"] = shipping_method_name
        if order_lines_count is not UNSET:
            field_dict["orderLinesCount"] = order_lines_count
        if sell_to_address is not UNSET:
            field_dict["sellToAddress"] = sell_to_address
        if bill_to_address is not UNSET:
            field_dict["billToAddress"] = bill_to_address
        if ship_to_address is not UNSET:
            field_dict["shipToAddress"] = ship_to_address
        if sales_lines is not UNSET:
            field_dict["salesLines"] = sales_lines
        if tax_lines is not UNSET:
            field_dict["taxLines"] = tax_lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.salesline import Salesline
        from ..models.taxline import Taxline

        d = src_dict.copy()
        document_id = d.pop("documentId", UNSET)

        document_type = d.pop("documentType", UNSET)

        original_order_id = d.pop("originalOrderId", UNSET)

        currency_id = d.pop("currencyId", UNSET)

        prices_incl_tax = d.pop("pricesInclTax", UNSET)

        status = d.pop("status", UNSET)

        sales_person_id = d.pop("salesPersonId", UNSET)

        sales_person_name = d.pop("salesPersonName", UNSET)

        contact_id = d.pop("contactId", UNSET)

        contact_name = d.pop("contactName", UNSET)

        tax_percent = d.pop("taxPercent", UNSET)

        tax_amount = d.pop("taxAmount", UNSET)

        invoice_discount = d.pop("invoiceDiscount", UNSET)

        subtotal = d.pop("subtotal", UNSET)

        total_excl_tax = d.pop("totalExclTax", UNSET)

        total_incl_tax = d.pop("totalInclTax", UNSET)

        order_date = d.pop("orderDate", UNSET)

        posting_date = d.pop("postingDate", UNSET)

        document_date = d.pop("documentDate", UNSET)

        due_date = d.pop("dueDate", UNSET)

        shipment_date = d.pop("shipmentDate", UNSET)

        payment_terms_code = d.pop("paymentTermsCode", UNSET)

        payment_method_name = d.pop("paymentMethodName", UNSET)

        payment_status = d.pop("paymentStatus", UNSET)

        payment_transaction_id = d.pop("paymentTransactionId", UNSET)

        location_code = d.pop("locationCode", UNSET)

        shipping_method_code = d.pop("shippingMethodCode", UNSET)

        customer_id = d.pop("customerId", UNSET)

        reference_no = d.pop("referenceNo", UNSET)

        shop_account_email = d.pop("shopAccountEmail", UNSET)

        outstanding_amount = d.pop("outstandingAmount", UNSET)

        shipping_method_name = d.pop("shippingMethodName", UNSET)

        order_lines_count = d.pop("orderLinesCount", UNSET)

        _sell_to_address = d.pop("sellToAddress", UNSET)
        sell_to_address: Union[Unset, Address]
        if isinstance(_sell_to_address, Unset):
            sell_to_address = UNSET
        else:
            sell_to_address = Address.from_dict(_sell_to_address)

        _bill_to_address = d.pop("billToAddress", UNSET)
        bill_to_address: Union[Unset, Address]
        if isinstance(_bill_to_address, Unset):
            bill_to_address = UNSET
        else:
            bill_to_address = Address.from_dict(_bill_to_address)

        _ship_to_address = d.pop("shipToAddress", UNSET)
        ship_to_address: Union[Unset, Address]
        if isinstance(_ship_to_address, Unset):
            ship_to_address = UNSET
        else:
            ship_to_address = Address.from_dict(_ship_to_address)

        sales_lines = []
        _sales_lines = d.pop("salesLines", UNSET)
        for sales_lines_item_data in _sales_lines or []:
            sales_lines_item = Salesline.from_dict(sales_lines_item_data)

            sales_lines.append(sales_lines_item)

        tax_lines = []
        _tax_lines = d.pop("taxLines", UNSET)
        for tax_lines_item_data in _tax_lines or []:
            tax_lines_item = Taxline.from_dict(tax_lines_item_data)

            tax_lines.append(tax_lines_item)

        invoice = cls(
            document_id=document_id,
            document_type=document_type,
            original_order_id=original_order_id,
            currency_id=currency_id,
            prices_incl_tax=prices_incl_tax,
            status=status,
            sales_person_id=sales_person_id,
            sales_person_name=sales_person_name,
            contact_id=contact_id,
            contact_name=contact_name,
            tax_percent=tax_percent,
            tax_amount=tax_amount,
            invoice_discount=invoice_discount,
            subtotal=subtotal,
            total_excl_tax=total_excl_tax,
            total_incl_tax=total_incl_tax,
            order_date=order_date,
            posting_date=posting_date,
            document_date=document_date,
            due_date=due_date,
            shipment_date=shipment_date,
            payment_terms_code=payment_terms_code,
            payment_method_name=payment_method_name,
            payment_status=payment_status,
            payment_transaction_id=payment_transaction_id,
            location_code=location_code,
            shipping_method_code=shipping_method_code,
            customer_id=customer_id,
            reference_no=reference_no,
            shop_account_email=shop_account_email,
            outstanding_amount=outstanding_amount,
            shipping_method_name=shipping_method_name,
            order_lines_count=order_lines_count,
            sell_to_address=sell_to_address,
            bill_to_address=bill_to_address,
            ship_to_address=ship_to_address,
            sales_lines=sales_lines,
            tax_lines=tax_lines,
        )

        return invoice
