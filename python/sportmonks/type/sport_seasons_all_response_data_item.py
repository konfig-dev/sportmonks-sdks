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


class RequiredSportSeasonsAllResponseDataItem(TypedDict):
    pass

class OptionalSportSeasonsAllResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    sport_id: typing.Union[int, float]

    league_id: typing.Union[int, float]

    tie_breaker_rule_id: typing.Union[int, float]

    name: str

    finished: bool

    pending: bool

    is_current: bool

    starting_at: str

    ending_at: typing.Optional[str]

    standings_recalculated_at: str

class SportSeasonsAllResponseDataItem(RequiredSportSeasonsAllResponseDataItem, OptionalSportSeasonsAllResponseDataItem):
    pass
