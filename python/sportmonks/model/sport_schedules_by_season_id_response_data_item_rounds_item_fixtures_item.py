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


class SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItem(
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
            
            
            class group_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'group_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class aggregate_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'aggregate_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            round_id = schemas.NumberSchema
            state_id = schemas.NumberSchema
            venue_id = schemas.NumberSchema
            name = schemas.StrSchema
            
            
            class home_score(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'home_score':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class away_score(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'away_score':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            starting_at = schemas.StrSchema
            
            
            class result_info(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'result_info':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            leg = schemas.StrSchema
            
            
            class details(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'details':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            length = schemas.NumberSchema
            placeholder = schemas.BoolSchema
            
            
            class last_processed_at(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'last_processed_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            starting_at_timestamp = schemas.NumberSchema
        
            @staticmethod
            def participants() -> typing.Type['SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipants']:
                return SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipants
            __annotations__ = {
                "id": id,
                "sport_id": sport_id,
                "league_id": league_id,
                "season_id": season_id,
                "stage_id": stage_id,
                "group_id": group_id,
                "aggregate_id": aggregate_id,
                "round_id": round_id,
                "state_id": state_id,
                "venue_id": venue_id,
                "name": name,
                "home_score": home_score,
                "away_score": away_score,
                "starting_at": starting_at,
                "result_info": result_info,
                "leg": leg,
                "details": details,
                "length": length,
                "placeholder": placeholder,
                "last_processed_at": last_processed_at,
                "starting_at_timestamp": starting_at_timestamp,
                "participants": participants,
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
    def __getitem__(self, name: typing_extensions.Literal["group_id"]) -> MetaOapg.properties.group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["aggregate_id"]) -> MetaOapg.properties.aggregate_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["round_id"]) -> MetaOapg.properties.round_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state_id"]) -> MetaOapg.properties.state_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["venue_id"]) -> MetaOapg.properties.venue_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["home_score"]) -> MetaOapg.properties.home_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["away_score"]) -> MetaOapg.properties.away_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["starting_at"]) -> MetaOapg.properties.starting_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result_info"]) -> MetaOapg.properties.result_info: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["leg"]) -> MetaOapg.properties.leg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["length"]) -> MetaOapg.properties.length: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["placeholder"]) -> MetaOapg.properties.placeholder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_processed_at"]) -> MetaOapg.properties.last_processed_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["starting_at_timestamp"]) -> MetaOapg.properties.starting_at_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["participants"]) -> 'SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipants': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "league_id", "season_id", "stage_id", "group_id", "aggregate_id", "round_id", "state_id", "venue_id", "name", "home_score", "away_score", "starting_at", "result_info", "leg", "details", "length", "placeholder", "last_processed_at", "starting_at_timestamp", "participants", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["group_id"]) -> typing.Union[MetaOapg.properties.group_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["aggregate_id"]) -> typing.Union[MetaOapg.properties.aggregate_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["round_id"]) -> typing.Union[MetaOapg.properties.round_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state_id"]) -> typing.Union[MetaOapg.properties.state_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["venue_id"]) -> typing.Union[MetaOapg.properties.venue_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["home_score"]) -> typing.Union[MetaOapg.properties.home_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["away_score"]) -> typing.Union[MetaOapg.properties.away_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["starting_at"]) -> typing.Union[MetaOapg.properties.starting_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result_info"]) -> typing.Union[MetaOapg.properties.result_info, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["leg"]) -> typing.Union[MetaOapg.properties.leg, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union[MetaOapg.properties.details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["length"]) -> typing.Union[MetaOapg.properties.length, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["placeholder"]) -> typing.Union[MetaOapg.properties.placeholder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_processed_at"]) -> typing.Union[MetaOapg.properties.last_processed_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["starting_at_timestamp"]) -> typing.Union[MetaOapg.properties.starting_at_timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["participants"]) -> typing.Union['SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipants', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "league_id", "season_id", "stage_id", "group_id", "aggregate_id", "round_id", "state_id", "venue_id", "name", "home_score", "away_score", "starting_at", "result_info", "leg", "details", "length", "placeholder", "last_processed_at", "starting_at_timestamp", "participants", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sport_id: typing.Union[MetaOapg.properties.sport_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        league_id: typing.Union[MetaOapg.properties.league_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        season_id: typing.Union[MetaOapg.properties.season_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        stage_id: typing.Union[MetaOapg.properties.stage_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        group_id: typing.Union[MetaOapg.properties.group_id, None, str, schemas.Unset] = schemas.unset,
        aggregate_id: typing.Union[MetaOapg.properties.aggregate_id, None, str, schemas.Unset] = schemas.unset,
        round_id: typing.Union[MetaOapg.properties.round_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        state_id: typing.Union[MetaOapg.properties.state_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        venue_id: typing.Union[MetaOapg.properties.venue_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        home_score: typing.Union[MetaOapg.properties.home_score, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        away_score: typing.Union[MetaOapg.properties.away_score, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        starting_at: typing.Union[MetaOapg.properties.starting_at, str, schemas.Unset] = schemas.unset,
        result_info: typing.Union[MetaOapg.properties.result_info, None, str, schemas.Unset] = schemas.unset,
        leg: typing.Union[MetaOapg.properties.leg, str, schemas.Unset] = schemas.unset,
        details: typing.Union[MetaOapg.properties.details, None, str, schemas.Unset] = schemas.unset,
        length: typing.Union[MetaOapg.properties.length, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        placeholder: typing.Union[MetaOapg.properties.placeholder, bool, schemas.Unset] = schemas.unset,
        last_processed_at: typing.Union[MetaOapg.properties.last_processed_at, None, str, schemas.Unset] = schemas.unset,
        starting_at_timestamp: typing.Union[MetaOapg.properties.starting_at_timestamp, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        participants: typing.Union['SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipants', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            sport_id=sport_id,
            league_id=league_id,
            season_id=season_id,
            stage_id=stage_id,
            group_id=group_id,
            aggregate_id=aggregate_id,
            round_id=round_id,
            state_id=state_id,
            venue_id=venue_id,
            name=name,
            home_score=home_score,
            away_score=away_score,
            starting_at=starting_at,
            result_info=result_info,
            leg=leg,
            details=details,
            length=length,
            placeholder=placeholder,
            last_processed_at=last_processed_at,
            starting_at_timestamp=starting_at_timestamp,
            participants=participants,
            _configuration=_configuration,
            **kwargs,
        )

from sportmonks.model.sport_schedules_by_season_id_response_data_item_rounds_item_fixtures_item_participants import SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipants
