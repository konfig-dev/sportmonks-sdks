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


class SportSchedulesByTeamIdResponseDataItemRoundsItem(
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
            stage_id = schemas.NumberSchema
            name = schemas.StrSchema
            finished = schemas.BoolSchema
            is_current = schemas.BoolSchema
            starting_at = schemas.StrSchema
            ending_at = schemas.StrSchema
        
            @staticmethod
            def fixtures() -> typing.Type['SportSchedulesByTeamIdResponseDataItemRoundsItemFixtures']:
                return SportSchedulesByTeamIdResponseDataItemRoundsItemFixtures
            __annotations__ = {
                "id": id,
                "sport_id": sport_id,
                "league_id": league_id,
                "season_id": season_id,
                "stage_id": stage_id,
                "name": name,
                "finished": finished,
                "is_current": is_current,
                "starting_at": starting_at,
                "ending_at": ending_at,
                "fixtures": fixtures,
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
    def __getitem__(self, name: typing_extensions.Literal["stage_id"]) -> MetaOapg.properties.stage_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finished"]) -> MetaOapg.properties.finished: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_current"]) -> MetaOapg.properties.is_current: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["starting_at"]) -> MetaOapg.properties.starting_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ending_at"]) -> MetaOapg.properties.ending_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fixtures"]) -> 'SportSchedulesByTeamIdResponseDataItemRoundsItemFixtures': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "league_id", "season_id", "stage_id", "name", "finished", "is_current", "starting_at", "ending_at", "fixtures", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["stage_id"]) -> typing.Union[MetaOapg.properties.stage_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finished"]) -> typing.Union[MetaOapg.properties.finished, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_current"]) -> typing.Union[MetaOapg.properties.is_current, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["starting_at"]) -> typing.Union[MetaOapg.properties.starting_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ending_at"]) -> typing.Union[MetaOapg.properties.ending_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fixtures"]) -> typing.Union['SportSchedulesByTeamIdResponseDataItemRoundsItemFixtures', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "league_id", "season_id", "stage_id", "name", "finished", "is_current", "starting_at", "ending_at", "fixtures", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sport_id: typing.Union[MetaOapg.properties.sport_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        league_id: typing.Union[MetaOapg.properties.league_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        season_id: typing.Union[MetaOapg.properties.season_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        stage_id: typing.Union[MetaOapg.properties.stage_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        finished: typing.Union[MetaOapg.properties.finished, bool, schemas.Unset] = schemas.unset,
        is_current: typing.Union[MetaOapg.properties.is_current, bool, schemas.Unset] = schemas.unset,
        starting_at: typing.Union[MetaOapg.properties.starting_at, str, schemas.Unset] = schemas.unset,
        ending_at: typing.Union[MetaOapg.properties.ending_at, str, schemas.Unset] = schemas.unset,
        fixtures: typing.Union['SportSchedulesByTeamIdResponseDataItemRoundsItemFixtures', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportSchedulesByTeamIdResponseDataItemRoundsItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            sport_id=sport_id,
            league_id=league_id,
            season_id=season_id,
            stage_id=stage_id,
            name=name,
            finished=finished,
            is_current=is_current,
            starting_at=starting_at,
            ending_at=ending_at,
            fixtures=fixtures,
            _configuration=_configuration,
            **kwargs,
        )

from sportmonks.model.sport_schedules_by_team_id_response_data_item_rounds_item_fixtures import SportSchedulesByTeamIdResponseDataItemRoundsItemFixtures
