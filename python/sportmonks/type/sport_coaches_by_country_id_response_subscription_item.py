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

from sportmonks.type.sport_coaches_by_country_id_response_subscription_item_add_ons import SportCoachesByCountryIdResponseSubscriptionItemAddOns
from sportmonks.type.sport_coaches_by_country_id_response_subscription_item_meta import SportCoachesByCountryIdResponseSubscriptionItemMeta
from sportmonks.type.sport_coaches_by_country_id_response_subscription_item_plans import SportCoachesByCountryIdResponseSubscriptionItemPlans
from sportmonks.type.sport_coaches_by_country_id_response_subscription_item_widgets import SportCoachesByCountryIdResponseSubscriptionItemWidgets

class RequiredSportCoachesByCountryIdResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportCoachesByCountryIdResponseSubscriptionItem(TypedDict, total=False):
    meta: SportCoachesByCountryIdResponseSubscriptionItemMeta

    plans: SportCoachesByCountryIdResponseSubscriptionItemPlans

    add_ons: SportCoachesByCountryIdResponseSubscriptionItemAddOns

    widgets: SportCoachesByCountryIdResponseSubscriptionItemWidgets

class SportCoachesByCountryIdResponseSubscriptionItem(RequiredSportCoachesByCountryIdResponseSubscriptionItem, OptionalSportCoachesByCountryIdResponseSubscriptionItem):
    pass
