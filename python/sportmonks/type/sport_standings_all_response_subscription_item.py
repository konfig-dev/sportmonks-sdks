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

from sportmonks.type.sport_standings_all_response_subscription_item_add_ons import SportStandingsAllResponseSubscriptionItemAddOns
from sportmonks.type.sport_standings_all_response_subscription_item_meta import SportStandingsAllResponseSubscriptionItemMeta
from sportmonks.type.sport_standings_all_response_subscription_item_plans import SportStandingsAllResponseSubscriptionItemPlans
from sportmonks.type.sport_standings_all_response_subscription_item_widgets import SportStandingsAllResponseSubscriptionItemWidgets

class RequiredSportStandingsAllResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportStandingsAllResponseSubscriptionItem(TypedDict, total=False):
    meta: SportStandingsAllResponseSubscriptionItemMeta

    plans: SportStandingsAllResponseSubscriptionItemPlans

    add_ons: SportStandingsAllResponseSubscriptionItemAddOns

    widgets: SportStandingsAllResponseSubscriptionItemWidgets

class SportStandingsAllResponseSubscriptionItem(RequiredSportStandingsAllResponseSubscriptionItem, OptionalSportStandingsAllResponseSubscriptionItem):
    pass
