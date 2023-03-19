from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wheel_installation_kit import WheelInstallationKit
    from ..models.wheel_installation_part import WheelInstallationPart


T = TypeVar("T", bound="WheelInstallation")


@attr.s(auto_attribs=True)
class WheelInstallation:
    """
    Attributes:
        thibert_part_number (Union[Unset, None, str]): Thibert part number
        wheel_installation_kits (Union[Unset, None, List['WheelInstallationKit']]):
        wheel_installation_parts (Union[Unset, None, List['WheelInstallationPart']]):
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    wheel_installation_kits: Union[Unset, None, List["WheelInstallationKit"]] = UNSET
    wheel_installation_parts: Union[Unset, None, List["WheelInstallationPart"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        wheel_installation_kits: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.wheel_installation_kits, Unset):
            if self.wheel_installation_kits is None:
                wheel_installation_kits = None
            else:
                wheel_installation_kits = []
                for wheel_installation_kits_item_data in self.wheel_installation_kits:
                    wheel_installation_kits_item = wheel_installation_kits_item_data.to_dict()

                    wheel_installation_kits.append(wheel_installation_kits_item)

        wheel_installation_parts: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.wheel_installation_parts, Unset):
            if self.wheel_installation_parts is None:
                wheel_installation_parts = None
            else:
                wheel_installation_parts = []
                for wheel_installation_parts_item_data in self.wheel_installation_parts:
                    wheel_installation_parts_item = wheel_installation_parts_item_data.to_dict()

                    wheel_installation_parts.append(wheel_installation_parts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if wheel_installation_kits is not UNSET:
            field_dict["wheelInstallationKits"] = wheel_installation_kits
        if wheel_installation_parts is not UNSET:
            field_dict["wheelInstallationParts"] = wheel_installation_parts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wheel_installation_kit import WheelInstallationKit
        from ..models.wheel_installation_part import WheelInstallationPart

        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        wheel_installation_kits = []
        _wheel_installation_kits = d.pop("wheelInstallationKits", UNSET)
        for wheel_installation_kits_item_data in _wheel_installation_kits or []:
            wheel_installation_kits_item = WheelInstallationKit.from_dict(wheel_installation_kits_item_data)

            wheel_installation_kits.append(wheel_installation_kits_item)

        wheel_installation_parts = []
        _wheel_installation_parts = d.pop("wheelInstallationParts", UNSET)
        for wheel_installation_parts_item_data in _wheel_installation_parts or []:
            wheel_installation_parts_item = WheelInstallationPart.from_dict(wheel_installation_parts_item_data)

            wheel_installation_parts.append(wheel_installation_parts_item)

        wheel_installation = cls(
            thibert_part_number=thibert_part_number,
            wheel_installation_kits=wheel_installation_kits,
            wheel_installation_parts=wheel_installation_parts,
        )

        return wheel_installation
