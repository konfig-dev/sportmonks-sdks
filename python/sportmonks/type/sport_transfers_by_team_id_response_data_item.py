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


class RequiredSportTransfersByTeamIdResponseDataItem(TypedDict):
    pass

class OptionalSportTransfersByTeamIdResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    sport_id: typing.Union[int, float]

    player_id: typing.Union[int, float]

    type_id: typing.Union[int, float]

    from_team_id: typing.Union[int, float]

    to_team_id: typing.Union[int, float]

    position_id: typing.Optional[typing.Union[int, float]]

    detailed_position_id: typing.Optional[typing.Union[int, float]]

    date: str

    career_ended: bool

    completed: bool

    completed_at: str

class SportTransfersByTeamIdResponseDataItem(RequiredSportTransfersByTeamIdResponseDataItem, OptionalSportTransfersByTeamIdResponseDataItem):
    pass
