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


class SportLeaguesByDateResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.NumberSchema
            sport_id = schemas.NumberSchema
            country_id = schemas.NumberSchema
            name = schemas.StrSchema
            active = schemas.BoolSchema
            short_code = schemas.StrSchema
            image_path = schemas.StrSchema
            type = schemas.StrSchema
            sub_type = schemas.StrSchema
            last_played_at = schemas.StrSchema
            category = schemas.NumberSchema
            has_jerseys = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "sport_id": sport_id,
                "country_id": country_id,
                "name": name,
                "active": active,
                "short_code": short_code,
                "image_path": image_path,
                "type": type,
                "sub_type": sub_type,
                "last_played_at": last_played_at,
                "category": category,
                "has_jerseys": has_jerseys,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sport_id"]) -> MetaOapg.properties.sport_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_id"]) -> MetaOapg.properties.country_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["short_code"]) -> MetaOapg.properties.short_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_path"]) -> MetaOapg.properties.image_path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sub_type"]) -> MetaOapg.properties.sub_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_played_at"]) -> MetaOapg.properties.last_played_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_jerseys"]) -> MetaOapg.properties.has_jerseys: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "country_id", "name", "active", "short_code", "image_path", "type", "sub_type", "last_played_at", "category", "has_jerseys", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sport_id"]) -> typing.Union[MetaOapg.properties.sport_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_id"]) -> typing.Union[MetaOapg.properties.country_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["short_code"]) -> typing.Union[MetaOapg.properties.short_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_path"]) -> typing.Union[MetaOapg.properties.image_path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sub_type"]) -> typing.Union[MetaOapg.properties.sub_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_played_at"]) -> typing.Union[MetaOapg.properties.last_played_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_jerseys"]) -> typing.Union[MetaOapg.properties.has_jerseys, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "country_id", "name", "active", "short_code", "image_path", "type", "sub_type", "last_played_at", "category", "has_jerseys", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sport_id: typing.Union[MetaOapg.properties.sport_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        country_id: typing.Union[MetaOapg.properties.country_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        short_code: typing.Union[MetaOapg.properties.short_code, str, schemas.Unset] = schemas.unset,
        image_path: typing.Union[MetaOapg.properties.image_path, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        sub_type: typing.Union[MetaOapg.properties.sub_type, str, schemas.Unset] = schemas.unset,
        last_played_at: typing.Union[MetaOapg.properties.last_played_at, str, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        has_jerseys: typing.Union[MetaOapg.properties.has_jerseys, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportLeaguesByDateResponseDataItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            sport_id=sport_id,
            country_id=country_id,
            name=name,
            active=active,
            short_code=short_code,
            image_path=image_path,
            type=type,
            sub_type=sub_type,
            last_played_at=last_played_at,
            category=category,
            has_jerseys=has_jerseys,
            _configuration=_configuration,
            **kwargs,
        )
