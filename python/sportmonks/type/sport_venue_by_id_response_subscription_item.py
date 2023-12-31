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

from sportmonks.type.sport_venue_by_id_response_subscription_item_add_ons import SportVenueByIdResponseSubscriptionItemAddOns
from sportmonks.type.sport_venue_by_id_response_subscription_item_meta import SportVenueByIdResponseSubscriptionItemMeta
from sportmonks.type.sport_venue_by_id_response_subscription_item_plans import SportVenueByIdResponseSubscriptionItemPlans
from sportmonks.type.sport_venue_by_id_response_subscription_item_widgets import SportVenueByIdResponseSubscriptionItemWidgets

class RequiredSportVenueByIdResponseSubscriptionItem(TypedDict):
    pass

class OptionalSportVenueByIdResponseSubscriptionItem(TypedDict, total=False):
    meta: SportVenueByIdResponseSubscriptionItemMeta

    plans: SportVenueByIdResponseSubscriptionItemPlans

    add_ons: SportVenueByIdResponseSubscriptionItemAddOns

    widgets: SportVenueByIdResponseSubscriptionItemWidgets

class SportVenueByIdResponseSubscriptionItem(RequiredSportVenueByIdResponseSubscriptionItem, OptionalSportVenueByIdResponseSubscriptionItem):
    pass
