from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.part import Part


T = TypeVar("T", bound="WheelInstallationKit")


@attr.s(auto_attribs=True)
class WheelInstallationKit:
    """
    Attributes:
        thibert_part_number (Union[Unset, None, str]): Thibert part number associated with this part.
        part (Union[Unset, Part]): Represents the information Thibert holds on a part.
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    part: Union[Unset, "Part"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        part: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.part, Unset):
            part = self.part.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if part is not UNSET:
            field_dict["part"] = part

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.part import Part

        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        _part = d.pop("part", UNSET)
        part: Union[Unset, Part]
        if isinstance(_part, Unset):
            part = UNSET
        else:
            part = Part.from_dict(_part)

        wheel_installation_kit = cls(
            thibert_part_number=thibert_part_number,
            part=part,
        )

        return wheel_installation_kit
