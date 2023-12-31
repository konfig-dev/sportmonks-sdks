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


class RequiredSportLeaguesByCountryIdResponseDataItem(TypedDict):
    pass

class OptionalSportLeaguesByCountryIdResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    sport_id: typing.Union[int, float]

    country_id: typing.Union[int, float]

    name: str

    active: bool

    short_code: typing.Optional[str]

    image_path: str

    type: str

    sub_type: str

    last_played_at: str

    category: typing.Union[int, float]

    has_jerseys: bool

class SportLeaguesByCountryIdResponseDataItem(RequiredSportLeaguesByCountryIdResponseDataItem, OptionalSportLeaguesByCountryIdResponseDataItem):
    pass
