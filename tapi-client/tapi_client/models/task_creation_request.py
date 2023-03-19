from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_item import TaskItem


T = TypeVar("T", bound="TaskCreationRequest")


@attr.s(auto_attribs=True)
class TaskCreationRequest:
    """
    Attributes:
        assigned_group (Union[Unset, None, str]):
        title (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        items (Union[Unset, None, List['TaskItem']]):
    """

    assigned_group: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    items: Union[Unset, None, List["TaskItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        assigned_group = self.assigned_group
        title = self.title
        description = self.description
        items: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            if self.items is None:
                items = None
            else:
                items = []
                for items_item_data in self.items:
                    items_item = items_item_data.to_dict()

                    items.append(items_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if assigned_group is not UNSET:
            field_dict["assignedGroup"] = assigned_group
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_item import TaskItem

        d = src_dict.copy()
        assigned_group = d.pop("assignedGroup", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = TaskItem.from_dict(items_item_data)

            items.append(items_item)

        task_creation_request = cls(
            assigned_group=assigned_group,
            title=title,
            description=description,
            items=items,
        )

        return task_creation_request
