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


class SportRoundsAllResponseRateLimit(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            resets_in_seconds = schemas.NumberSchema
            remaining = schemas.NumberSchema
            requested_entity = schemas.StrSchema
            __annotations__ = {
                "resets_in_seconds": resets_in_seconds,
                "remaining": remaining,
                "requested_entity": requested_entity,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resets_in_seconds"]) -> MetaOapg.properties.resets_in_seconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remaining"]) -> MetaOapg.properties.remaining: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requested_entity"]) -> MetaOapg.properties.requested_entity: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resets_in_seconds", "remaining", "requested_entity", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resets_in_seconds"]) -> typing.Union[MetaOapg.properties.resets_in_seconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remaining"]) -> typing.Union[MetaOapg.properties.remaining, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requested_entity"]) -> typing.Union[MetaOapg.properties.requested_entity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resets_in_seconds", "remaining", "requested_entity", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        resets_in_seconds: typing.Union[MetaOapg.properties.resets_in_seconds, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        remaining: typing.Union[MetaOapg.properties.remaining, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        requested_entity: typing.Union[MetaOapg.properties.requested_entity, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportRoundsAllResponseRateLimit':
        return super().__new__(
            cls,
            *args,
            resets_in_seconds=resets_in_seconds,
            remaining=remaining,
            requested_entity=requested_entity,
            _configuration=_configuration,
            **kwargs,
        )
