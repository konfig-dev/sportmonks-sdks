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


class OddsBookmakersSearchResponsePagination(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            count = schemas.NumberSchema
            per_page = schemas.NumberSchema
            current_page = schemas.NumberSchema
            
            
            class next_page(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'next_page':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            has_more = schemas.BoolSchema
            __annotations__ = {
                "count": count,
                "per_page": per_page,
                "current_page": current_page,
                "next_page": next_page,
                "has_more": has_more,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["per_page"]) -> MetaOapg.properties.per_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_page"]) -> MetaOapg.properties.current_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_page"]) -> MetaOapg.properties.next_page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_more"]) -> MetaOapg.properties.has_more: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["count", "per_page", "current_page", "next_page", "has_more", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["per_page"]) -> typing.Union[MetaOapg.properties.per_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_page"]) -> typing.Union[MetaOapg.properties.current_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_page"]) -> typing.Union[MetaOapg.properties.next_page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_more"]) -> typing.Union[MetaOapg.properties.has_more, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["count", "per_page", "current_page", "next_page", "has_more", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        per_page: typing.Union[MetaOapg.properties.per_page, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        current_page: typing.Union[MetaOapg.properties.current_page, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        next_page: typing.Union[MetaOapg.properties.next_page, None, str, schemas.Unset] = schemas.unset,
        has_more: typing.Union[MetaOapg.properties.has_more, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OddsBookmakersSearchResponsePagination':
        return super().__new__(
            cls,
            *args,
            count=count,
            per_page=per_page,
            current_page=current_page,
            next_page=next_page,
            has_more=has_more,
            _configuration=_configuration,
            **kwargs,
        )
