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


class SportTransferByIdResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.NumberSchema
            sport_id = schemas.NumberSchema
            player_id = schemas.NumberSchema
            type_id = schemas.NumberSchema
            from_team_id = schemas.NumberSchema
            to_team_id = schemas.NumberSchema
            position_id = schemas.NumberSchema
            detailed_position_id = schemas.NumberSchema
            date = schemas.StrSchema
            career_ended = schemas.BoolSchema
            completed = schemas.BoolSchema
            completed_at = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "sport_id": sport_id,
                "player_id": player_id,
                "type_id": type_id,
                "from_team_id": from_team_id,
                "to_team_id": to_team_id,
                "position_id": position_id,
                "detailed_position_id": detailed_position_id,
                "date": date,
                "career_ended": career_ended,
                "completed": completed,
                "completed_at": completed_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sport_id"]) -> MetaOapg.properties.sport_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["player_id"]) -> MetaOapg.properties.player_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type_id"]) -> MetaOapg.properties.type_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from_team_id"]) -> MetaOapg.properties.from_team_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_team_id"]) -> MetaOapg.properties.to_team_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position_id"]) -> MetaOapg.properties.position_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detailed_position_id"]) -> MetaOapg.properties.detailed_position_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["career_ended"]) -> MetaOapg.properties.career_ended: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completed"]) -> MetaOapg.properties.completed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completed_at"]) -> MetaOapg.properties.completed_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "player_id", "type_id", "from_team_id", "to_team_id", "position_id", "detailed_position_id", "date", "career_ended", "completed", "completed_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sport_id"]) -> typing.Union[MetaOapg.properties.sport_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["player_id"]) -> typing.Union[MetaOapg.properties.player_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type_id"]) -> typing.Union[MetaOapg.properties.type_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from_team_id"]) -> typing.Union[MetaOapg.properties.from_team_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_team_id"]) -> typing.Union[MetaOapg.properties.to_team_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position_id"]) -> typing.Union[MetaOapg.properties.position_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detailed_position_id"]) -> typing.Union[MetaOapg.properties.detailed_position_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["career_ended"]) -> typing.Union[MetaOapg.properties.career_ended, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completed"]) -> typing.Union[MetaOapg.properties.completed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completed_at"]) -> typing.Union[MetaOapg.properties.completed_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "player_id", "type_id", "from_team_id", "to_team_id", "position_id", "detailed_position_id", "date", "career_ended", "completed", "completed_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sport_id: typing.Union[MetaOapg.properties.sport_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        player_id: typing.Union[MetaOapg.properties.player_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        type_id: typing.Union[MetaOapg.properties.type_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        from_team_id: typing.Union[MetaOapg.properties.from_team_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        to_team_id: typing.Union[MetaOapg.properties.to_team_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        position_id: typing.Union[MetaOapg.properties.position_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        detailed_position_id: typing.Union[MetaOapg.properties.detailed_position_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, schemas.Unset] = schemas.unset,
        career_ended: typing.Union[MetaOapg.properties.career_ended, bool, schemas.Unset] = schemas.unset,
        completed: typing.Union[MetaOapg.properties.completed, bool, schemas.Unset] = schemas.unset,
        completed_at: typing.Union[MetaOapg.properties.completed_at, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportTransferByIdResponseData':
        return super().__new__(
            cls,
            *args,
            id=id,
            sport_id=sport_id,
            player_id=player_id,
            type_id=type_id,
            from_team_id=from_team_id,
            to_team_id=to_team_id,
            position_id=position_id,
            detailed_position_id=detailed_position_id,
            date=date,
            career_ended=career_ended,
            completed=completed,
            completed_at=completed_at,
            _configuration=_configuration,
            **kwargs,
        )
