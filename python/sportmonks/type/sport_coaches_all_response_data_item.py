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


class RequiredSportCoachesAllResponseDataItem(TypedDict):
    pass

class OptionalSportCoachesAllResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    player_id: typing.Union[int, float]

    sport_id: typing.Union[int, float]

    country_id: typing.Union[int, float]

    nationality_id: typing.Optional[str]

    city_id: typing.Optional[str]

    common_name: str

    firstname: str

    lastname: str

    name: str

    display_name: str

    image_path: str

    height: typing.Optional[typing.Union[int, float]]

    weight: typing.Optional[typing.Union[int, float]]

    date_of_birth: typing.Optional[str]

    gender: str

class SportCoachesAllResponseDataItem(RequiredSportCoachesAllResponseDataItem, OptionalSportCoachesAllResponseDataItem):
    pass
