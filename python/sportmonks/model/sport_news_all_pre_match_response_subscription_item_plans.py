# coding: utf-8

"""
    SportMonks

    Surpass the competition with superior sports data

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sportmonks import schemas  # noqa: F401


class SportNewsAllPreMatchResponseSubscriptionItemPlans(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['SportNewsAllPreMatchResponseSubscriptionItemPlansItem']:
            return SportNewsAllPreMatchResponseSubscriptionItemPlansItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['SportNewsAllPreMatchResponseSubscriptionItemPlansItem'], typing.List['SportNewsAllPreMatchResponseSubscriptionItemPlansItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SportNewsAllPreMatchResponseSubscriptionItemPlans':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'SportNewsAllPreMatchResponseSubscriptionItemPlansItem':
        return super().__getitem__(i)

from sportmonks.model.sport_news_all_pre_match_response_subscription_item_plans_item import SportNewsAllPreMatchResponseSubscriptionItemPlansItem
