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

from sportmonks.type.sport_rivals_by_team_id_response_subscription_item_add_ons import SportRivalsByTeamIdResponseSubscriptionItemAddOns
from sportmonks.type.sport_rivals_by_team_id_response_subscription_item_meta import SportRivalsByTeamIdResponseSubscriptionItemMeta
from sportmonks.type.sport_rivals_by_team_id_response_subscription_item_plans import SportRivalsByTeamIdResponseSubscriptionItemPlans

class RequiredSportRivalsByTeamIdResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportRivalsByTeamIdResponseSubscriptionItem(TypedDict, total=False):
    meta: SportRivalsByTeamIdResponseSubscriptionItemMeta

    plans: SportRivalsByTeamIdResponseSubscriptionItemPlans

    add_ons: SportRivalsByTeamIdResponseSubscriptionItemAddOns

class SportRivalsByTeamIdResponseSubscriptionItem(RequiredSportRivalsByTeamIdResponseSubscriptionItem, OptionalSportRivalsByTeamIdResponseSubscriptionItem):
    pass
