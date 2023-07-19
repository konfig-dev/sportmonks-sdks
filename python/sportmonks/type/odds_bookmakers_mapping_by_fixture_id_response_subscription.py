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

from sportmonks.type.odds_bookmakers_mapping_by_fixture_id_response_subscription_item import OddsBookmakersMappingByFixtureIdResponseSubscriptionItem

OddsBookmakersMappingByFixtureIdResponseSubscription = typing.List[OddsBookmakersMappingByFixtureIdResponseSubscriptionItem]