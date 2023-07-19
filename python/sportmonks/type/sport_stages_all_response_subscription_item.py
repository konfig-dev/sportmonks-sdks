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

from sportmonks.type.sport_stages_all_response_subscription_item_add_ons import SportStagesAllResponseSubscriptionItemAddOns
from sportmonks.type.sport_stages_all_response_subscription_item_meta import SportStagesAllResponseSubscriptionItemMeta
from sportmonks.type.sport_stages_all_response_subscription_item_plans import SportStagesAllResponseSubscriptionItemPlans
from sportmonks.type.sport_stages_all_response_subscription_item_widgets import SportStagesAllResponseSubscriptionItemWidgets

class RequiredSportStagesAllResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportStagesAllResponseSubscriptionItem(TypedDict, total=False):
    meta: SportStagesAllResponseSubscriptionItemMeta

    plans: SportStagesAllResponseSubscriptionItemPlans

    add_ons: SportStagesAllResponseSubscriptionItemAddOns

    widgets: SportStagesAllResponseSubscriptionItemWidgets

class SportStagesAllResponseSubscriptionItem(RequiredSportStagesAllResponseSubscriptionItem, OptionalSportStagesAllResponseSubscriptionItem):
    pass