from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PricesByCurrencies")


@attr.s(auto_attribs=True)
class PricesByCurrencies:
    """
    Attributes:
        currency_code (Union[Unset, None, str]):
        price_value (Union[Unset, float]):
    """

    currency_code: Union[Unset, None, str] = UNSET
    price_value: Union[Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        currency_code = self.currency_code
        price_value = self.price_value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if currency_code is not UNSET:
            field_dict["currencyCode"] = currency_code
        if price_value is not UNSET:
            field_dict["priceValue"] = price_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency_code = d.pop("currencyCode", UNSET)

        price_value = d.pop("priceValue", UNSET)

        prices_by_currencies = cls(
            currency_code=currency_code,
            price_value=price_value,
        )

        return prices_by_currencies
