from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory import Inventory


T = TypeVar("T", bound="PartInventory")


@attr.s(auto_attribs=True)
class PartInventory:
    """
    Attributes:
        thibert_part_number (Union[Unset, None, str]): Thibert part number associated with this item. Example: 082030.
        inventories (Union[Unset, None, List['Inventory']]): List of all inventories associated with this item.
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    inventories: Union[Unset, None, List["Inventory"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        inventories: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inventories, Unset):
            if self.inventories is None:
                inventories = None
            else:
                inventories = []
                for inventories_item_data in self.inventories:
                    inventories_item = inventories_item_data.to_dict()

                    inventories.append(inventories_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if inventories is not UNSET:
            field_dict["inventories"] = inventories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.inventory import Inventory

        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        inventories = []
        _inventories = d.pop("inventories", UNSET)
        for inventories_item_data in _inventories or []:
            inventories_item = Inventory.from_dict(inventories_item_data)

            inventories.append(inventories_item)

        part_inventory = cls(
            thibert_part_number=thibert_part_number,
            inventories=inventories,
        )

        return part_inventory
