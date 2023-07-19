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


class RequiredSportOddsInPlayByFixtureIdResponseDataItem(TypedDict):
    pass

class OptionalSportOddsInPlayByFixtureIdResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    fixture_id: typing.Union[int, float]

    provider_id: typing.Union[int, float]

    external_id: str

    market_id: typing.Union[int, float]

    bookmaker_id: typing.Union[int, float]

    label: str

    value: str

    name: typing.Optional[str]

    sort_order: typing.Union[int, float]

    market_description: str

    probability: str

    dp3: str

    fractional: str

    american: str

    winning: bool

    suspended: bool

    stopped: bool

    total: typing.Optional[str]

    handicap: typing.Optional[str]

    participants: typing.Optional[str]

    created_at: str

    updated_at: str

class SportOddsInPlayByFixtureIdResponseDataItem(RequiredSportOddsInPlayByFixtureIdResponseDataItem, OptionalSportOddsInPlayByFixtureIdResponseDataItem):
    pass
