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

from sportmonks.type.sport_livescores_all_response_subscription_item_add_ons import SportLivescoresAllResponseSubscriptionItemAddOns
from sportmonks.type.sport_livescores_all_response_subscription_item_meta import SportLivescoresAllResponseSubscriptionItemMeta
from sportmonks.type.sport_livescores_all_response_subscription_item_plans import SportLivescoresAllResponseSubscriptionItemPlans
from sportmonks.type.sport_livescores_all_response_subscription_item_widgets import SportLivescoresAllResponseSubscriptionItemWidgets

class RequiredSportLivescoresAllResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportLivescoresAllResponseSubscriptionItem(TypedDict, total=False):
    meta: SportLivescoresAllResponseSubscriptionItemMeta

    plans: SportLivescoresAllResponseSubscriptionItemPlans

    add_ons: SportLivescoresAllResponseSubscriptionItemAddOns

    widgets: SportLivescoresAllResponseSubscriptionItemWidgets

class SportLivescoresAllResponseSubscriptionItem(RequiredSportLivescoresAllResponseSubscriptionItem, OptionalSportLivescoresAllResponseSubscriptionItem):
    pass
