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


class RequiredSportStateByIdResponseData(TypedDict):
    pass

class OptionalSportStateByIdResponseData(TypedDict, total=False):
    id: typing.Union[int, float]

    state: str

    name: str

    short_name: str

    developer_name: str

    is_live: bool

    is_pending: bool

    is_period_end: bool

    is_final_state: bool

    is_cancelled: bool

    is_final_standing_state: bool

    is_completed: bool

    type_id: typing.Optional[str]

    is_deleted: bool

    is_notstarted: bool

    sections_active: bool

    schedule_overrule: bool

class SportStateByIdResponseData(RequiredSportStateByIdResponseData, OptionalSportStateByIdResponseData):
    pass
