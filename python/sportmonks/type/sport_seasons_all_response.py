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

from sportmonks.type.sport_seasons_all_response_data import SportSeasonsAllResponseData
from sportmonks.type.sport_seasons_all_response_pagination import SportSeasonsAllResponsePagination
from sportmonks.type.sport_seasons_all_response_rate_limit import SportSeasonsAllResponseRateLimit
from sportmonks.type.sport_seasons_all_response_subscription import SportSeasonsAllResponseSubscription

class RequiredSportSeasonsAllResponse(TypedDict):
    pass

class OptionalSportSeasonsAllResponse(TypedDict, total=False):
    data: SportSeasonsAllResponseData

    pagination: SportSeasonsAllResponsePagination

    subscription: SportSeasonsAllResponseSubscription

    rate_limit: SportSeasonsAllResponseRateLimit

    timezone: str

class SportSeasonsAllResponse(RequiredSportSeasonsAllResponse, OptionalSportSeasonsAllResponse):
    pass
