"""Keystone API client. This is a simple wrapper around the Keystone API."""
from zeep import Client
import cred

WSDL: str = cred.WSDL
KEY: str = cred.KEY


"""
Input Value Description:
key (String)
FullAccountNo (String) 
OrderProcessMethod (Integer)
PartNumberQuantity (String)
DropShipFirstName (String) 25 char
DropShipMiddleInitial (String) 1 char
DropShipLastName (String) 25 char
DropShipAddress1 (String) 35 char
DropShipAddress2 (String) 35 char
DropShipCity (String) 30 char
DropShipState (String) 2 char
DropShipPostalCode (String) 12 char
DropShipPhone (String) 15 char
DropShipState (String) 2 char
DropShipCountry (String) 3 char
DropShipEmail (String) 255 char
PONumber (String) 20 char
AdditionalInfo (String) 255 char
ServiceLevel (String) 3 char
"""


def drop_ship_multiple_parts(
    key: str,
    full_account_no: str,
    order_process_method: str,
    part_number_quantity: dict,
    drop_ship_firstname: str,
    dropship_middle_initial: str,
    dropship_lastname: str,
    dropship_address1: str,
    dropship_address2: str,
    dropship_city: str,
    dropship_state: str,
    dropship_postalsode: str,
    dropship_phone: str,
    dropship_country: str,
    dropship_email: str,
    po_number: str,
    service_level: str,
    additional_info: str = "",
) -> str:
    """Create a web service method and place an order based on the information passed in.
    
    It returns a real-time status on the line item(s). It accepts multiple line items per order,
    and allows different shipping options, available through the GetShippingOptions method.
    All orders can be viewed through eKeystone or the GetOrderHistory web method.
    Args:
        key (str): A web service security key.
        full_account_no (str): The 5-7 character account number provided by Keystone.
        order_process_method (str):What to do with the order:
                                    ____0 - Verify Order - No parts are ordered; This assures
                                            the user that the order can be fulfilled by Keystone.
                                    ____1 - Complete order - All parts are ordered if zero 'X'
                                            records are returned; ORDER FAILS IF THERE IS
                                            ONE OR MORE 'X' RECORDS.
        part_number_quantity (dict):Partnumber (Keystone vendor line code and the Keystone part num)
                                        and quantity. The string is in the following format:
                                    ____'K33332206,1|G12100,1,Special Deal'- a comma seperates the
                                            part number from the quantity and Additional Part
                                            Information (OPTIONAL).
                                    ____A pipe '|' seperates the full part number and quantity from
                                        additional part number/quantity groups.
                                    ____ A maximum of 250 partnumber/quantity groupings is allowed.
        drop_ship_firstname (str): Drop ship customer's first name.
        dropship_middle_initial (str): Drop ship customer's middle initial.
        dropship_lastname (str): Drop ship customer's last name.
        dropship_address1 (str): Drop ship customer's address line 1.
        dropship_address2 (str): Drop ship customer's address line 2.
        dropship_city (str): Drop ship customer's city.
        dropship_state (str): Drop ship customer's state.
        dropship_postalsode (str): Drop ship customer's postal code.
        dropship_phone (str): Drop ship customer's phone - use format: XXX-XXX-XXXX.
        dropship_country (str): Drop ship customer's country.
        dropship_email (str): Drop ship customer's email.
        po_number (str): The PO number for this order's line items.
        service_level (str): The shipping method for this item.
                            This can be found through the GetShippingOptions web method.
        additional_info (str): NOT CURRENTLY IMPLEMENTED, use PartNumberQuantity
                            to pass additional info by part.
    Returns:
        str: Output - A dataset with two tables, 'Status' and 'PartResults'.
                    The Status table contains one row. Possible outputs are:
                        "OK", "Verified" or "Error: " + error message.
                    The PartResults table contains a list of the input parts,
                        quantity, status and statusmessage.
                    The 'Status' column value of the PartResults table will be
                        ' ' or 'X'. 'X' is a non orderable item;
                        the 'StatusMessage' column will display the
                        reason for which the order was rejected.
    """
    return str("")






def get_client(wsdl: str=WSDL) -> Client:
    """Create a SOAP client.
    
    Args:
        wsdl (str): The WSDL file link for the SOAP client.
    Returns:
        Client: A SOAP client.
    """
    client: Client = Client(wsdl)
    result = client.service.GetUser(123)  # request user with ID 123
    name = result["Username"]
    print(name)
    return client




