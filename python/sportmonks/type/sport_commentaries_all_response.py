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

from sportmonks.type.sport_commentaries_all_response_data import SportCommentariesAllResponseData
from sportmonks.type.sport_commentaries_all_response_pagination import SportCommentariesAllResponsePagination
from sportmonks.type.sport_commentaries_all_response_rate_limit import SportCommentariesAllResponseRateLimit
from sportmonks.type.sport_commentaries_all_response_subscription import SportCommentariesAllResponseSubscription

class RequiredSportCommentariesAllResponse(TypedDict):
    pass

class OptionalSportCommentariesAllResponse(TypedDict, total=False):
    data: SportCommentariesAllResponseData

    pagination: SportCommentariesAllResponsePagination

    subscription: SportCommentariesAllResponseSubscription

    rate_limit: SportCommentariesAllResponseRateLimit

    timezone: str

class SportCommentariesAllResponse(RequiredSportCommentariesAllResponse, OptionalSportCommentariesAllResponse):
    pass
