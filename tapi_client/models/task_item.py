from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskItem")


@attr.s(auto_attribs=True)
class TaskItem:
    """
    Attributes:
        name (Union[Unset, None, str]):
        catalog (Union[Unset, None, str]):
    """

    name: Union[Unset, None, str] = UNSET
    catalog: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        catalog = self.catalog

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if catalog is not UNSET:
            field_dict["catalog"] = catalog

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        catalog = d.pop("catalog", UNSET)

        task_item = cls(
            name=name,
            catalog=catalog,
        )

        return task_item
