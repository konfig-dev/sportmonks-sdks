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

from sportmonks.type.sport_players_latest_response_subscription_item_add_ons import SportPlayersLatestResponseSubscriptionItemAddOns
from sportmonks.type.sport_players_latest_response_subscription_item_meta import SportPlayersLatestResponseSubscriptionItemMeta
from sportmonks.type.sport_players_latest_response_subscription_item_plans import SportPlayersLatestResponseSubscriptionItemPlans
from sportmonks.type.sport_players_latest_response_subscription_item_widgets import SportPlayersLatestResponseSubscriptionItemWidgets

class RequiredSportPlayersLatestResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportPlayersLatestResponseSubscriptionItem(TypedDict, total=False):
    meta: SportPlayersLatestResponseSubscriptionItemMeta

    plans: SportPlayersLatestResponseSubscriptionItemPlans

    add_ons: SportPlayersLatestResponseSubscriptionItemAddOns

    widgets: SportPlayersLatestResponseSubscriptionItemWidgets

class SportPlayersLatestResponseSubscriptionItem(RequiredSportPlayersLatestResponseSubscriptionItem, OptionalSportPlayersLatestResponseSubscriptionItem):
    pass
