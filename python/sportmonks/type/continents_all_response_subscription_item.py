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

from sportmonks.type.continents_all_response_subscription_item_add_ons import ContinentsAllResponseSubscriptionItemAddOns
from sportmonks.type.continents_all_response_subscription_item_meta import ContinentsAllResponseSubscriptionItemMeta
from sportmonks.type.continents_all_response_subscription_item_plans import ContinentsAllResponseSubscriptionItemPlans
from sportmonks.type.continents_all_response_subscription_item_widgets import ContinentsAllResponseSubscriptionItemWidgets

class RequiredContinentsAllResponseSubscriptionItem(TypedDict):
    pass

class OptionalContinentsAllResponseSubscriptionItem(TypedDict, total=False):
    meta: ContinentsAllResponseSubscriptionItemMeta

    plans: ContinentsAllResponseSubscriptionItemPlans

    add_ons: ContinentsAllResponseSubscriptionItemAddOns

    widgets: ContinentsAllResponseSubscriptionItemWidgets

class ContinentsAllResponseSubscriptionItem(RequiredContinentsAllResponseSubscriptionItem, OptionalContinentsAllResponseSubscriptionItem):
    pass
