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


class SportLeaguesAllResponseSubscriptionItemPlans(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['SportLeaguesAllResponseSubscriptionItemPlansItem']:
            return SportLeaguesAllResponseSubscriptionItemPlansItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['SportLeaguesAllResponseSubscriptionItemPlansItem'], typing.List['SportLeaguesAllResponseSubscriptionItemPlansItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SportLeaguesAllResponseSubscriptionItemPlans':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'SportLeaguesAllResponseSubscriptionItemPlansItem':
        return super().__getitem__(i)

from sportmonks.model.sport_leagues_all_response_subscription_item_plans_item import SportLeaguesAllResponseSubscriptionItemPlansItem
