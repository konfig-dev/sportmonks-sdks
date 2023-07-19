# coding: utf-8

"""
    SportMonks

    Surpass the competition with superior sports data

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal

from sportmonks.type.sport_schedules_by_season_id_response_data_item_aggregates import SportSchedulesBySeasonIdResponseDataItemAggregates
from sportmonks.type.sport_schedules_by_season_id_response_data_item_rounds import SportSchedulesBySeasonIdResponseDataItemRounds

class RequiredSportSchedulesBySeasonIdResponseDataItem(TypedDict):
    pass

class OptionalSportSchedulesBySeasonIdResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    sport_id: typing.Union[int, float]

    league_id: typing.Union[int, float]

    season_id: typing.Union[int, float]

    type_id: typing.Union[int, float]

    name: str

    sort_order: typing.Union[int, float]

    finished: bool

    is_current: bool

    starting_at: str

    ending_at: str

    rounds: SportSchedulesBySeasonIdResponseDataItemRounds

    aggregates: SportSchedulesBySeasonIdResponseDataItemAggregates

class SportSchedulesBySeasonIdResponseDataItem(RequiredSportSchedulesBySeasonIdResponseDataItem, OptionalSportSchedulesBySeasonIdResponseDataItem):
    pass
