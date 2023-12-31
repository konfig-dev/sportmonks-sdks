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

from sportmonks.type.sport_venues_all_response_subscription_item_add_ons import SportVenuesAllResponseSubscriptionItemAddOns
from sportmonks.type.sport_venues_all_response_subscription_item_meta import SportVenuesAllResponseSubscriptionItemMeta
from sportmonks.type.sport_venues_all_response_subscription_item_plans import SportVenuesAllResponseSubscriptionItemPlans
from sportmonks.type.sport_venues_all_response_subscription_item_widgets import SportVenuesAllResponseSubscriptionItemWidgets

class RequiredSportVenuesAllResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportVenuesAllResponseSubscriptionItem(TypedDict, total=False):
    meta: SportVenuesAllResponseSubscriptionItemMeta

    plans: SportVenuesAllResponseSubscriptionItemPlans

    add_ons: SportVenuesAllResponseSubscriptionItemAddOns

    widgets: SportVenuesAllResponseSubscriptionItemWidgets

class SportVenuesAllResponseSubscriptionItem(RequiredSportVenuesAllResponseSubscriptionItem, OptionalSportVenuesAllResponseSubscriptionItem):
    pass
