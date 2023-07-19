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

from sportmonks.type.sport_news_all_pre_match_response_subscription_item_add_ons import SportNewsAllPreMatchResponseSubscriptionItemAddOns
from sportmonks.type.sport_news_all_pre_match_response_subscription_item_meta import SportNewsAllPreMatchResponseSubscriptionItemMeta
from sportmonks.type.sport_news_all_pre_match_response_subscription_item_plans import SportNewsAllPreMatchResponseSubscriptionItemPlans

class RequiredSportNewsAllPreMatchResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportNewsAllPreMatchResponseSubscriptionItem(TypedDict, total=False):
    meta: SportNewsAllPreMatchResponseSubscriptionItemMeta

    plans: SportNewsAllPreMatchResponseSubscriptionItemPlans

    add_ons: SportNewsAllPreMatchResponseSubscriptionItemAddOns

class SportNewsAllPreMatchResponseSubscriptionItem(RequiredSportNewsAllPreMatchResponseSubscriptionItem, OptionalSportNewsAllPreMatchResponseSubscriptionItem):
    pass