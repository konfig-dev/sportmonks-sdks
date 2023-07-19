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


class SportStagesSearchResponseSubscriptionItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def meta() -> typing.Type['SportStagesSearchResponseSubscriptionItemMeta']:
                return SportStagesSearchResponseSubscriptionItemMeta
        
            @staticmethod
            def plans() -> typing.Type['SportStagesSearchResponseSubscriptionItemPlans']:
                return SportStagesSearchResponseSubscriptionItemPlans
        
            @staticmethod
            def add_ons() -> typing.Type['SportStagesSearchResponseSubscriptionItemAddOns']:
                return SportStagesSearchResponseSubscriptionItemAddOns
        
            @staticmethod
            def widgets() -> typing.Type['SportStagesSearchResponseSubscriptionItemWidgets']:
                return SportStagesSearchResponseSubscriptionItemWidgets
            __annotations__ = {
                "meta": meta,
                "plans": plans,
                "add_ons": add_ons,
                "widgets": widgets,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'SportStagesSearchResponseSubscriptionItemMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plans"]) -> 'SportStagesSearchResponseSubscriptionItemPlans': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["add_ons"]) -> 'SportStagesSearchResponseSubscriptionItemAddOns': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["widgets"]) -> 'SportStagesSearchResponseSubscriptionItemWidgets': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["meta", "plans", "add_ons", "widgets", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['SportStagesSearchResponseSubscriptionItemMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plans"]) -> typing.Union['SportStagesSearchResponseSubscriptionItemPlans', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["add_ons"]) -> typing.Union['SportStagesSearchResponseSubscriptionItemAddOns', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["widgets"]) -> typing.Union['SportStagesSearchResponseSubscriptionItemWidgets', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["meta", "plans", "add_ons", "widgets", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        meta: typing.Union['SportStagesSearchResponseSubscriptionItemMeta', schemas.Unset] = schemas.unset,
        plans: typing.Union['SportStagesSearchResponseSubscriptionItemPlans', schemas.Unset] = schemas.unset,
        add_ons: typing.Union['SportStagesSearchResponseSubscriptionItemAddOns', schemas.Unset] = schemas.unset,
        widgets: typing.Union['SportStagesSearchResponseSubscriptionItemWidgets', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportStagesSearchResponseSubscriptionItem':
        return super().__new__(
            cls,
            *args,
            meta=meta,
            plans=plans,
            add_ons=add_ons,
            widgets=widgets,
            _configuration=_configuration,
            **kwargs,
        )

from sportmonks.model.sport_stages_search_response_subscription_item_add_ons import SportStagesSearchResponseSubscriptionItemAddOns
from sportmonks.model.sport_stages_search_response_subscription_item_meta import SportStagesSearchResponseSubscriptionItemMeta
from sportmonks.model.sport_stages_search_response_subscription_item_plans import SportStagesSearchResponseSubscriptionItemPlans
from sportmonks.model.sport_stages_search_response_subscription_item_widgets import SportStagesSearchResponseSubscriptionItemWidgets
