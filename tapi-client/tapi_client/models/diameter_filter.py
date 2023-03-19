from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiameterFilter")


@attr.s(auto_attribs=True)
class DiameterFilter:
    """
    Attributes:
        diameter (Union[Unset, int]):
    """

    diameter: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        diameter = self.diameter

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if diameter is not UNSET:
            field_dict["diameter"] = diameter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        diameter = d.pop("diameter", UNSET)

        diameter_filter = cls(
            diameter=diameter,
        )

        return diameter_filter
