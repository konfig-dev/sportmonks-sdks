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


class RequiredSportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipantsItemMeta(TypedDict):
    pass

class OptionalSportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipantsItemMeta(TypedDict, total=False):
    location: str

class SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipantsItemMeta(RequiredSportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipantsItemMeta, OptionalSportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipantsItemMeta):
    pass
