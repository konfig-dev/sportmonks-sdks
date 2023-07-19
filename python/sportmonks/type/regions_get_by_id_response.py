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

from sportmonks.type.regions_get_by_id_response_data import RegionsGetByIdResponseData
from sportmonks.type.regions_get_by_id_response_rate_limit import RegionsGetByIdResponseRateLimit
from sportmonks.type.regions_get_by_id_response_subscription import RegionsGetByIdResponseSubscription

class RequiredRegionsGetByIdResponse(TypedDict):
    pass

class OptionalRegionsGetByIdResponse(TypedDict, total=False):
    data: RegionsGetByIdResponseData

    subscription: RegionsGetByIdResponseSubscription

    rate_limit: RegionsGetByIdResponseRateLimit

    timezone: str

class RegionsGetByIdResponse(RequiredRegionsGetByIdResponse, OptionalRegionsGetByIdResponse):
    pass
