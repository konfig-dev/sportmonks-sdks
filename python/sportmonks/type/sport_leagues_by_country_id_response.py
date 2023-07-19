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

from sportmonks.type.sport_leagues_by_country_id_response_data import SportLeaguesByCountryIdResponseData
from sportmonks.type.sport_leagues_by_country_id_response_pagination import SportLeaguesByCountryIdResponsePagination
from sportmonks.type.sport_leagues_by_country_id_response_rate_limit import SportLeaguesByCountryIdResponseRateLimit
from sportmonks.type.sport_leagues_by_country_id_response_subscription import SportLeaguesByCountryIdResponseSubscription

class RequiredSportLeaguesByCountryIdResponse(TypedDict):
    pass

class OptionalSportLeaguesByCountryIdResponse(TypedDict, total=False):
    data: SportLeaguesByCountryIdResponseData

    pagination: SportLeaguesByCountryIdResponsePagination

    subscription: SportLeaguesByCountryIdResponseSubscription

    rate_limit: SportLeaguesByCountryIdResponseRateLimit

    timezone: str

class SportLeaguesByCountryIdResponse(RequiredSportLeaguesByCountryIdResponse, OptionalSportLeaguesByCountryIdResponse):
    pass
