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


class RequiredSportPlayersSearchResponseDataItem(TypedDict):
    pass

class OptionalSportPlayersSearchResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    sport_id: typing.Union[int, float]

    country_id: typing.Union[int, float]

    nationality_id: typing.Union[int, float]

    city_id: typing.Optional[str]

    position_id: typing.Union[int, float]

    detailed_position_id: typing.Union[typing.Optional[str], typing.Union[int, float]]

    type_id: typing.Union[int, float]

    common_name: str

    firstname: str

    lastname: str

    name: str

    display_name: str

    image_path: str

    height: typing.Union[int, float]

    weight: typing.Union[int, float]

    date_of_birth: str

    gender: str

class SportPlayersSearchResponseDataItem(RequiredSportPlayersSearchResponseDataItem, OptionalSportPlayersSearchResponseDataItem):
    pass
