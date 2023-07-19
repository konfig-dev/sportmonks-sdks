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


class RequiredSportPlayersLatestResponseRateLimit(TypedDict):
    pass

class OptionalSportPlayersLatestResponseRateLimit(TypedDict, total=False):
    resets_in_seconds: typing.Union[int, float]

    remaining: typing.Union[int, float]

    requested_entity: str

class SportPlayersLatestResponseRateLimit(RequiredSportPlayersLatestResponseRateLimit, OptionalSportPlayersLatestResponseRateLimit):
    pass
