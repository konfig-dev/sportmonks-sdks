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


class RequiredSportTransfersByTeamIdResponseSubscriptionItemPlansItem(TypedDict):
    pass

class OptionalSportTransfersByTeamIdResponseSubscriptionItemPlansItem(TypedDict, total=False):
    plan: str

    sport: str

    category: str

class SportTransfersByTeamIdResponseSubscriptionItemPlansItem(RequiredSportTransfersByTeamIdResponseSubscriptionItemPlansItem, OptionalSportTransfersByTeamIdResponseSubscriptionItemPlansItem):
    pass
