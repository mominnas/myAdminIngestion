import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribute import Attribute
    from ..models.category import Category
    from ..models.fitment_details import FitmentDetails
    from ..models.image import Image
    from ..models.inventory import Inventory
    from ..models.localized_string import LocalizedString
    from ..models.prices_by_currencies import PricesByCurrencies
    from ..models.related_part import RelatedPart


T = TypeVar("T", bound="Part")


@attr.s(auto_attribs=True)
class Part:
    """Represents the information Thibert holds on a part.

    Attributes:
        thibert_part_number (Union[Unset, None, str]): Thibert part number associated with this item. Example: 082030.
        your_price (Union[Unset, float]): Price of this item for the given customer. Example: 124.02.
        your_price_currency_code (Union[Unset, None, str]): Currency of YourPrice for the given customer. Example: CAD.
        jobber_price (Union[Unset, None, List['PricesByCurrencies']]): Jobber price of this item.
        msrp_price (Union[Unset, None, List['PricesByCurrencies']]): Manufacturer's suggested retail price of this item.
        map_price (Union[Unset, None, List['PricesByCurrencies']]): Manufacturer's suggested retail price of this item.
        vendor_part_number (Union[Unset, None, str]): Manufacturer's part number of this item. Example:
            32571885114342731MM1.
        brand (Union[Unset, None, str]): Brand associated with this item. Example: RTX.
        model (Union[Unset, None, str]): Model of this item. Example: Scalene.
        series (Union[Unset, None, str]): Series of this item. Example: RTX OE.
        web_status (Union[Unset, None, str]): Availability status of this item. Example: Active.
        titles (Union[Unset, None, List['LocalizedString']]): Titles of this item.
        short_descriptions (Union[Unset, None, List['LocalizedString']]): Short description of this item.
        long_descriptions (Union[Unset, None, List['LocalizedString']]): Long description of this item.
        application_notes (Union[Unset, None, List['LocalizedString']]): Application note for the buyer.
        replacement_item (Union[Unset, None, str]): Item which replaces this item.
        wheel_part_type_id (Union[Unset, None, str]): WheelPartTypeID (00030 = Dually, 00076 = Styled Steel, 00021 =
            Steel, 00020 = Alloy)
        wheel_part_type (Union[Unset, None, List['LocalizedString']]): Wheel Part Type (Dually, Styled Steel, Steel,
            Alloy) in english and french
        is_on_clearance (Union[Unset, bool]): Indicates if this part is on clearance
        is_on_clearance_title (Union[Unset, None, List['LocalizedString']]): Title of the Clearance
        is_new_arrival (Union[Unset, bool]): Indicates if this part is a new arrival
        is_new_arrival_title (Union[Unset, None, List['LocalizedString']]): Title of the new arrival
        is_overweight (Union[Unset, bool]): Indicates if this part is Overweight
        is_oversize (Union[Unset, bool]): Indicates if this part is Oversize
        unit_net_weight_packed_lbs (Union[Unset, float]): Indicate the unit weight packed (lbs)
        unit_height_packed (Union[Unset, float]): Indicate the Height packed (inch)
        unit_length_packed (Union[Unset, float]): Indicate the Length packed (inch)
        unit_width_packed (Union[Unset, float]): Indicate the Width packed (inch)
        unit_upc_code (Union[Unset, None, str]): Indicate the UPC of this item
        last_modification_date (Union[Unset, datetime.datetime]):
        images (Union[Unset, None, List['Image']]): List of all images associated with this item.
        attributes (Union[Unset, None, List['Attribute']]): List of all attributes associated with this item.
        inventories (Union[Unset, None, List['Inventory']]): List of all inventories associated with this item.
        categories (Union[Unset, None, List['Category']]): List of all categories associated with this item.
        fitment_details (Union[Unset, FitmentDetails]):
        related_parts (Union[Unset, None, List['RelatedPart']]): List of suggested related parts (ex: You might also
            like, Useful accessories ...)
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    your_price: Union[Unset, float] = UNSET
    your_price_currency_code: Union[Unset, None, str] = UNSET
    jobber_price: Union[Unset, None, List["PricesByCurrencies"]] = UNSET
    msrp_price: Union[Unset, None, List["PricesByCurrencies"]] = UNSET
    map_price: Union[Unset, None, List["PricesByCurrencies"]] = UNSET
    vendor_part_number: Union[Unset, None, str] = UNSET
    brand: Union[Unset, None, str] = UNSET
    model: Union[Unset, None, str] = UNSET
    series: Union[Unset, None, str] = UNSET
    web_status: Union[Unset, None, str] = UNSET
    titles: Union[Unset, None, List["LocalizedString"]] = UNSET
    short_descriptions: Union[Unset, None, List["LocalizedString"]] = UNSET
    long_descriptions: Union[Unset, None, List["LocalizedString"]] = UNSET
    application_notes: Union[Unset, None, List["LocalizedString"]] = UNSET
    replacement_item: Union[Unset, None, str] = UNSET
    wheel_part_type_id: Union[Unset, None, str] = UNSET
    wheel_part_type: Union[Unset, None, List["LocalizedString"]] = UNSET
    is_on_clearance: Union[Unset, bool] = UNSET
    is_on_clearance_title: Union[Unset, None, List["LocalizedString"]] = UNSET
    is_new_arrival: Union[Unset, bool] = UNSET
    is_new_arrival_title: Union[Unset, None, List["LocalizedString"]] = UNSET
    is_overweight: Union[Unset, bool] = UNSET
    is_oversize: Union[Unset, bool] = UNSET
    unit_net_weight_packed_lbs: Union[Unset, float] = UNSET
    unit_height_packed: Union[Unset, float] = UNSET
    unit_length_packed: Union[Unset, float] = UNSET
    unit_width_packed: Union[Unset, float] = UNSET
    unit_upc_code: Union[Unset, None, str] = UNSET
    last_modification_date: Union[Unset, datetime.datetime] = UNSET
    images: Union[Unset, None, List["Image"]] = UNSET
    attributes: Union[Unset, None, List["Attribute"]] = UNSET
    inventories: Union[Unset, None, List["Inventory"]] = UNSET
    categories: Union[Unset, None, List["Category"]] = UNSET
    fitment_details: Union[Unset, "FitmentDetails"] = UNSET
    related_parts: Union[Unset, None, List["RelatedPart"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        your_price = self.your_price
        your_price_currency_code = self.your_price_currency_code
        jobber_price: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.jobber_price, Unset):
            if self.jobber_price is None:
                jobber_price = None
            else:
                jobber_price = []
                for jobber_price_item_data in self.jobber_price:
                    jobber_price_item = jobber_price_item_data.to_dict()

                    jobber_price.append(jobber_price_item)

        msrp_price: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.msrp_price, Unset):
            if self.msrp_price is None:
                msrp_price = None
            else:
                msrp_price = []
                for msrp_price_item_data in self.msrp_price:
                    msrp_price_item = msrp_price_item_data.to_dict()

                    msrp_price.append(msrp_price_item)

        map_price: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.map_price, Unset):
            if self.map_price is None:
                map_price = None
            else:
                map_price = []
                for map_price_item_data in self.map_price:
                    map_price_item = map_price_item_data.to_dict()

                    map_price.append(map_price_item)

        vendor_part_number = self.vendor_part_number
        brand = self.brand
        model = self.model
        series = self.series
        web_status = self.web_status
        titles: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.titles, Unset):
            if self.titles is None:
                titles = None
            else:
                titles = []
                for titles_item_data in self.titles:
                    titles_item = titles_item_data.to_dict()

                    titles.append(titles_item)

        short_descriptions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.short_descriptions, Unset):
            if self.short_descriptions is None:
                short_descriptions = None
            else:
                short_descriptions = []
                for short_descriptions_item_data in self.short_descriptions:
                    short_descriptions_item = short_descriptions_item_data.to_dict()

                    short_descriptions.append(short_descriptions_item)

        long_descriptions: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.long_descriptions, Unset):
            if self.long_descriptions is None:
                long_descriptions = None
            else:
                long_descriptions = []
                for long_descriptions_item_data in self.long_descriptions:
                    long_descriptions_item = long_descriptions_item_data.to_dict()

                    long_descriptions.append(long_descriptions_item)

        application_notes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.application_notes, Unset):
            if self.application_notes is None:
                application_notes = None
            else:
                application_notes = []
                for application_notes_item_data in self.application_notes:
                    application_notes_item = application_notes_item_data.to_dict()

                    application_notes.append(application_notes_item)

        replacement_item = self.replacement_item
        wheel_part_type_id = self.wheel_part_type_id
        wheel_part_type: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.wheel_part_type, Unset):
            if self.wheel_part_type is None:
                wheel_part_type = None
            else:
                wheel_part_type = []
                for wheel_part_type_item_data in self.wheel_part_type:
                    wheel_part_type_item = wheel_part_type_item_data.to_dict()

                    wheel_part_type.append(wheel_part_type_item)

        is_on_clearance = self.is_on_clearance
        is_on_clearance_title: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.is_on_clearance_title, Unset):
            if self.is_on_clearance_title is None:
                is_on_clearance_title = None
            else:
                is_on_clearance_title = []
                for is_on_clearance_title_item_data in self.is_on_clearance_title:
                    is_on_clearance_title_item = is_on_clearance_title_item_data.to_dict()

                    is_on_clearance_title.append(is_on_clearance_title_item)

        is_new_arrival = self.is_new_arrival
        is_new_arrival_title: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.is_new_arrival_title, Unset):
            if self.is_new_arrival_title is None:
                is_new_arrival_title = None
            else:
                is_new_arrival_title = []
                for is_new_arrival_title_item_data in self.is_new_arrival_title:
                    is_new_arrival_title_item = is_new_arrival_title_item_data.to_dict()

                    is_new_arrival_title.append(is_new_arrival_title_item)

        is_overweight = self.is_overweight
        is_oversize = self.is_oversize
        unit_net_weight_packed_lbs = self.unit_net_weight_packed_lbs
        unit_height_packed = self.unit_height_packed
        unit_length_packed = self.unit_length_packed
        unit_width_packed = self.unit_width_packed
        unit_upc_code = self.unit_upc_code
        last_modification_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_modification_date, Unset):
            last_modification_date = self.last_modification_date.isoformat()

        images: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            if self.images is None:
                images = None
            else:
                images = []
                for images_item_data in self.images:
                    images_item = images_item_data.to_dict()

                    images.append(images_item)

        attributes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            if self.attributes is None:
                attributes = None
            else:
                attributes = []
                for attributes_item_data in self.attributes:
                    attributes_item = attributes_item_data.to_dict()

                    attributes.append(attributes_item)

        inventories: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inventories, Unset):
            if self.inventories is None:
                inventories = None
            else:
                inventories = []
                for inventories_item_data in self.inventories:
                    inventories_item = inventories_item_data.to_dict()

                    inventories.append(inventories_item)

        categories: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            if self.categories is None:
                categories = None
            else:
                categories = []
                for categories_item_data in self.categories:
                    categories_item = categories_item_data.to_dict()

                    categories.append(categories_item)

        fitment_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fitment_details, Unset):
            fitment_details = self.fitment_details.to_dict()

        related_parts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.related_parts, Unset):
            if self.related_parts is None:
                related_parts = None
            else:
                related_parts = []
                for related_parts_item_data in self.related_parts:
                    related_parts_item = related_parts_item_data.to_dict()

                    related_parts.append(related_parts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if your_price is not UNSET:
            field_dict["yourPrice"] = your_price
        if your_price_currency_code is not UNSET:
            field_dict["yourPriceCurrencyCode"] = your_price_currency_code
        if jobber_price is not UNSET:
            field_dict["jobberPrice"] = jobber_price
        if msrp_price is not UNSET:
            field_dict["msrpPrice"] = msrp_price
        if map_price is not UNSET:
            field_dict["mapPrice"] = map_price
        if vendor_part_number is not UNSET:
            field_dict["vendorPartNumber"] = vendor_part_number
        if brand is not UNSET:
            field_dict["brand"] = brand
        if model is not UNSET:
            field_dict["model"] = model
        if series is not UNSET:
            field_dict["series"] = series
        if web_status is not UNSET:
            field_dict["webStatus"] = web_status
        if titles is not UNSET:
            field_dict["titles"] = titles
        if short_descriptions is not UNSET:
            field_dict["shortDescriptions"] = short_descriptions
        if long_descriptions is not UNSET:
            field_dict["longDescriptions"] = long_descriptions
        if application_notes is not UNSET:
            field_dict["applicationNotes"] = application_notes
        if replacement_item is not UNSET:
            field_dict["replacementItem"] = replacement_item
        if wheel_part_type_id is not UNSET:
            field_dict["wheelPartTypeID"] = wheel_part_type_id
        if wheel_part_type is not UNSET:
            field_dict["wheelPartType"] = wheel_part_type
        if is_on_clearance is not UNSET:
            field_dict["isOnClearance"] = is_on_clearance
        if is_on_clearance_title is not UNSET:
            field_dict["isOnClearanceTitle"] = is_on_clearance_title
        if is_new_arrival is not UNSET:
            field_dict["isNewArrival"] = is_new_arrival
        if is_new_arrival_title is not UNSET:
            field_dict["isNewArrivalTitle"] = is_new_arrival_title
        if is_overweight is not UNSET:
            field_dict["isOverweight"] = is_overweight
        if is_oversize is not UNSET:
            field_dict["isOversize"] = is_oversize
        if unit_net_weight_packed_lbs is not UNSET:
            field_dict["unitNetWeightPackedLBS"] = unit_net_weight_packed_lbs
        if unit_height_packed is not UNSET:
            field_dict["unitHeightPacked"] = unit_height_packed
        if unit_length_packed is not UNSET:
            field_dict["unitLengthPacked"] = unit_length_packed
        if unit_width_packed is not UNSET:
            field_dict["unitWidthPacked"] = unit_width_packed
        if unit_upc_code is not UNSET:
            field_dict["unitUPCCode"] = unit_upc_code
        if last_modification_date is not UNSET:
            field_dict["lastModificationDate"] = last_modification_date
        if images is not UNSET:
            field_dict["images"] = images
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if inventories is not UNSET:
            field_dict["inventories"] = inventories
        if categories is not UNSET:
            field_dict["categories"] = categories
        if fitment_details is not UNSET:
            field_dict["fitmentDetails"] = fitment_details
        if related_parts is not UNSET:
            field_dict["relatedParts"] = related_parts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribute import Attribute
        from ..models.category import Category
        from ..models.fitment_details import FitmentDetails
        from ..models.image import Image
        from ..models.inventory import Inventory
        from ..models.localized_string import LocalizedString
        from ..models.prices_by_currencies import PricesByCurrencies
        from ..models.related_part import RelatedPart

        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        your_price = d.pop("yourPrice", UNSET)

        your_price_currency_code = d.pop("yourPriceCurrencyCode", UNSET)

        jobber_price = []
        _jobber_price = d.pop("jobberPrice", UNSET)
        for jobber_price_item_data in _jobber_price or []:
            jobber_price_item = PricesByCurrencies.from_dict(jobber_price_item_data)

            jobber_price.append(jobber_price_item)

        msrp_price = []
        _msrp_price = d.pop("msrpPrice", UNSET)
        for msrp_price_item_data in _msrp_price or []:
            msrp_price_item = PricesByCurrencies.from_dict(msrp_price_item_data)

            msrp_price.append(msrp_price_item)

        map_price = []
        _map_price = d.pop("mapPrice", UNSET)
        for map_price_item_data in _map_price or []:
            map_price_item = PricesByCurrencies.from_dict(map_price_item_data)

            map_price.append(map_price_item)

        vendor_part_number = d.pop("vendorPartNumber", UNSET)

        brand = d.pop("brand", UNSET)

        model = d.pop("model", UNSET)

        series = d.pop("series", UNSET)

        web_status = d.pop("webStatus", UNSET)

        titles = []
        _titles = d.pop("titles", UNSET)
        for titles_item_data in _titles or []:
            titles_item = LocalizedString.from_dict(titles_item_data)

            titles.append(titles_item)

        short_descriptions = []
        _short_descriptions = d.pop("shortDescriptions", UNSET)
        for short_descriptions_item_data in _short_descriptions or []:
            short_descriptions_item = LocalizedString.from_dict(short_descriptions_item_data)

            short_descriptions.append(short_descriptions_item)

        long_descriptions = []
        _long_descriptions = d.pop("longDescriptions", UNSET)
        for long_descriptions_item_data in _long_descriptions or []:
            long_descriptions_item = LocalizedString.from_dict(long_descriptions_item_data)

            long_descriptions.append(long_descriptions_item)

        application_notes = []
        _application_notes = d.pop("applicationNotes", UNSET)
        for application_notes_item_data in _application_notes or []:
            application_notes_item = LocalizedString.from_dict(application_notes_item_data)

            application_notes.append(application_notes_item)

        replacement_item = d.pop("replacementItem", UNSET)

        wheel_part_type_id = d.pop("wheelPartTypeID", UNSET)

        wheel_part_type = []
        _wheel_part_type = d.pop("wheelPartType", UNSET)
        for wheel_part_type_item_data in _wheel_part_type or []:
            wheel_part_type_item = LocalizedString.from_dict(wheel_part_type_item_data)

            wheel_part_type.append(wheel_part_type_item)

        is_on_clearance = d.pop("isOnClearance", UNSET)

        is_on_clearance_title = []
        _is_on_clearance_title = d.pop("isOnClearanceTitle", UNSET)
        for is_on_clearance_title_item_data in _is_on_clearance_title or []:
            is_on_clearance_title_item = LocalizedString.from_dict(is_on_clearance_title_item_data)

            is_on_clearance_title.append(is_on_clearance_title_item)

        is_new_arrival = d.pop("isNewArrival", UNSET)

        is_new_arrival_title = []
        _is_new_arrival_title = d.pop("isNewArrivalTitle", UNSET)
        for is_new_arrival_title_item_data in _is_new_arrival_title or []:
            is_new_arrival_title_item = LocalizedString.from_dict(is_new_arrival_title_item_data)

            is_new_arrival_title.append(is_new_arrival_title_item)

        is_overweight = d.pop("isOverweight", UNSET)

        is_oversize = d.pop("isOversize", UNSET)

        unit_net_weight_packed_lbs = d.pop("unitNetWeightPackedLBS", UNSET)

        unit_height_packed = d.pop("unitHeightPacked", UNSET)

        unit_length_packed = d.pop("unitLengthPacked", UNSET)

        unit_width_packed = d.pop("unitWidthPacked", UNSET)

        unit_upc_code = d.pop("unitUPCCode", UNSET)

        _last_modification_date = d.pop("lastModificationDate", UNSET)
        last_modification_date: Union[Unset, datetime.datetime]
        if isinstance(_last_modification_date, Unset):
            last_modification_date = UNSET
        else:
            last_modification_date = isoparse(_last_modification_date)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = Image.from_dict(images_item_data)

            images.append(images_item)

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = Attribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        inventories = []
        _inventories = d.pop("inventories", UNSET)
        for inventories_item_data in _inventories or []:
            inventories_item = Inventory.from_dict(inventories_item_data)

            inventories.append(inventories_item)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = Category.from_dict(categories_item_data)

            categories.append(categories_item)

        _fitment_details = d.pop("fitmentDetails", UNSET)
        fitment_details: Union[Unset, FitmentDetails]
        if isinstance(_fitment_details, Unset):
            fitment_details = UNSET
        else:
            fitment_details = FitmentDetails.from_dict(_fitment_details)

        related_parts = []
        _related_parts = d.pop("relatedParts", UNSET)
        for related_parts_item_data in _related_parts or []:
            related_parts_item = RelatedPart.from_dict(related_parts_item_data)

            related_parts.append(related_parts_item)

        part = cls(
            thibert_part_number=thibert_part_number,
            your_price=your_price,
            your_price_currency_code=your_price_currency_code,
            jobber_price=jobber_price,
            msrp_price=msrp_price,
            map_price=map_price,
            vendor_part_number=vendor_part_number,
            brand=brand,
            model=model,
            series=series,
            web_status=web_status,
            titles=titles,
            short_descriptions=short_descriptions,
            long_descriptions=long_descriptions,
            application_notes=application_notes,
            replacement_item=replacement_item,
            wheel_part_type_id=wheel_part_type_id,
            wheel_part_type=wheel_part_type,
            is_on_clearance=is_on_clearance,
            is_on_clearance_title=is_on_clearance_title,
            is_new_arrival=is_new_arrival,
            is_new_arrival_title=is_new_arrival_title,
            is_overweight=is_overweight,
            is_oversize=is_oversize,
            unit_net_weight_packed_lbs=unit_net_weight_packed_lbs,
            unit_height_packed=unit_height_packed,
            unit_length_packed=unit_length_packed,
            unit_width_packed=unit_width_packed,
            unit_upc_code=unit_upc_code,
            last_modification_date=last_modification_date,
            images=images,
            attributes=attributes,
            inventories=inventories,
            categories=categories,
            fitment_details=fitment_details,
            related_parts=related_parts,
        )

        return part
