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

from sportmonks.type.sport_predictions_all_response_data import SportPredictionsAllResponseData
from sportmonks.type.sport_predictions_all_response_pagination import SportPredictionsAllResponsePagination
from sportmonks.type.sport_predictions_all_response_rate_limit import SportPredictionsAllResponseRateLimit
from sportmonks.type.sport_predictions_all_response_subscription import SportPredictionsAllResponseSubscription

class RequiredSportPredictionsAllResponse(TypedDict):
    pass

class OptionalSportPredictionsAllResponse(TypedDict, total=False):
    data: SportPredictionsAllResponseData

    pagination: SportPredictionsAllResponsePagination

    subscription: SportPredictionsAllResponseSubscription

    rate_limit: SportPredictionsAllResponseRateLimit

    timezone: str

class SportPredictionsAllResponse(RequiredSportPredictionsAllResponse, OptionalSportPredictionsAllResponse):
    pass
