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

from sportmonks.type.sport_fixtures_search_response_data import SportFixturesSearchResponseData
from sportmonks.type.sport_fixtures_search_response_pagination import SportFixturesSearchResponsePagination
from sportmonks.type.sport_fixtures_search_response_rate_limit import SportFixturesSearchResponseRateLimit
from sportmonks.type.sport_fixtures_search_response_subscription import SportFixturesSearchResponseSubscription

class RequiredSportFixturesSearchResponse(TypedDict):
    pass

class OptionalSportFixturesSearchResponse(TypedDict, total=False):
    data: SportFixturesSearchResponseData

    pagination: SportFixturesSearchResponsePagination

    subscription: SportFixturesSearchResponseSubscription

    rate_limit: SportFixturesSearchResponseRateLimit

    timezone: str

class SportFixturesSearchResponse(RequiredSportFixturesSearchResponse, OptionalSportFixturesSearchResponse):
    pass
