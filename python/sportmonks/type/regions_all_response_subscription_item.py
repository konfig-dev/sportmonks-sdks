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

from sportmonks.type.regions_all_response_subscription_item_add_ons import RegionsAllResponseSubscriptionItemAddOns
from sportmonks.type.regions_all_response_subscription_item_meta import RegionsAllResponseSubscriptionItemMeta
from sportmonks.type.regions_all_response_subscription_item_plans import RegionsAllResponseSubscriptionItemPlans
from sportmonks.type.regions_all_response_subscription_item_widgets import RegionsAllResponseSubscriptionItemWidgets

class RequiredRegionsAllResponseSubscriptionItem(TypedDict):
    pass

class OptionalRegionsAllResponseSubscriptionItem(TypedDict, total=False):
    meta: RegionsAllResponseSubscriptionItemMeta

    plans: RegionsAllResponseSubscriptionItemPlans

    add_ons: RegionsAllResponseSubscriptionItemAddOns

    widgets: RegionsAllResponseSubscriptionItemWidgets

class RegionsAllResponseSubscriptionItem(RequiredRegionsAllResponseSubscriptionItem, OptionalRegionsAllResponseSubscriptionItem):
    pass