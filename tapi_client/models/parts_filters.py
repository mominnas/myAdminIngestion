from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_line import FilterLine


T = TypeVar("T", bound="PartsFilters")


@attr.s(auto_attribs=True)
class PartsFilters:
    """List of filters to filter the search

    Attributes:
        filter_lines (Union[Unset, None, List['FilterLine']]):
    """

    filter_lines: Union[Unset, None, List["FilterLine"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        filter_lines: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filter_lines, Unset):
            if self.filter_lines is None:
                filter_lines = None
            else:
                filter_lines = []
                for filter_lines_item_data in self.filter_lines:
                    filter_lines_item = filter_lines_item_data.to_dict()

                    filter_lines.append(filter_lines_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if filter_lines is not UNSET:
            field_dict["filterLines"] = filter_lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.filter_line import FilterLine

        d = src_dict.copy()
        filter_lines = []
        _filter_lines = d.pop("filterLines", UNSET)
        for filter_lines_item_data in _filter_lines or []:
            filter_lines_item = FilterLine.from_dict(filter_lines_item_data)

            filter_lines.append(filter_lines_item)

        parts_filters = cls(
            filter_lines=filter_lines,
        )

        return parts_filters
