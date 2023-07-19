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

from sportmonks.type.sport_standings_by_round_id_response_subscription_item_add_ons import SportStandingsByRoundIdResponseSubscriptionItemAddOns
from sportmonks.type.sport_standings_by_round_id_response_subscription_item_meta import SportStandingsByRoundIdResponseSubscriptionItemMeta
from sportmonks.type.sport_standings_by_round_id_response_subscription_item_plans import SportStandingsByRoundIdResponseSubscriptionItemPlans
from sportmonks.type.sport_standings_by_round_id_response_subscription_item_widgets import SportStandingsByRoundIdResponseSubscriptionItemWidgets

class RequiredSportStandingsByRoundIdResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportStandingsByRoundIdResponseSubscriptionItem(TypedDict, total=False):
    meta: SportStandingsByRoundIdResponseSubscriptionItemMeta

    plans: SportStandingsByRoundIdResponseSubscriptionItemPlans

    add_ons: SportStandingsByRoundIdResponseSubscriptionItemAddOns

    widgets: SportStandingsByRoundIdResponseSubscriptionItemWidgets

class SportStandingsByRoundIdResponseSubscriptionItem(RequiredSportStandingsByRoundIdResponseSubscriptionItem, OptionalSportStandingsByRoundIdResponseSubscriptionItem):
    pass