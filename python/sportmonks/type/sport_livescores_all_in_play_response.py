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

from sportmonks.type.sport_livescores_all_in_play_response_data import SportLivescoresAllInPlayResponseData
from sportmonks.type.sport_livescores_all_in_play_response_rate_limit import SportLivescoresAllInPlayResponseRateLimit
from sportmonks.type.sport_livescores_all_in_play_response_subscription import SportLivescoresAllInPlayResponseSubscription

class RequiredSportLivescoresAllInPlayResponse(TypedDict):
    pass

class OptionalSportLivescoresAllInPlayResponse(TypedDict, total=False):
    data: SportLivescoresAllInPlayResponseData

    subscription: SportLivescoresAllInPlayResponseSubscription

    rate_limit: SportLivescoresAllInPlayResponseRateLimit

    timezone: str

class SportLivescoresAllInPlayResponse(RequiredSportLivescoresAllInPlayResponse, OptionalSportLivescoresAllInPlayResponse):
    pass
