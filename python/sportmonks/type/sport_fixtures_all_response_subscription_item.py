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

from sportmonks.type.sport_fixtures_all_response_subscription_item_add_ons import SportFixturesAllResponseSubscriptionItemAddOns
from sportmonks.type.sport_fixtures_all_response_subscription_item_meta import SportFixturesAllResponseSubscriptionItemMeta
from sportmonks.type.sport_fixtures_all_response_subscription_item_plans import SportFixturesAllResponseSubscriptionItemPlans
from sportmonks.type.sport_fixtures_all_response_subscription_item_widgets import SportFixturesAllResponseSubscriptionItemWidgets

class RequiredSportFixturesAllResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportFixturesAllResponseSubscriptionItem(TypedDict, total=False):
    meta: SportFixturesAllResponseSubscriptionItemMeta

    plans: SportFixturesAllResponseSubscriptionItemPlans

    add_ons: SportFixturesAllResponseSubscriptionItemAddOns

    widgets: SportFixturesAllResponseSubscriptionItemWidgets

class SportFixturesAllResponseSubscriptionItem(RequiredSportFixturesAllResponseSubscriptionItem, OptionalSportFixturesAllResponseSubscriptionItem):
    pass
