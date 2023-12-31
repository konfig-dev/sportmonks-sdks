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


class CountriesSearchResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['CountriesSearchResponseData']:
                return CountriesSearchResponseData
        
            @staticmethod
            def pagination() -> typing.Type['CountriesSearchResponsePagination']:
                return CountriesSearchResponsePagination
        
            @staticmethod
            def subscription() -> typing.Type['CountriesSearchResponseSubscription']:
                return CountriesSearchResponseSubscription
        
            @staticmethod
            def rate_limit() -> typing.Type['CountriesSearchResponseRateLimit']:
                return CountriesSearchResponseRateLimit
            timezone = schemas.StrSchema
            __annotations__ = {
                "data": data,
                "pagination": pagination,
                "subscription": subscription,
                "rate_limit": rate_limit,
                "timezone": timezone,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'CountriesSearchResponseData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pagination"]) -> 'CountriesSearchResponsePagination': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscription"]) -> 'CountriesSearchResponseSubscription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate_limit"]) -> 'CountriesSearchResponseRateLimit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "pagination", "subscription", "rate_limit", "timezone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['CountriesSearchResponseData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pagination"]) -> typing.Union['CountriesSearchResponsePagination', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscription"]) -> typing.Union['CountriesSearchResponseSubscription', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate_limit"]) -> typing.Union['CountriesSearchResponseRateLimit', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "pagination", "subscription", "rate_limit", "timezone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union['CountriesSearchResponseData', schemas.Unset] = schemas.unset,
        pagination: typing.Union['CountriesSearchResponsePagination', schemas.Unset] = schemas.unset,
        subscription: typing.Union['CountriesSearchResponseSubscription', schemas.Unset] = schemas.unset,
        rate_limit: typing.Union['CountriesSearchResponseRateLimit', schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CountriesSearchResponse':
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

from sportmonks.model.countries_search_response_data import CountriesSearchResponseData
from sportmonks.model.countries_search_response_pagination import CountriesSearchResponsePagination
from sportmonks.model.countries_search_response_rate_limit import CountriesSearchResponseRateLimit
from sportmonks.model.countries_search_response_subscription import CountriesSearchResponseSubscription
