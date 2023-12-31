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

from sportmonks.type.sport_predictions_all_value_bets_response_data_item_predictions import SportPredictionsAllValueBetsResponseDataItemPredictions

class RequiredSportPredictionsAllValueBetsResponseDataItem(TypedDict):
    pass

class OptionalSportPredictionsAllValueBetsResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    fixture_id: typing.Union[int, float]

    predictions: SportPredictionsAllValueBetsResponseDataItemPredictions

    type_id: typing.Union[int, float]

class SportPredictionsAllValueBetsResponseDataItem(RequiredSportPredictionsAllValueBetsResponseDataItem, OptionalSportPredictionsAllValueBetsResponseDataItem):
    pass
