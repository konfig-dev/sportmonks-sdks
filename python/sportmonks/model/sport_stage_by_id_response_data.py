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


class SportStageByIdResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.NumberSchema
            sport_id = schemas.NumberSchema
            league_id = schemas.NumberSchema
            season_id = schemas.NumberSchema
            type_id = schemas.NumberSchema
            name = schemas.StrSchema
            
            
            class sort_order(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sort_order':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            finished = schemas.BoolSchema
            is_current = schemas.BoolSchema
            
            
            class starting_at(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'starting_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ending_at(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ending_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "sport_id": sport_id,
                "league_id": league_id,
                "season_id": season_id,
                "type_id": type_id,
                "name": name,
                "sort_order": sort_order,
                "finished": finished,
                "is_current": is_current,
                "starting_at": starting_at,
                "ending_at": ending_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sport_id"]) -> MetaOapg.properties.sport_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["league_id"]) -> MetaOapg.properties.league_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["season_id"]) -> MetaOapg.properties.season_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type_id"]) -> MetaOapg.properties.type_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort_order"]) -> MetaOapg.properties.sort_order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finished"]) -> MetaOapg.properties.finished: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_current"]) -> MetaOapg.properties.is_current: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["starting_at"]) -> MetaOapg.properties.starting_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ending_at"]) -> MetaOapg.properties.ending_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "league_id", "season_id", "type_id", "name", "sort_order", "finished", "is_current", "starting_at", "ending_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sport_id"]) -> typing.Union[MetaOapg.properties.sport_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["league_id"]) -> typing.Union[MetaOapg.properties.league_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["season_id"]) -> typing.Union[MetaOapg.properties.season_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type_id"]) -> typing.Union[MetaOapg.properties.type_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort_order"]) -> typing.Union[MetaOapg.properties.sort_order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finished"]) -> typing.Union[MetaOapg.properties.finished, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_current"]) -> typing.Union[MetaOapg.properties.is_current, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["starting_at"]) -> typing.Union[MetaOapg.properties.starting_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ending_at"]) -> typing.Union[MetaOapg.properties.ending_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "league_id", "season_id", "type_id", "name", "sort_order", "finished", "is_current", "starting_at", "ending_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sport_id: typing.Union[MetaOapg.properties.sport_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        league_id: typing.Union[MetaOapg.properties.league_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        season_id: typing.Union[MetaOapg.properties.season_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        type_id: typing.Union[MetaOapg.properties.type_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        sort_order: typing.Union[MetaOapg.properties.sort_order, None, str, schemas.Unset] = schemas.unset,
        finished: typing.Union[MetaOapg.properties.finished, bool, schemas.Unset] = schemas.unset,
        is_current: typing.Union[MetaOapg.properties.is_current, bool, schemas.Unset] = schemas.unset,
        starting_at: typing.Union[MetaOapg.properties.starting_at, None, str, schemas.Unset] = schemas.unset,
        ending_at: typing.Union[MetaOapg.properties.ending_at, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportStageByIdResponseData':
        return super().__new__(
            cls,
            *args,
            id=id,
            sport_id=sport_id,
            league_id=league_id,
            season_id=season_id,
            type_id=type_id,
            name=name,
            sort_order=sort_order,
            finished=finished,
            is_current=is_current,
            starting_at=starting_at,
            ending_at=ending_at,
            _configuration=_configuration,
            **kwargs,
        )
