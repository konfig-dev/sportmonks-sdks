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


class RequiredSportLeaguesByCountryIdResponsePagination(TypedDict):
    pass

class OptionalSportLeaguesByCountryIdResponsePagination(TypedDict, total=False):
    count: typing.Union[int, float]

    per_page: typing.Union[int, float]

    current_page: typing.Union[int, float]

    next_page: typing.Optional[str]

    has_more: bool

class SportLeaguesByCountryIdResponsePagination(RequiredSportLeaguesByCountryIdResponsePagination, OptionalSportLeaguesByCountryIdResponsePagination):
    pass
