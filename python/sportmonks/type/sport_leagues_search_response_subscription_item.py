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

from sportmonks.type.sport_leagues_search_response_subscription_item_add_ons import SportLeaguesSearchResponseSubscriptionItemAddOns
from sportmonks.type.sport_leagues_search_response_subscription_item_meta import SportLeaguesSearchResponseSubscriptionItemMeta
from sportmonks.type.sport_leagues_search_response_subscription_item_plans import SportLeaguesSearchResponseSubscriptionItemPlans
from sportmonks.type.sport_leagues_search_response_subscription_item_widgets import SportLeaguesSearchResponseSubscriptionItemWidgets

class RequiredSportLeaguesSearchResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportLeaguesSearchResponseSubscriptionItem(TypedDict, total=False):
    meta: SportLeaguesSearchResponseSubscriptionItemMeta

    plans: SportLeaguesSearchResponseSubscriptionItemPlans

    add_ons: SportLeaguesSearchResponseSubscriptionItemAddOns

    widgets: SportLeaguesSearchResponseSubscriptionItemWidgets

class SportLeaguesSearchResponseSubscriptionItem(RequiredSportLeaguesSearchResponseSubscriptionItem, OptionalSportLeaguesSearchResponseSubscriptionItem):
    pass