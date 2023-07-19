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

from sportmonks.type.sport_fixtures_by_date_response_subscription_item_add_ons import SportFixturesByDateResponseSubscriptionItemAddOns
from sportmonks.type.sport_fixtures_by_date_response_subscription_item_meta import SportFixturesByDateResponseSubscriptionItemMeta
from sportmonks.type.sport_fixtures_by_date_response_subscription_item_plans import SportFixturesByDateResponseSubscriptionItemPlans
from sportmonks.type.sport_fixtures_by_date_response_subscription_item_widgets import SportFixturesByDateResponseSubscriptionItemWidgets

class RequiredSportFixturesByDateResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportFixturesByDateResponseSubscriptionItem(TypedDict, total=False):
    meta: SportFixturesByDateResponseSubscriptionItemMeta

    plans: SportFixturesByDateResponseSubscriptionItemPlans

    add_ons: SportFixturesByDateResponseSubscriptionItemAddOns

    widgets: SportFixturesByDateResponseSubscriptionItemWidgets

class SportFixturesByDateResponseSubscriptionItem(RequiredSportFixturesByDateResponseSubscriptionItem, OptionalSportFixturesByDateResponseSubscriptionItem):
    pass
