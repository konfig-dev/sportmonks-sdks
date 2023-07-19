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


class SportTopScorersBySeasonIdResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            season_id = schemas.NumberSchema
            player_id = schemas.NumberSchema
            type_id = schemas.NumberSchema
            team_id = schemas.NumberSchema
            position = schemas.NumberSchema
            total = schemas.NumberSchema
            
            
            class points(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'points':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "season_id": season_id,
                "player_id": player_id,
                "type_id": type_id,
                "team_id": team_id,
                "position": position,
                "total": total,
                "points": points,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["season_id"]) -> MetaOapg.properties.season_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["player_id"]) -> MetaOapg.properties.player_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type_id"]) -> MetaOapg.properties.type_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team_id"]) -> MetaOapg.properties.team_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["points"]) -> MetaOapg.properties.points: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["season_id", "player_id", "type_id", "team_id", "position", "total", "points", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["season_id"]) -> typing.Union[MetaOapg.properties.season_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["player_id"]) -> typing.Union[MetaOapg.properties.player_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type_id"]) -> typing.Union[MetaOapg.properties.type_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team_id"]) -> typing.Union[MetaOapg.properties.team_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> typing.Union[MetaOapg.properties.position, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["points"]) -> typing.Union[MetaOapg.properties.points, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["season_id", "player_id", "type_id", "team_id", "position", "total", "points", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        season_id: typing.Union[MetaOapg.properties.season_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        player_id: typing.Union[MetaOapg.properties.player_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        type_id: typing.Union[MetaOapg.properties.type_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        team_id: typing.Union[MetaOapg.properties.team_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        position: typing.Union[MetaOapg.properties.position, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        points: typing.Union[MetaOapg.properties.points, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportTopScorersBySeasonIdResponseDataItem':
        return super().__new__(
            cls,
            *args,
            season_id=season_id,
            player_id=player_id,
            type_id=type_id,
            team_id=team_id,
            position=position,
            total=total,
            points=points,
            _configuration=_configuration,
            **kwargs,
        )
