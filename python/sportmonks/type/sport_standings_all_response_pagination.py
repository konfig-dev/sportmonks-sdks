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


class RequiredSportStandingsAllResponsePagination(TypedDict):
    pass

class OptionalSportStandingsAllResponsePagination(TypedDict, total=False):
    count: typing.Union[int, float]

    per_page: typing.Union[int, float]

    current_page: typing.Union[int, float]

    next_page: str

    has_more: bool

class SportStandingsAllResponsePagination(RequiredSportStandingsAllResponsePagination, OptionalSportStandingsAllResponsePagination):
    pass
