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

from sportmonks.type.sport_top_scorers_by_stage_id_response_data import SportTopScorersByStageIdResponseData
from sportmonks.type.sport_top_scorers_by_stage_id_response_pagination import SportTopScorersByStageIdResponsePagination
from sportmonks.type.sport_top_scorers_by_stage_id_response_rate_limit import SportTopScorersByStageIdResponseRateLimit
from sportmonks.type.sport_top_scorers_by_stage_id_response_subscription import SportTopScorersByStageIdResponseSubscription

class RequiredSportTopScorersByStageIdResponse(TypedDict):
    pass

class OptionalSportTopScorersByStageIdResponse(TypedDict, total=False):
    data: SportTopScorersByStageIdResponseData

    pagination: SportTopScorersByStageIdResponsePagination

    subscription: SportTopScorersByStageIdResponseSubscription

    rate_limit: SportTopScorersByStageIdResponseRateLimit

    timezone: str

class SportTopScorersByStageIdResponse(RequiredSportTopScorersByStageIdResponse, OptionalSportTopScorersByStageIdResponse):
    pass
