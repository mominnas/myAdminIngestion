from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Image")


@attr.s(auto_attribs=True)
class Image:
    """Model representing an image of an item.

    Attributes:
        thibert_part_number (Union[Unset, None, str]): Part number of the item associated with this image.
        image_url (Union[Unset, None, str]): URL of where the image is hosted and can be retrived.
        image_type (Union[Unset, None, str]): Type of the image.
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    image_url: Union[Unset, None, str] = UNSET
    image_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        image_url = self.image_url
        image_type = self.image_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if image_url is not UNSET:
            field_dict["imageURL"] = image_url
        if image_type is not UNSET:
            field_dict["imageType"] = image_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        image_url = d.pop("imageURL", UNSET)

        image_type = d.pop("imageType", UNSET)

        image = cls(
            thibert_part_number=thibert_part_number,
            image_url=image_url,
            image_type=image_type,
        )

        return image
