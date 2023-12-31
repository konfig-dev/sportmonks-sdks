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


class RequiredSportLivescoresAllInPlayResponseDataItem(TypedDict):
    pass

class OptionalSportLivescoresAllInPlayResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    sport_id: typing.Union[int, float]

    league_id: typing.Union[int, float]

    season_id: typing.Union[int, float]

    stage_id: typing.Union[int, float]

    group_id: typing.Optional[str]

    aggregate_id: typing.Optional[str]

    round_id: typing.Union[int, float]

    state_id: typing.Union[int, float]

    venue_id: typing.Union[int, float]

    name: str

    home_score: typing.Union[int, float]

    away_score: typing.Union[int, float]

    starting_at: str

    result_info: typing.Optional[str]

    leg: str

    details: typing.Optional[str]

    length: typing.Union[int, float]

    placeholder: bool

    last_processed_at: str

    starting_at_timestamp: typing.Union[int, float]

class SportLivescoresAllInPlayResponseDataItem(RequiredSportLivescoresAllInPlayResponseDataItem, OptionalSportLivescoresAllInPlayResponseDataItem):
    pass
