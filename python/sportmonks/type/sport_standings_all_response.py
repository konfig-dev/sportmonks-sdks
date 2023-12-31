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

from sportmonks.type.sport_standings_all_response_data import SportStandingsAllResponseData
from sportmonks.type.sport_standings_all_response_pagination import SportStandingsAllResponsePagination
from sportmonks.type.sport_standings_all_response_rate_limit import SportStandingsAllResponseRateLimit
from sportmonks.type.sport_standings_all_response_subscription import SportStandingsAllResponseSubscription

class RequiredSportStandingsAllResponse(TypedDict):
    pass

class OptionalSportStandingsAllResponse(TypedDict, total=False):
    data: SportStandingsAllResponseData

    pagination: SportStandingsAllResponsePagination

    subscription: SportStandingsAllResponseSubscription

    rate_limit: SportStandingsAllResponseRateLimit

    timezone: str

class SportStandingsAllResponse(RequiredSportStandingsAllResponse, OptionalSportStandingsAllResponse):
    pass
