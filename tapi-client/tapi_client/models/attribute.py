from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_string import LocalizedString


T = TypeVar("T", bound="Attribute")


@attr.s(auto_attribs=True)
class Attribute:
    """Model representing an attribute of an item.

    Attributes:
        thibert_part_number (Union[Unset, None, str]): Part number of the item associated with this attribute.
        attribute_id (Union[Unset, None, str]): ID of this attribute.
        attribute_names (Union[Unset, None, List['LocalizedString']]): Name of this attribute.
        attribute_values (Union[Unset, None, List['LocalizedString']]): Value of this attribute.
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    attribute_id: Union[Unset, None, str] = UNSET
    attribute_names: Union[Unset, None, List["LocalizedString"]] = UNSET
    attribute_values: Union[Unset, None, List["LocalizedString"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        attribute_id = self.attribute_id
        attribute_names: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_names, Unset):
            if self.attribute_names is None:
                attribute_names = None
            else:
                attribute_names = []
                for attribute_names_item_data in self.attribute_names:
                    attribute_names_item = attribute_names_item_data.to_dict()

                    attribute_names.append(attribute_names_item)

        attribute_values: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_values, Unset):
            if self.attribute_values is None:
                attribute_values = None
            else:
                attribute_values = []
                for attribute_values_item_data in self.attribute_values:
                    attribute_values_item = attribute_values_item_data.to_dict()

                    attribute_values.append(attribute_values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if attribute_id is not UNSET:
            field_dict["attributeID"] = attribute_id
        if attribute_names is not UNSET:
            field_dict["attributeNames"] = attribute_names
        if attribute_values is not UNSET:
            field_dict["attributeValues"] = attribute_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.localized_string import LocalizedString

        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        attribute_id = d.pop("attributeID", UNSET)

        attribute_names = []
        _attribute_names = d.pop("attributeNames", UNSET)
        for attribute_names_item_data in _attribute_names or []:
            attribute_names_item = LocalizedString.from_dict(attribute_names_item_data)

            attribute_names.append(attribute_names_item)

        attribute_values = []
        _attribute_values = d.pop("attributeValues", UNSET)
        for attribute_values_item_data in _attribute_values or []:
            attribute_values_item = LocalizedString.from_dict(attribute_values_item_data)

            attribute_values.append(attribute_values_item)

        attribute = cls(
            thibert_part_number=thibert_part_number,
            attribute_id=attribute_id,
            attribute_names=attribute_names,
            attribute_values=attribute_values,
        )

        return attribute
