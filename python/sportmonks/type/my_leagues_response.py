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

from sportmonks.type.my_leagues_response_data import MyLeaguesResponseData
from sportmonks.type.my_leagues_response_rate_limit import MyLeaguesResponseRateLimit
from sportmonks.type.my_leagues_response_subscription import MyLeaguesResponseSubscription

class RequiredMyLeaguesResponse(TypedDict):
    pass

class OptionalMyLeaguesResponse(TypedDict, total=False):
    data: MyLeaguesResponseData

    subscription: MyLeaguesResponseSubscription

    rate_limit: MyLeaguesResponseRateLimit

    timezone: str

class MyLeaguesResponse(RequiredMyLeaguesResponse, OptionalMyLeaguesResponse):
    pass
