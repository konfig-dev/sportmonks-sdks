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


class RequiredSportVenuesBySeasonIdResponseDataItem(TypedDict):
    pass

class OptionalSportVenuesBySeasonIdResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    country_id: typing.Union[typing.Union[int, float], typing.Optional[str]]

    city_id: typing.Union[typing.Union[int, float], typing.Optional[str]]

    name: str

    address: str

    zipcode: typing.Optional[str]

    latitude: str

    longitude: str

    capacity: typing.Union[int, float]

    image_path: typing.Optional[str]

    city_name: str

    surface: str

    national_team: bool

class SportVenuesBySeasonIdResponseDataItem(RequiredSportVenuesBySeasonIdResponseDataItem, OptionalSportVenuesBySeasonIdResponseDataItem):
    pass