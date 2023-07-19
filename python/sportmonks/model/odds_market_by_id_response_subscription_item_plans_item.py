# coding: utf-8

"""
    SportMonks

    Surpass the competition with superior sports data

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sportmonks import schemas  # noqa: F401


class OddsMarketByIdResponseSubscriptionItemPlansItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            plan = schemas.StrSchema
            sport = schemas.StrSchema
            category = schemas.StrSchema
            __annotations__ = {
                "plan": plan,
                "sport": sport,
                "category": category,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plan"]) -> MetaOapg.properties.plan: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sport"]) -> MetaOapg.properties.sport: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["plan", "sport", "category", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plan"]) -> typing.Union[MetaOapg.properties.plan, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sport"]) -> typing.Union[MetaOapg.properties.sport, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["plan", "sport", "category", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        plan: typing.Union[MetaOapg.properties.plan, str, schemas.Unset] = schemas.unset,
        sport: typing.Union[MetaOapg.properties.sport, str, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OddsMarketByIdResponseSubscriptionItemPlansItem':
        return super().__new__(
            cls,
            *args,
            plan=plan,
            sport=sport,
            category=category,
            _configuration=_configuration,
            **kwargs,
        )
