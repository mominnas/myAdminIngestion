from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_string import LocalizedString


T = TypeVar("T", bound="WheelPartType")


@attr.s(auto_attribs=True)
class WheelPartType:
    """Model representing the Wheel Part Type.

    Attributes:
        wheel_part_type_id (Union[Unset, None, str]): WheelPartTypeID used to filter result Example: 00020.
        wheel_part_types (Union[Unset, None, List['LocalizedString']]): WheelPartType Name
    """

    wheel_part_type_id: Union[Unset, None, str] = UNSET
    wheel_part_types: Union[Unset, None, List["LocalizedString"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        wheel_part_type_id = self.wheel_part_type_id
        wheel_part_types: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.wheel_part_types, Unset):
            if self.wheel_part_types is None:
                wheel_part_types = None
            else:
                wheel_part_types = []
                for wheel_part_types_item_data in self.wheel_part_types:
                    wheel_part_types_item = wheel_part_types_item_data.to_dict()

                    wheel_part_types.append(wheel_part_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if wheel_part_type_id is not UNSET:
            field_dict["wheelPartTypeID"] = wheel_part_type_id
        if wheel_part_types is not UNSET:
            field_dict["wheelPartTypes"] = wheel_part_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.localized_string import LocalizedString

        d = src_dict.copy()
        wheel_part_type_id = d.pop("wheelPartTypeID", UNSET)

        wheel_part_types = []
        _wheel_part_types = d.pop("wheelPartTypes", UNSET)
        for wheel_part_types_item_data in _wheel_part_types or []:
            wheel_part_types_item = LocalizedString.from_dict(wheel_part_types_item_data)

            wheel_part_types.append(wheel_part_types_item)

        wheel_part_type = cls(
            wheel_part_type_id=wheel_part_type_id,
            wheel_part_types=wheel_part_types,
        )

        return wheel_part_type
