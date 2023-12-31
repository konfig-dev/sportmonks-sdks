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


class RequiredOddsMarketByIdResponseData(TypedDict):
    pass

class OptionalOddsMarketByIdResponseData(TypedDict, total=False):
    id: typing.Union[int, float]

    legacy_id: typing.Union[int, float]

    name: str

    developer_name: str

    has_winning_calculations: bool

class OddsMarketByIdResponseData(RequiredOddsMarketByIdResponseData, OptionalOddsMarketByIdResponseData):
    pass
