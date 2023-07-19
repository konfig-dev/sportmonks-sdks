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

from sportmonks.type.sport_player_by_id_response_subscription_item_add_ons import SportPlayerByIdResponseSubscriptionItemAddOns
from sportmonks.type.sport_player_by_id_response_subscription_item_meta import SportPlayerByIdResponseSubscriptionItemMeta
from sportmonks.type.sport_player_by_id_response_subscription_item_plans import SportPlayerByIdResponseSubscriptionItemPlans
from sportmonks.type.sport_player_by_id_response_subscription_item_widgets import SportPlayerByIdResponseSubscriptionItemWidgets

class RequiredSportPlayerByIdResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportPlayerByIdResponseSubscriptionItem(TypedDict, total=False):
    meta: SportPlayerByIdResponseSubscriptionItemMeta

    plans: SportPlayerByIdResponseSubscriptionItemPlans

    add_ons: SportPlayerByIdResponseSubscriptionItemAddOns

    widgets: SportPlayerByIdResponseSubscriptionItemWidgets

class SportPlayerByIdResponseSubscriptionItem(RequiredSportPlayerByIdResponseSubscriptionItem, OptionalSportPlayerByIdResponseSubscriptionItem):
    pass