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


class RequiredSportNewsAllPreMatchResponseDataItem(TypedDict):
    pass

class OptionalSportNewsAllPreMatchResponseDataItem(TypedDict, total=False):
    title: str

    id: typing.Union[int, float]

    fixture_id: typing.Union[int, float]

    league_id: typing.Union[int, float]

    type: str

class SportNewsAllPreMatchResponseDataItem(RequiredSportNewsAllPreMatchResponseDataItem, OptionalSportNewsAllPreMatchResponseDataItem):
    pass