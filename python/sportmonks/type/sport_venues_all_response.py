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

from sportmonks.type.sport_venues_all_response_data import SportVenuesAllResponseData
from sportmonks.type.sport_venues_all_response_pagination import SportVenuesAllResponsePagination
from sportmonks.type.sport_venues_all_response_rate_limit import SportVenuesAllResponseRateLimit
from sportmonks.type.sport_venues_all_response_subscription import SportVenuesAllResponseSubscription

class RequiredSportVenuesAllResponse(TypedDict):
    pass

class OptionalSportVenuesAllResponse(TypedDict, total=False):
    data: SportVenuesAllResponseData

    pagination: SportVenuesAllResponsePagination

    subscription: SportVenuesAllResponseSubscription

    rate_limit: SportVenuesAllResponseRateLimit

    timezone: str

class SportVenuesAllResponse(RequiredSportVenuesAllResponse, OptionalSportVenuesAllResponse):
    pass
