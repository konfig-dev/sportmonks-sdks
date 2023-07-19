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


class RequiredCitiesSearchResponseDataItem(TypedDict):
    pass

class OptionalCitiesSearchResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    country_id: typing.Union[int, float]

    region_id: typing.Union[int, float]

    name: str

    latitude: typing.Optional[str]

    longitude: typing.Optional[str]

class CitiesSearchResponseDataItem(RequiredCitiesSearchResponseDataItem, OptionalCitiesSearchResponseDataItem):
    pass
