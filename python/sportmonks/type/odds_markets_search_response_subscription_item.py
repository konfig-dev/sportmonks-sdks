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

from sportmonks.type.odds_markets_search_response_subscription_item_add_ons import OddsMarketsSearchResponseSubscriptionItemAddOns
from sportmonks.type.odds_markets_search_response_subscription_item_meta import OddsMarketsSearchResponseSubscriptionItemMeta
from sportmonks.type.odds_markets_search_response_subscription_item_plans import OddsMarketsSearchResponseSubscriptionItemPlans
from sportmonks.type.odds_markets_search_response_subscription_item_widgets import OddsMarketsSearchResponseSubscriptionItemWidgets

class RequiredOddsMarketsSearchResponseSubscriptionItem(TypedDict):
    pass

class OptionalOddsMarketsSearchResponseSubscriptionItem(TypedDict, total=False):
    meta: OddsMarketsSearchResponseSubscriptionItemMeta

    plans: OddsMarketsSearchResponseSubscriptionItemPlans

    add_ons: OddsMarketsSearchResponseSubscriptionItemAddOns

    widgets: OddsMarketsSearchResponseSubscriptionItemWidgets

class OddsMarketsSearchResponseSubscriptionItem(RequiredOddsMarketsSearchResponseSubscriptionItem, OptionalOddsMarketsSearchResponseSubscriptionItem):
    pass
