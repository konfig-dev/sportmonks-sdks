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

from sportmonks.type.sport_standing_corrections_by_season_id_response_subscription_item_add_ons import SportStandingCorrectionsBySeasonIdResponseSubscriptionItemAddOns
from sportmonks.type.sport_standing_corrections_by_season_id_response_subscription_item_meta import SportStandingCorrectionsBySeasonIdResponseSubscriptionItemMeta
from sportmonks.type.sport_standing_corrections_by_season_id_response_subscription_item_plans import SportStandingCorrectionsBySeasonIdResponseSubscriptionItemPlans
from sportmonks.type.sport_standing_corrections_by_season_id_response_subscription_item_widgets import SportStandingCorrectionsBySeasonIdResponseSubscriptionItemWidgets

class RequiredSportStandingCorrectionsBySeasonIdResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportStandingCorrectionsBySeasonIdResponseSubscriptionItem(TypedDict, total=False):
    meta: SportStandingCorrectionsBySeasonIdResponseSubscriptionItemMeta

    plans: SportStandingCorrectionsBySeasonIdResponseSubscriptionItemPlans

    add_ons: SportStandingCorrectionsBySeasonIdResponseSubscriptionItemAddOns

    widgets: SportStandingCorrectionsBySeasonIdResponseSubscriptionItemWidgets

class SportStandingCorrectionsBySeasonIdResponseSubscriptionItem(RequiredSportStandingCorrectionsBySeasonIdResponseSubscriptionItem, OptionalSportStandingCorrectionsBySeasonIdResponseSubscriptionItem):
    pass