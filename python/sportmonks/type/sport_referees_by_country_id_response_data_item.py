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


class RequiredSportRefereesByCountryIdResponseDataItem(TypedDict):
    pass

class OptionalSportRefereesByCountryIdResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    sport_id: typing.Union[int, float]

    country_id: typing.Union[int, float]

    city_id: typing.Optional[str]

    common_name: str

    firstname: str

    lastname: str

    name: str

    display_name: str

    image_path: str

    height: typing.Optional[str]

    weight: typing.Optional[str]

    date_of_birth: typing.Optional[str]

    gender: typing.Optional[str]

class SportRefereesByCountryIdResponseDataItem(RequiredSportRefereesByCountryIdResponseDataItem, OptionalSportRefereesByCountryIdResponseDataItem):
    pass