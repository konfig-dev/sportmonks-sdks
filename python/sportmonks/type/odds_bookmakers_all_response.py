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

from sportmonks.type.odds_bookmakers_all_response_data import OddsBookmakersAllResponseData
from sportmonks.type.odds_bookmakers_all_response_pagination import OddsBookmakersAllResponsePagination
from sportmonks.type.odds_bookmakers_all_response_rate_limit import OddsBookmakersAllResponseRateLimit
from sportmonks.type.odds_bookmakers_all_response_subscription import OddsBookmakersAllResponseSubscription

class RequiredOddsBookmakersAllResponse(TypedDict):
    pass

class OptionalOddsBookmakersAllResponse(TypedDict, total=False):
    data: OddsBookmakersAllResponseData

    pagination: OddsBookmakersAllResponsePagination

    subscription: OddsBookmakersAllResponseSubscription

    rate_limit: OddsBookmakersAllResponseRateLimit

    timezone: str

class OddsBookmakersAllResponse(RequiredOddsBookmakersAllResponse, OptionalOddsBookmakersAllResponse):
    pass
