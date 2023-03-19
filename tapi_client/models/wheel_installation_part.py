from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_string import LocalizedString
    from ..models.part import Part


T = TypeVar("T", bound="WheelInstallationPart")


@attr.s(auto_attribs=True)
class WheelInstallationPart:
    """
    Attributes:
        thibert_part_number (Union[Unset, None, str]): Thibert part number associated with this part.
        bolt_per_wheel_qty (Union[Unset, None, str]): The numbers of Bolts required per wheel for this vehicle
        innerpack (Union[Unset, None, int]): Qty of item in the pack
        qty_per_wheel (Union[Unset, None, int]): Qty needed per wheel
        sort_order (Union[Unset, None, int]):
        installation_part_type (Union[Unset, None, List['LocalizedString']]): Type of installation part
        part (Union[Unset, Part]): Represents the information Thibert holds on a part.
        compatible_keys (Union[Unset, None, List['Part']]): List of compatible keys for the installation of a bolt
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    bolt_per_wheel_qty: Union[Unset, None, str] = UNSET
    innerpack: Union[Unset, None, int] = UNSET
    qty_per_wheel: Union[Unset, None, int] = UNSET
    sort_order: Union[Unset, None, int] = UNSET
    installation_part_type: Union[Unset, None, List["LocalizedString"]] = UNSET
    part: Union[Unset, "Part"] = UNSET
    compatible_keys: Union[Unset, None, List["Part"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        bolt_per_wheel_qty = self.bolt_per_wheel_qty
        innerpack = self.innerpack
        qty_per_wheel = self.qty_per_wheel
        sort_order = self.sort_order
        installation_part_type: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.installation_part_type, Unset):
            if self.installation_part_type is None:
                installation_part_type = None
            else:
                installation_part_type = []
                for installation_part_type_item_data in self.installation_part_type:
                    installation_part_type_item = installation_part_type_item_data.to_dict()

                    installation_part_type.append(installation_part_type_item)

        part: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.part, Unset):
            part = self.part.to_dict()

        compatible_keys: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.compatible_keys, Unset):
            if self.compatible_keys is None:
                compatible_keys = None
            else:
                compatible_keys = []
                for compatible_keys_item_data in self.compatible_keys:
                    compatible_keys_item = compatible_keys_item_data.to_dict()

                    compatible_keys.append(compatible_keys_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if bolt_per_wheel_qty is not UNSET:
            field_dict["boltPerWheelQty"] = bolt_per_wheel_qty
        if innerpack is not UNSET:
            field_dict["innerpack"] = innerpack
        if qty_per_wheel is not UNSET:
            field_dict["qtyPerWheel"] = qty_per_wheel
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if installation_part_type is not UNSET:
            field_dict["installationPartType"] = installation_part_type
        if part is not UNSET:
            field_dict["part"] = part
        if compatible_keys is not UNSET:
            field_dict["compatibleKeys"] = compatible_keys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.localized_string import LocalizedString
        from ..models.part import Part

        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        bolt_per_wheel_qty = d.pop("boltPerWheelQty", UNSET)

        innerpack = d.pop("innerpack", UNSET)

        qty_per_wheel = d.pop("qtyPerWheel", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        installation_part_type = []
        _installation_part_type = d.pop("installationPartType", UNSET)
        for installation_part_type_item_data in _installation_part_type or []:
            installation_part_type_item = LocalizedString.from_dict(installation_part_type_item_data)

            installation_part_type.append(installation_part_type_item)

        _part = d.pop("part", UNSET)
        part: Union[Unset, Part]
        if isinstance(_part, Unset):
            part = UNSET
        else:
            part = Part.from_dict(_part)

        compatible_keys = []
        _compatible_keys = d.pop("compatibleKeys", UNSET)
        for compatible_keys_item_data in _compatible_keys or []:
            compatible_keys_item = Part.from_dict(compatible_keys_item_data)

            compatible_keys.append(compatible_keys_item)

        wheel_installation_part = cls(
            thibert_part_number=thibert_part_number,
            bolt_per_wheel_qty=bolt_per_wheel_qty,
            innerpack=innerpack,
            qty_per_wheel=qty_per_wheel,
            sort_order=sort_order,
            installation_part_type=installation_part_type,
            part=part,
            compatible_keys=compatible_keys,
        )

        return wheel_installation_part
