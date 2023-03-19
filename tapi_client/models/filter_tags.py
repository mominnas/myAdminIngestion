from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterTags")


@attr.s(auto_attribs=True)
class FilterTags:
    """
    Attributes:
        tag_name (Union[Unset, None, str]):
        tag_order (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        value (Union[Unset, None, str]):
    """

    tag_name: Union[Unset, None, str] = UNSET
    tag_order: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tag_name = self.tag_name
        tag_order = self.tag_order
        name = self.name
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if tag_name is not UNSET:
            field_dict["tagName"] = tag_name
        if tag_order is not UNSET:
            field_dict["tagOrder"] = tag_order
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag_name = d.pop("tagName", UNSET)

        tag_order = d.pop("tagOrder", UNSET)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        filter_tags = cls(
            tag_name=tag_name,
            tag_order=tag_order,
            name=name,
            value=value,
        )

        return filter_tags
