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

from sportmonks.type.sport_players_by_country_id_response_data import SportPlayersByCountryIdResponseData
from sportmonks.type.sport_players_by_country_id_response_pagination import SportPlayersByCountryIdResponsePagination
from sportmonks.type.sport_players_by_country_id_response_rate_limit import SportPlayersByCountryIdResponseRateLimit
from sportmonks.type.sport_players_by_country_id_response_subscription import SportPlayersByCountryIdResponseSubscription

class RequiredSportPlayersByCountryIdResponse(TypedDict):
    pass

class OptionalSportPlayersByCountryIdResponse(TypedDict, total=False):
    data: SportPlayersByCountryIdResponseData

    pagination: SportPlayersByCountryIdResponsePagination

    subscription: SportPlayersByCountryIdResponseSubscription

    rate_limit: SportPlayersByCountryIdResponseRateLimit

    timezone: str

class SportPlayersByCountryIdResponse(RequiredSportPlayersByCountryIdResponse, OptionalSportPlayersByCountryIdResponse):
    pass
