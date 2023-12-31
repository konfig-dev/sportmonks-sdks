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


class RequiredSportTopScorersByStageIdResponseDataItem(TypedDict):
    pass

class OptionalSportTopScorersByStageIdResponseDataItem(TypedDict, total=False):
    stage_id: typing.Union[int, float]

    player_id: typing.Union[int, float]

    type_id: typing.Union[int, float]

    team_id: typing.Union[int, float]

    position: typing.Union[int, float]

    total: typing.Union[int, float]

    points: typing.Optional[str]

class SportTopScorersByStageIdResponseDataItem(RequiredSportTopScorersByStageIdResponseDataItem, OptionalSportTopScorersByStageIdResponseDataItem):
    pass
