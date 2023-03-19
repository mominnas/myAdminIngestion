from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterLine")


@attr.s(auto_attribs=True)
class FilterLine:
    """
    Attributes:
        filter_name (Union[Unset, None, str]): Available filters name: ThibertPartNumber, VendorPartNumber,
            WheelPartTypeID, Brand, Diameter, Width, BoltPattern, CenterBore, Offset, CategoryId, LastModificationDate
        filter_values (Union[Unset, None, List[str]]): Example of possible filter values (not exhaustive)
            <br />
            ThibertPartNumber: 081001, 00021, 00030, 00076
            <br />
            VendorPartNumber: 32571885114342731MM1, 49581, 8LTC49K
            <br />
            WheelPartTypeID: 00020, 00021, 00030, 00076
            <br />
            Brand: RTX, Ceco, Black Rhino ...
            <br />
            Diameter: 17, 18, 19 ...
            <br />
            Width: 6, 8, 9.5 ...
            <br />
            BoltPattern: 5x114.3, 6x132, 8x165.1 ...
            <br />
            CenterBore: 60.1, 108, 130.8
            <br />
            Offset: -13, 27, 52.5
            <br />
            CategoryId: 0360, 026 ...
            <br />
            LastModificationDate: 12/31/2023 Example: ['entry1', 'entry2', 'entry3'].
    """

    filter_name: Union[Unset, None, str] = UNSET
    filter_values: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        filter_name = self.filter_name
        filter_values: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.filter_values, Unset):
            if self.filter_values is None:
                filter_values = None
            else:
                filter_values = self.filter_values

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if filter_name is not UNSET:
            field_dict["filterName"] = filter_name
        if filter_values is not UNSET:
            field_dict["filterValues"] = filter_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filter_name = d.pop("filterName", UNSET)

        filter_values = cast(List[str], d.pop("filterValues", UNSET))

        filter_line = cls(
            filter_name=filter_name,
            filter_values=filter_values,
        )

        return filter_line
