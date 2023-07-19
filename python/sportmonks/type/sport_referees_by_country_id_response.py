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

from sportmonks.type.sport_referees_by_country_id_response_data import SportRefereesByCountryIdResponseData
from sportmonks.type.sport_referees_by_country_id_response_pagination import SportRefereesByCountryIdResponsePagination
from sportmonks.type.sport_referees_by_country_id_response_rate_limit import SportRefereesByCountryIdResponseRateLimit
from sportmonks.type.sport_referees_by_country_id_response_subscription import SportRefereesByCountryIdResponseSubscription

class RequiredSportRefereesByCountryIdResponse(TypedDict):
    pass

class OptionalSportRefereesByCountryIdResponse(TypedDict, total=False):
    data: SportRefereesByCountryIdResponseData

    pagination: SportRefereesByCountryIdResponsePagination

    subscription: SportRefereesByCountryIdResponseSubscription

    rate_limit: SportRefereesByCountryIdResponseRateLimit

    timezone: str

class SportRefereesByCountryIdResponse(RequiredSportRefereesByCountryIdResponse, OptionalSportRefereesByCountryIdResponse):
    pass
