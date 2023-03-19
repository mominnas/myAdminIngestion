from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_string import LocalizedString


T = TypeVar("T", bound="Category")


@attr.s(auto_attribs=True)
class Category:
    """
    Attributes:
        thibert_part_number (Union[Unset, None, str]): Part number of the item associated with this category.
        category_id (Union[Unset, None, str]): CategoryID of the category represented in this hierarchy
        category_level (Union[Unset, int]): Level of the category represented in this hierarchy
        category_id_level_1 (Union[Unset, None, str]): CategoryID for the Level1 of this hierarchy
        category_name_level_1 (Union[Unset, None, List['LocalizedString']]): Name of the category at Level1
        category_id_level_2 (Union[Unset, None, str]): CategoryID for the Level2 of this hierarchy
        category_name_level_2 (Union[Unset, None, List['LocalizedString']]): Name of the category at Level2
        category_id_level_3 (Union[Unset, None, str]): CategoryID for the Level3 of this hierarchy
        category_name_level_3 (Union[Unset, None, List['LocalizedString']]): Name of the category at Level3
        category_id_level_4 (Union[Unset, None, str]): CategoryID for the Level4 of this hierarchy
        category_name_level_4 (Union[Unset, None, List['LocalizedString']]): Name of the category at Level4
        category_id_level_5 (Union[Unset, None, str]): CategoryID for the Level5 of this hierarchy
        category_name_level_5 (Union[Unset, None, List['LocalizedString']]): Name of the category at Level5
        category_id_level_6 (Union[Unset, None, str]): CategoryID for the Level6 of this hierarchy
        category_name_level_6 (Union[Unset, None, List['LocalizedString']]): Name of the category at Level6
        category_id_level_7 (Union[Unset, None, str]): CategoryID for the Level7 of this hierarchy
        category_name_level_7 (Union[Unset, None, List['LocalizedString']]): Name of the category at Level7
        category_image_url (Union[Unset, None, str]): Image of the category represented in this hierarchy
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    category_id: Union[Unset, None, str] = UNSET
    category_level: Union[Unset, int] = UNSET
    category_id_level_1: Union[Unset, None, str] = UNSET
    category_name_level_1: Union[Unset, None, List["LocalizedString"]] = UNSET
    category_id_level_2: Union[Unset, None, str] = UNSET
    category_name_level_2: Union[Unset, None, List["LocalizedString"]] = UNSET
    category_id_level_3: Union[Unset, None, str] = UNSET
    category_name_level_3: Union[Unset, None, List["LocalizedString"]] = UNSET
    category_id_level_4: Union[Unset, None, str] = UNSET
    category_name_level_4: Union[Unset, None, List["LocalizedString"]] = UNSET
    category_id_level_5: Union[Unset, None, str] = UNSET
    category_name_level_5: Union[Unset, None, List["LocalizedString"]] = UNSET
    category_id_level_6: Union[Unset, None, str] = UNSET
    category_name_level_6: Union[Unset, None, List["LocalizedString"]] = UNSET
    category_id_level_7: Union[Unset, None, str] = UNSET
    category_name_level_7: Union[Unset, None, List["LocalizedString"]] = UNSET
    category_image_url: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        category_id = self.category_id
        category_level = self.category_level
        category_id_level_1 = self.category_id_level_1
        category_name_level_1: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.category_name_level_1, Unset):
            if self.category_name_level_1 is None:
                category_name_level_1 = None
            else:
                category_name_level_1 = []
                for category_name_level_1_item_data in self.category_name_level_1:
                    category_name_level_1_item = category_name_level_1_item_data.to_dict()

                    category_name_level_1.append(category_name_level_1_item)

        category_id_level_2 = self.category_id_level_2
        category_name_level_2: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.category_name_level_2, Unset):
            if self.category_name_level_2 is None:
                category_name_level_2 = None
            else:
                category_name_level_2 = []
                for category_name_level_2_item_data in self.category_name_level_2:
                    category_name_level_2_item = category_name_level_2_item_data.to_dict()

                    category_name_level_2.append(category_name_level_2_item)

        category_id_level_3 = self.category_id_level_3
        category_name_level_3: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.category_name_level_3, Unset):
            if self.category_name_level_3 is None:
                category_name_level_3 = None
            else:
                category_name_level_3 = []
                for category_name_level_3_item_data in self.category_name_level_3:
                    category_name_level_3_item = category_name_level_3_item_data.to_dict()

                    category_name_level_3.append(category_name_level_3_item)

        category_id_level_4 = self.category_id_level_4
        category_name_level_4: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.category_name_level_4, Unset):
            if self.category_name_level_4 is None:
                category_name_level_4 = None
            else:
                category_name_level_4 = []
                for category_name_level_4_item_data in self.category_name_level_4:
                    category_name_level_4_item = category_name_level_4_item_data.to_dict()

                    category_name_level_4.append(category_name_level_4_item)

        category_id_level_5 = self.category_id_level_5
        category_name_level_5: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.category_name_level_5, Unset):
            if self.category_name_level_5 is None:
                category_name_level_5 = None
            else:
                category_name_level_5 = []
                for category_name_level_5_item_data in self.category_name_level_5:
                    category_name_level_5_item = category_name_level_5_item_data.to_dict()

                    category_name_level_5.append(category_name_level_5_item)

        category_id_level_6 = self.category_id_level_6
        category_name_level_6: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.category_name_level_6, Unset):
            if self.category_name_level_6 is None:
                category_name_level_6 = None
            else:
                category_name_level_6 = []
                for category_name_level_6_item_data in self.category_name_level_6:
                    category_name_level_6_item = category_name_level_6_item_data.to_dict()

                    category_name_level_6.append(category_name_level_6_item)

        category_id_level_7 = self.category_id_level_7
        category_name_level_7: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.category_name_level_7, Unset):
            if self.category_name_level_7 is None:
                category_name_level_7 = None
            else:
                category_name_level_7 = []
                for category_name_level_7_item_data in self.category_name_level_7:
                    category_name_level_7_item = category_name_level_7_item_data.to_dict()

                    category_name_level_7.append(category_name_level_7_item)

        category_image_url = self.category_image_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_level is not UNSET:
            field_dict["categoryLevel"] = category_level
        if category_id_level_1 is not UNSET:
            field_dict["categoryIdLevel1"] = category_id_level_1
        if category_name_level_1 is not UNSET:
            field_dict["categoryNameLevel1"] = category_name_level_1
        if category_id_level_2 is not UNSET:
            field_dict["categoryIdLevel2"] = category_id_level_2
        if category_name_level_2 is not UNSET:
            field_dict["categoryNameLevel2"] = category_name_level_2
        if category_id_level_3 is not UNSET:
            field_dict["categoryIdLevel3"] = category_id_level_3
        if category_name_level_3 is not UNSET:
            field_dict["categoryNameLevel3"] = category_name_level_3
        if category_id_level_4 is not UNSET:
            field_dict["categoryIdLevel4"] = category_id_level_4
        if category_name_level_4 is not UNSET:
            field_dict["categoryNameLevel4"] = category_name_level_4
        if category_id_level_5 is not UNSET:
            field_dict["categoryIdLevel5"] = category_id_level_5
        if category_name_level_5 is not UNSET:
            field_dict["categoryNameLevel5"] = category_name_level_5
        if category_id_level_6 is not UNSET:
            field_dict["categoryIdLevel6"] = category_id_level_6
        if category_name_level_6 is not UNSET:
            field_dict["categoryNameLevel6"] = category_name_level_6
        if category_id_level_7 is not UNSET:
            field_dict["categoryIdLevel7"] = category_id_level_7
        if category_name_level_7 is not UNSET:
            field_dict["categoryNameLevel7"] = category_name_level_7
        if category_image_url is not UNSET:
            field_dict["categoryImageURL"] = category_image_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.localized_string import LocalizedString

        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        category_id = d.pop("categoryId", UNSET)

        category_level = d.pop("categoryLevel", UNSET)

        category_id_level_1 = d.pop("categoryIdLevel1", UNSET)

        category_name_level_1 = []
        _category_name_level_1 = d.pop("categoryNameLevel1", UNSET)
        for category_name_level_1_item_data in _category_name_level_1 or []:
            category_name_level_1_item = LocalizedString.from_dict(category_name_level_1_item_data)

            category_name_level_1.append(category_name_level_1_item)

        category_id_level_2 = d.pop("categoryIdLevel2", UNSET)

        category_name_level_2 = []
        _category_name_level_2 = d.pop("categoryNameLevel2", UNSET)
        for category_name_level_2_item_data in _category_name_level_2 or []:
            category_name_level_2_item = LocalizedString.from_dict(category_name_level_2_item_data)

            category_name_level_2.append(category_name_level_2_item)

        category_id_level_3 = d.pop("categoryIdLevel3", UNSET)

        category_name_level_3 = []
        _category_name_level_3 = d.pop("categoryNameLevel3", UNSET)
        for category_name_level_3_item_data in _category_name_level_3 or []:
            category_name_level_3_item = LocalizedString.from_dict(category_name_level_3_item_data)

            category_name_level_3.append(category_name_level_3_item)

        category_id_level_4 = d.pop("categoryIdLevel4", UNSET)

        category_name_level_4 = []
        _category_name_level_4 = d.pop("categoryNameLevel4", UNSET)
        for category_name_level_4_item_data in _category_name_level_4 or []:
            category_name_level_4_item = LocalizedString.from_dict(category_name_level_4_item_data)

            category_name_level_4.append(category_name_level_4_item)

        category_id_level_5 = d.pop("categoryIdLevel5", UNSET)

        category_name_level_5 = []
        _category_name_level_5 = d.pop("categoryNameLevel5", UNSET)
        for category_name_level_5_item_data in _category_name_level_5 or []:
            category_name_level_5_item = LocalizedString.from_dict(category_name_level_5_item_data)

            category_name_level_5.append(category_name_level_5_item)

        category_id_level_6 = d.pop("categoryIdLevel6", UNSET)

        category_name_level_6 = []
        _category_name_level_6 = d.pop("categoryNameLevel6", UNSET)
        for category_name_level_6_item_data in _category_name_level_6 or []:
            category_name_level_6_item = LocalizedString.from_dict(category_name_level_6_item_data)

            category_name_level_6.append(category_name_level_6_item)

        category_id_level_7 = d.pop("categoryIdLevel7", UNSET)

        category_name_level_7 = []
        _category_name_level_7 = d.pop("categoryNameLevel7", UNSET)
        for category_name_level_7_item_data in _category_name_level_7 or []:
            category_name_level_7_item = LocalizedString.from_dict(category_name_level_7_item_data)

            category_name_level_7.append(category_name_level_7_item)

        category_image_url = d.pop("categoryImageURL", UNSET)

        category = cls(
            thibert_part_number=thibert_part_number,
            category_id=category_id,
            category_level=category_level,
            category_id_level_1=category_id_level_1,
            category_name_level_1=category_name_level_1,
            category_id_level_2=category_id_level_2,
            category_name_level_2=category_name_level_2,
            category_id_level_3=category_id_level_3,
            category_name_level_3=category_name_level_3,
            category_id_level_4=category_id_level_4,
            category_name_level_4=category_name_level_4,
            category_id_level_5=category_id_level_5,
            category_name_level_5=category_name_level_5,
            category_id_level_6=category_id_level_6,
            category_name_level_6=category_name_level_6,
            category_id_level_7=category_id_level_7,
            category_name_level_7=category_name_level_7,
            category_image_url=category_image_url,
        )

        return category
