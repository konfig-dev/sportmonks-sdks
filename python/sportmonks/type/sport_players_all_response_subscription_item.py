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

from sportmonks.type.sport_players_all_response_subscription_item_add_ons import SportPlayersAllResponseSubscriptionItemAddOns
from sportmonks.type.sport_players_all_response_subscription_item_meta import SportPlayersAllResponseSubscriptionItemMeta
from sportmonks.type.sport_players_all_response_subscription_item_plans import SportPlayersAllResponseSubscriptionItemPlans
from sportmonks.type.sport_players_all_response_subscription_item_widgets import SportPlayersAllResponseSubscriptionItemWidgets

class RequiredSportPlayersAllResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportPlayersAllResponseSubscriptionItem(TypedDict, total=False):
    meta: SportPlayersAllResponseSubscriptionItemMeta

    plans: SportPlayersAllResponseSubscriptionItemPlans

    add_ons: SportPlayersAllResponseSubscriptionItemAddOns

    widgets: SportPlayersAllResponseSubscriptionItemWidgets

class SportPlayersAllResponseSubscriptionItem(RequiredSportPlayersAllResponseSubscriptionItem, OptionalSportPlayersAllResponseSubscriptionItem):
    pass
