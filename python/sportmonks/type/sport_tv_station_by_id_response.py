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

from sportmonks.type.sport_tv_station_by_id_response_data import SportTvStationByIdResponseData
from sportmonks.type.sport_tv_station_by_id_response_rate_limit import SportTvStationByIdResponseRateLimit
from sportmonks.type.sport_tv_station_by_id_response_subscription import SportTvStationByIdResponseSubscription

class RequiredSportTvStationByIdResponse(TypedDict):
    pass

class OptionalSportTvStationByIdResponse(TypedDict, total=False):
    data: SportTvStationByIdResponseData

    subscription: SportTvStationByIdResponseSubscription

    rate_limit: SportTvStationByIdResponseRateLimit

    timezone: str

class SportTvStationByIdResponse(RequiredSportTvStationByIdResponse, OptionalSportTvStationByIdResponse):
    pass
