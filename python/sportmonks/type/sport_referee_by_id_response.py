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

from sportmonks.type.sport_referee_by_id_response_data import SportRefereeByIdResponseData
from sportmonks.type.sport_referee_by_id_response_rate_limit import SportRefereeByIdResponseRateLimit
from sportmonks.type.sport_referee_by_id_response_subscription import SportRefereeByIdResponseSubscription

class RequiredSportRefereeByIdResponse(TypedDict):
    pass

class OptionalSportRefereeByIdResponse(TypedDict, total=False):
    data: SportRefereeByIdResponseData

    subscription: SportRefereeByIdResponseSubscription

    rate_limit: SportRefereeByIdResponseRateLimit

    timezone: str

class SportRefereeByIdResponse(RequiredSportRefereeByIdResponse, OptionalSportRefereeByIdResponse):
    pass
