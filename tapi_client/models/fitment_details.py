from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FitmentDetails")


@attr.s(auto_attribs=True)
class FitmentDetails:
    """
    Attributes:
        thibert_part_number (Union[Unset, None, str]): Thibert part number associated with this item.
        is_direct_fit (Union[Unset, bool]): Indicates if the wheel is a direct fit for the vehicle
        is_direct_fit_image (Union[Unset, None, str]): Icon used to indicates when a wheel is a Direct Fit for the
            vehicle
        is_hub_centric (Union[Unset, bool]): Indicates if the wheel is hub centric for the vehicle
        is_hub_centric_image (Union[Unset, None, str]): Icon used to indicates when a wheel is hub centric for the
            vehicle
        is_oem_compatible (Union[Unset, bool]): Indicates if the wheel is OEM compatible for the vehicle
        is_oem_compatible_image (Union[Unset, None, str]): Icon used to indicates when a wheel is OEM compatible for the
            vehicle
        is_winter_approved (Union[Unset, bool]): Indicates if the wheel is winter approuved
        is_winter_approved_image (Union[Unset, None, str]): Icon used to indicates when a wheel is winter approuved
        is_staggered (Union[Unset, bool]): Indicates if the wheel is staggered for the vehicle
        is_staggered_image (Union[Unset, None, str]): Icon used to indicates when a wheel is staggered for the vehicle
        is_valve_included (Union[Unset, bool]): Indicates if the valve is included with this wheel
    """

    thibert_part_number: Union[Unset, None, str] = UNSET
    is_direct_fit: Union[Unset, bool] = UNSET
    is_direct_fit_image: Union[Unset, None, str] = UNSET
    is_hub_centric: Union[Unset, bool] = UNSET
    is_hub_centric_image: Union[Unset, None, str] = UNSET
    is_oem_compatible: Union[Unset, bool] = UNSET
    is_oem_compatible_image: Union[Unset, None, str] = UNSET
    is_winter_approved: Union[Unset, bool] = UNSET
    is_winter_approved_image: Union[Unset, None, str] = UNSET
    is_staggered: Union[Unset, bool] = UNSET
    is_staggered_image: Union[Unset, None, str] = UNSET
    is_valve_included: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        thibert_part_number = self.thibert_part_number
        is_direct_fit = self.is_direct_fit
        is_direct_fit_image = self.is_direct_fit_image
        is_hub_centric = self.is_hub_centric
        is_hub_centric_image = self.is_hub_centric_image
        is_oem_compatible = self.is_oem_compatible
        is_oem_compatible_image = self.is_oem_compatible_image
        is_winter_approved = self.is_winter_approved
        is_winter_approved_image = self.is_winter_approved_image
        is_staggered = self.is_staggered
        is_staggered_image = self.is_staggered_image
        is_valve_included = self.is_valve_included

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if thibert_part_number is not UNSET:
            field_dict["thibertPartNumber"] = thibert_part_number
        if is_direct_fit is not UNSET:
            field_dict["isDirectFit"] = is_direct_fit
        if is_direct_fit_image is not UNSET:
            field_dict["isDirectFitImage"] = is_direct_fit_image
        if is_hub_centric is not UNSET:
            field_dict["isHubCentric"] = is_hub_centric
        if is_hub_centric_image is not UNSET:
            field_dict["isHubCentricImage"] = is_hub_centric_image
        if is_oem_compatible is not UNSET:
            field_dict["isOEMCompatible"] = is_oem_compatible
        if is_oem_compatible_image is not UNSET:
            field_dict["isOEMCompatibleImage"] = is_oem_compatible_image
        if is_winter_approved is not UNSET:
            field_dict["isWinterApproved"] = is_winter_approved
        if is_winter_approved_image is not UNSET:
            field_dict["isWinterApprovedImage"] = is_winter_approved_image
        if is_staggered is not UNSET:
            field_dict["isStaggered"] = is_staggered
        if is_staggered_image is not UNSET:
            field_dict["isStaggeredImage"] = is_staggered_image
        if is_valve_included is not UNSET:
            field_dict["isValveIncluded"] = is_valve_included

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        thibert_part_number = d.pop("thibertPartNumber", UNSET)

        is_direct_fit = d.pop("isDirectFit", UNSET)

        is_direct_fit_image = d.pop("isDirectFitImage", UNSET)

        is_hub_centric = d.pop("isHubCentric", UNSET)

        is_hub_centric_image = d.pop("isHubCentricImage", UNSET)

        is_oem_compatible = d.pop("isOEMCompatible", UNSET)

        is_oem_compatible_image = d.pop("isOEMCompatibleImage", UNSET)

        is_winter_approved = d.pop("isWinterApproved", UNSET)

        is_winter_approved_image = d.pop("isWinterApprovedImage", UNSET)

        is_staggered = d.pop("isStaggered", UNSET)

        is_staggered_image = d.pop("isStaggeredImage", UNSET)

        is_valve_included = d.pop("isValveIncluded", UNSET)

        fitment_details = cls(
            thibert_part_number=thibert_part_number,
            is_direct_fit=is_direct_fit,
            is_direct_fit_image=is_direct_fit_image,
            is_hub_centric=is_hub_centric,
            is_hub_centric_image=is_hub_centric_image,
            is_oem_compatible=is_oem_compatible,
            is_oem_compatible_image=is_oem_compatible_image,
            is_winter_approved=is_winter_approved,
            is_winter_approved_image=is_winter_approved_image,
            is_staggered=is_staggered,
            is_staggered_image=is_staggered_image,
            is_valve_included=is_valve_included,
        )

        return fitment_details
