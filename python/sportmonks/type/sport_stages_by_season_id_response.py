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

from sportmonks.type.sport_stages_by_season_id_response_data import SportStagesBySeasonIdResponseData
from sportmonks.type.sport_stages_by_season_id_response_rate_limit import SportStagesBySeasonIdResponseRateLimit
from sportmonks.type.sport_stages_by_season_id_response_subscription import SportStagesBySeasonIdResponseSubscription

class RequiredSportStagesBySeasonIdResponse(TypedDict):
    pass

class OptionalSportStagesBySeasonIdResponse(TypedDict, total=False):
    data: SportStagesBySeasonIdResponseData

    subscription: SportStagesBySeasonIdResponseSubscription

    rate_limit: SportStagesBySeasonIdResponseRateLimit

    timezone: str

class SportStagesBySeasonIdResponse(RequiredSportStagesBySeasonIdResponse, OptionalSportStagesBySeasonIdResponse):
    pass
