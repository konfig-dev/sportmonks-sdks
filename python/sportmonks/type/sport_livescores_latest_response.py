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

from sportmonks.type.sport_livescores_latest_response_data import SportLivescoresLatestResponseData
from sportmonks.type.sport_livescores_latest_response_rate_limit import SportLivescoresLatestResponseRateLimit
from sportmonks.type.sport_livescores_latest_response_subscription import SportLivescoresLatestResponseSubscription

class RequiredSportLivescoresLatestResponse(TypedDict):
    pass

class OptionalSportLivescoresLatestResponse(TypedDict, total=False):
    data: SportLivescoresLatestResponseData

    subscription: SportLivescoresLatestResponseSubscription

    rate_limit: SportLivescoresLatestResponseRateLimit

    timezone: str

class SportLivescoresLatestResponse(RequiredSportLivescoresLatestResponse, OptionalSportLivescoresLatestResponse):
    pass
