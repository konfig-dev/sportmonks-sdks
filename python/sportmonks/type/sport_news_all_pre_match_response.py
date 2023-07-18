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


class RequiredSportNewsAllPreMatchResponse(TypedDict):
    pass

class OptionalSportNewsAllPreMatchResponse(TypedDict, total=False):
    data: typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    pagination: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    subscription: typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    rate_limit: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    timezone: str

class SportNewsAllPreMatchResponse(RequiredSportNewsAllPreMatchResponse, OptionalSportNewsAllPreMatchResponse):
    pass
