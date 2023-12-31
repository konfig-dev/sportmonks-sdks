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


class SportTeamsBySeasonIdResponseDataItem(
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
            venue_id = schemas.NumberSchema
            gender = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class short_code(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'short_code':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            image_path = schemas.StrSchema
            founded = schemas.NumberSchema
            type = schemas.StrSchema
            placeholder = schemas.BoolSchema
            last_played_at = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "sport_id": sport_id,
                "country_id": country_id,
                "venue_id": venue_id,
                "gender": gender,
                "name": name,
                "short_code": short_code,
                "image_path": image_path,
                "founded": founded,
                "type": type,
                "placeholder": placeholder,
                "last_played_at": last_played_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sport_id"]) -> MetaOapg.properties.sport_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_id"]) -> MetaOapg.properties.country_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["venue_id"]) -> MetaOapg.properties.venue_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["short_code"]) -> MetaOapg.properties.short_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_path"]) -> MetaOapg.properties.image_path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["founded"]) -> MetaOapg.properties.founded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["placeholder"]) -> MetaOapg.properties.placeholder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_played_at"]) -> MetaOapg.properties.last_played_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "country_id", "venue_id", "gender", "name", "short_code", "image_path", "founded", "type", "placeholder", "last_played_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sport_id"]) -> typing.Union[MetaOapg.properties.sport_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_id"]) -> typing.Union[MetaOapg.properties.country_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["venue_id"]) -> typing.Union[MetaOapg.properties.venue_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> typing.Union[MetaOapg.properties.gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["short_code"]) -> typing.Union[MetaOapg.properties.short_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_path"]) -> typing.Union[MetaOapg.properties.image_path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["founded"]) -> typing.Union[MetaOapg.properties.founded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["placeholder"]) -> typing.Union[MetaOapg.properties.placeholder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_played_at"]) -> typing.Union[MetaOapg.properties.last_played_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "country_id", "venue_id", "gender", "name", "short_code", "image_path", "founded", "type", "placeholder", "last_played_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sport_id: typing.Union[MetaOapg.properties.sport_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        country_id: typing.Union[MetaOapg.properties.country_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        venue_id: typing.Union[MetaOapg.properties.venue_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        gender: typing.Union[MetaOapg.properties.gender, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        short_code: typing.Union[MetaOapg.properties.short_code, None, str, schemas.Unset] = schemas.unset,
        image_path: typing.Union[MetaOapg.properties.image_path, str, schemas.Unset] = schemas.unset,
        founded: typing.Union[MetaOapg.properties.founded, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        placeholder: typing.Union[MetaOapg.properties.placeholder, bool, schemas.Unset] = schemas.unset,
        last_played_at: typing.Union[MetaOapg.properties.last_played_at, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportTeamsBySeasonIdResponseDataItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            sport_id=sport_id,
            country_id=country_id,
            venue_id=venue_id,
            gender=gender,
            name=name,
            short_code=short_code,
            image_path=image_path,
            founded=founded,
            type=type,
            placeholder=placeholder,
            last_played_at=last_played_at,
            _configuration=_configuration,
            **kwargs,
        )
