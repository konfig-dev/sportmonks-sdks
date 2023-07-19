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


class RequiredSportOddsPreMatchByFixtureAndBookmakerIdResponseDataItem(TypedDict):
    pass

class OptionalSportOddsPreMatchByFixtureAndBookmakerIdResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    fixture_id: typing.Union[int, float]

    market_id: typing.Union[int, float]

    bookmaker_id: typing.Union[int, float]

    label: str

    value: str

    name: str

    sort_order: typing.Optional[str]

    market_description: str

    probability: str

    dp3: str

    fractional: str

    american: str

    winning: typing.Optional[bool]

    stopped: bool

    total: typing.Optional[str]

    handicap: typing.Optional[str]

    participants: typing.Optional[str]

    created_at: str

    updated_at: str

    original_label: typing.Optional[str]

    latest_bookmaker_update: str

class SportOddsPreMatchByFixtureAndBookmakerIdResponseDataItem(RequiredSportOddsPreMatchByFixtureAndBookmakerIdResponseDataItem, OptionalSportOddsPreMatchByFixtureAndBookmakerIdResponseDataItem):
    pass
