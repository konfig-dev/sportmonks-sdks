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

from sportmonks.type.sport_stages_all_response_data import SportStagesAllResponseData
from sportmonks.type.sport_stages_all_response_pagination import SportStagesAllResponsePagination
from sportmonks.type.sport_stages_all_response_rate_limit import SportStagesAllResponseRateLimit
from sportmonks.type.sport_stages_all_response_subscription import SportStagesAllResponseSubscription

class RequiredSportStagesAllResponse(TypedDict):
    pass

class OptionalSportStagesAllResponse(TypedDict, total=False):
    data: SportStagesAllResponseData

    pagination: SportStagesAllResponsePagination

    subscription: SportStagesAllResponseSubscription

    rate_limit: SportStagesAllResponseRateLimit

    timezone: str

class SportStagesAllResponse(RequiredSportStagesAllResponse, OptionalSportStagesAllResponse):
    pass
