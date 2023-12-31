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


class SportCoachesAllResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['SportCoachesAllResponseData']:
                return SportCoachesAllResponseData
        
            @staticmethod
            def pagination() -> typing.Type['SportCoachesAllResponsePagination']:
                return SportCoachesAllResponsePagination
        
            @staticmethod
            def subscription() -> typing.Type['SportCoachesAllResponseSubscription']:
                return SportCoachesAllResponseSubscription
        
            @staticmethod
            def rate_limit() -> typing.Type['SportCoachesAllResponseRateLimit']:
                return SportCoachesAllResponseRateLimit
            timezone = schemas.StrSchema
            __annotations__ = {
                "data": data,
                "pagination": pagination,
                "subscription": subscription,
                "rate_limit": rate_limit,
                "timezone": timezone,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'SportCoachesAllResponseData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pagination"]) -> 'SportCoachesAllResponsePagination': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscription"]) -> 'SportCoachesAllResponseSubscription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate_limit"]) -> 'SportCoachesAllResponseRateLimit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "pagination", "subscription", "rate_limit", "timezone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['SportCoachesAllResponseData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pagination"]) -> typing.Union['SportCoachesAllResponsePagination', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscription"]) -> typing.Union['SportCoachesAllResponseSubscription', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate_limit"]) -> typing.Union['SportCoachesAllResponseRateLimit', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "pagination", "subscription", "rate_limit", "timezone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union['SportCoachesAllResponseData', schemas.Unset] = schemas.unset,
        pagination: typing.Union['SportCoachesAllResponsePagination', schemas.Unset] = schemas.unset,
        subscription: typing.Union['SportCoachesAllResponseSubscription', schemas.Unset] = schemas.unset,
        rate_limit: typing.Union['SportCoachesAllResponseRateLimit', schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportCoachesAllResponse':
        return super().__new__(
            cls,
            *args,
            data=data,
            pagination=pagination,
            subscription=subscription,
            rate_limit=rate_limit,
            timezone=timezone,
            _configuration=_configuration,
            **kwargs,
        )

from sportmonks.model.sport_coaches_all_response_data import SportCoachesAllResponseData
from sportmonks.model.sport_coaches_all_response_pagination import SportCoachesAllResponsePagination
from sportmonks.model.sport_coaches_all_response_rate_limit import SportCoachesAllResponseRateLimit
from sportmonks.model.sport_coaches_all_response_subscription import SportCoachesAllResponseSubscription
