from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartIsVehicleSpecific")


@attr.s(auto_attribs=True)
class PartIsVehicleSpecific:
    """
    Attributes:
        thibert_part_number (Union[Unset, None, str]): ThibertPartNumber validated
        is_vehicle_specific (Union[Unset, bool]): Indicates if there is a specific fitment for this part
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    is_vehicle_specific: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        is_vehicle_specific = self.is_vehicle_specific

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if is_vehicle_specific is not UNSET:
            field_dict["isVehicleSpecific"] = is_vehicle_specific

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        is_vehicle_specific = d.pop("isVehicleSpecific", UNSET)

        part_is_vehicle_specific = cls(
            thibert_part_number=thibert_part_number,
            is_vehicle_specific=is_vehicle_specific,
        )

        return part_is_vehicle_specific
