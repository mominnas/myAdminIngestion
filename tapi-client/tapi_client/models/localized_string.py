from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalizedString")


@attr.s(auto_attribs=True)
class LocalizedString:
    """
    Attributes:
        language_code (Union[Unset, None, str]):  Example: EN.
        localized_value (Union[Unset, None, str]):
    """

    language_code: Union[Unset, None, str] = UNSET
    localized_value: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        language_code = self.language_code
        localized_value = self.localized_value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if localized_value is not UNSET:
            field_dict["localizedValue"] = localized_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language_code = d.pop("languageCode", UNSET)

        localized_value = d.pop("localizedValue", UNSET)

        localized_string = cls(
            language_code=language_code,
            localized_value=localized_value,
        )

        return localized_string
