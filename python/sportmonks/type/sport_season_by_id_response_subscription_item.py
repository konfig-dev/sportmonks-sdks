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

from sportmonks.type.sport_season_by_id_response_subscription_item_add_ons import SportSeasonByIdResponseSubscriptionItemAddOns
from sportmonks.type.sport_season_by_id_response_subscription_item_meta import SportSeasonByIdResponseSubscriptionItemMeta
from sportmonks.type.sport_season_by_id_response_subscription_item_plans import SportSeasonByIdResponseSubscriptionItemPlans
from sportmonks.type.sport_season_by_id_response_subscription_item_widgets import SportSeasonByIdResponseSubscriptionItemWidgets

class RequiredSportSeasonByIdResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportSeasonByIdResponseSubscriptionItem(TypedDict, total=False):
    meta: SportSeasonByIdResponseSubscriptionItemMeta

    plans: SportSeasonByIdResponseSubscriptionItemPlans

    add_ons: SportSeasonByIdResponseSubscriptionItemAddOns

    widgets: SportSeasonByIdResponseSubscriptionItemWidgets

class SportSeasonByIdResponseSubscriptionItem(RequiredSportSeasonByIdResponseSubscriptionItem, OptionalSportSeasonByIdResponseSubscriptionItem):
    pass
