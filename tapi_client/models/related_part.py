from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image import Image
    from ..models.localized_string import LocalizedString


T = TypeVar("T", bound="RelatedPart")


@attr.s(auto_attribs=True)
class RelatedPart:
    """
    Attributes:
        thibert_part_number (Union[Unset, None, str]): Part number of the part Example: 082025.
        reference_thibert_part_number (Union[Unset, None, str]): Part number of the related part Example: TR413C.
        titles (Union[Unset, None, List['LocalizedString']]): Titles of the related part.
        reference_type (Union[Unset, None, List['LocalizedString']]): Short description of this item.
        images (Union[Unset, None, List['Image']]): List of all images associated with this related part.
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    reference_thibert_part_number: Union[Unset, None, str] = UNSET
    titles: Union[Unset, None, List["LocalizedString"]] = UNSET
    reference_type: Union[Unset, None, List["LocalizedString"]] = UNSET
    images: Union[Unset, None, List["Image"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        reference_thibert_part_number = self.reference_thibert_part_number
        titles: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.titles, Unset):
            if self.titles is None:
                titles = None
            else:
                titles = []
                for titles_item_data in self.titles:
                    titles_item = titles_item_data.to_dict()

                    titles.append(titles_item)

        reference_type: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.reference_type, Unset):
            if self.reference_type is None:
                reference_type = None
            else:
                reference_type = []
                for reference_type_item_data in self.reference_type:
                    reference_type_item = reference_type_item_data.to_dict()

                    reference_type.append(reference_type_item)

        images: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            if self.images is None:
                images = None
            else:
                images = []
                for images_item_data in self.images:
                    images_item = images_item_data.to_dict()

                    images.append(images_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if reference_thibert_part_number is not UNSET:
            field_dict["referenceThibertPartNumber"] = reference_thibert_part_number
        if titles is not UNSET:
            field_dict["titles"] = titles
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image import Image
        from ..models.localized_string import LocalizedString

        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        reference_thibert_part_number = d.pop("referenceThibertPartNumber", UNSET)

        titles = []
        _titles = d.pop("titles", UNSET)
        for titles_item_data in _titles or []:
            titles_item = LocalizedString.from_dict(titles_item_data)

            titles.append(titles_item)

        reference_type = []
        _reference_type = d.pop("referenceType", UNSET)
        for reference_type_item_data in _reference_type or []:
            reference_type_item = LocalizedString.from_dict(reference_type_item_data)

            reference_type.append(reference_type_item)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = Image.from_dict(images_item_data)

            images.append(images_item)

        related_part = cls(
            thibert_part_number=thibert_part_number,
            reference_thibert_part_number=reference_thibert_part_number,
            titles=titles,
            reference_type=reference_type,
            images=images,
        )

        return related_part
