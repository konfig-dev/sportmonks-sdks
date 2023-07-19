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

from sportmonks.type.sport_fixtures_by_ids_response_subscription_item_add_ons import SportFixturesByIdsResponseSubscriptionItemAddOns
from sportmonks.type.sport_fixtures_by_ids_response_subscription_item_meta import SportFixturesByIdsResponseSubscriptionItemMeta
from sportmonks.type.sport_fixtures_by_ids_response_subscription_item_plans import SportFixturesByIdsResponseSubscriptionItemPlans
from sportmonks.type.sport_fixtures_by_ids_response_subscription_item_widgets import SportFixturesByIdsResponseSubscriptionItemWidgets

class RequiredSportFixturesByIdsResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportFixturesByIdsResponseSubscriptionItem(TypedDict, total=False):
    meta: SportFixturesByIdsResponseSubscriptionItemMeta

    plans: SportFixturesByIdsResponseSubscriptionItemPlans

    add_ons: SportFixturesByIdsResponseSubscriptionItemAddOns

    widgets: SportFixturesByIdsResponseSubscriptionItemWidgets

class SportFixturesByIdsResponseSubscriptionItem(RequiredSportFixturesByIdsResponseSubscriptionItem, OptionalSportFixturesByIdsResponseSubscriptionItem):
    pass