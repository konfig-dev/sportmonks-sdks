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


class SportCommentariesAllResponseSubscriptionItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def meta() -> typing.Type['SportCommentariesAllResponseSubscriptionItemMeta']:
                return SportCommentariesAllResponseSubscriptionItemMeta
        
            @staticmethod
            def plans() -> typing.Type['SportCommentariesAllResponseSubscriptionItemPlans']:
                return SportCommentariesAllResponseSubscriptionItemPlans
        
            @staticmethod
            def add_ons() -> typing.Type['SportCommentariesAllResponseSubscriptionItemAddOns']:
                return SportCommentariesAllResponseSubscriptionItemAddOns
        
            @staticmethod
            def widgets() -> typing.Type['SportCommentariesAllResponseSubscriptionItemWidgets']:
                return SportCommentariesAllResponseSubscriptionItemWidgets
            __annotations__ = {
                "meta": meta,
                "plans": plans,
                "add_ons": add_ons,
                "widgets": widgets,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'SportCommentariesAllResponseSubscriptionItemMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plans"]) -> 'SportCommentariesAllResponseSubscriptionItemPlans': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["add_ons"]) -> 'SportCommentariesAllResponseSubscriptionItemAddOns': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["widgets"]) -> 'SportCommentariesAllResponseSubscriptionItemWidgets': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["meta", "plans", "add_ons", "widgets", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['SportCommentariesAllResponseSubscriptionItemMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plans"]) -> typing.Union['SportCommentariesAllResponseSubscriptionItemPlans', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["add_ons"]) -> typing.Union['SportCommentariesAllResponseSubscriptionItemAddOns', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["widgets"]) -> typing.Union['SportCommentariesAllResponseSubscriptionItemWidgets', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["meta", "plans", "add_ons", "widgets", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        meta: typing.Union['SportCommentariesAllResponseSubscriptionItemMeta', schemas.Unset] = schemas.unset,
        plans: typing.Union['SportCommentariesAllResponseSubscriptionItemPlans', schemas.Unset] = schemas.unset,
        add_ons: typing.Union['SportCommentariesAllResponseSubscriptionItemAddOns', schemas.Unset] = schemas.unset,
        widgets: typing.Union['SportCommentariesAllResponseSubscriptionItemWidgets', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportCommentariesAllResponseSubscriptionItem':
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

from sportmonks.model.sport_commentaries_all_response_subscription_item_add_ons import SportCommentariesAllResponseSubscriptionItemAddOns
from sportmonks.model.sport_commentaries_all_response_subscription_item_meta import SportCommentariesAllResponseSubscriptionItemMeta
from sportmonks.model.sport_commentaries_all_response_subscription_item_plans import SportCommentariesAllResponseSubscriptionItemPlans
from sportmonks.model.sport_commentaries_all_response_subscription_item_widgets import SportCommentariesAllResponseSubscriptionItemWidgets
