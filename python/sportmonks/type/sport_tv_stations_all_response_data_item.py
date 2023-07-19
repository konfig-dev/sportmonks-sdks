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


class RequiredSportTvStationsAllResponseDataItem(TypedDict):
    pass

class OptionalSportTvStationsAllResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    name: str

    url: str

    image_path: typing.Optional[str]

    type: str

    related_id: typing.Union[typing.Optional[str], typing.Union[int, float]]

class SportTvStationsAllResponseDataItem(RequiredSportTvStationsAllResponseDataItem, OptionalSportTvStationsAllResponseDataItem):
    pass
