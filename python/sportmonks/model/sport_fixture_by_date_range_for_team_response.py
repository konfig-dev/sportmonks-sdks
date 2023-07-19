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


class SportFixtureByDateRangeForTeamResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['SportFixtureByDateRangeForTeamResponseData']:
                return SportFixtureByDateRangeForTeamResponseData
        
            @staticmethod
            def pagination() -> typing.Type['SportFixtureByDateRangeForTeamResponsePagination']:
                return SportFixtureByDateRangeForTeamResponsePagination
        
            @staticmethod
            def subscription() -> typing.Type['SportFixtureByDateRangeForTeamResponseSubscription']:
                return SportFixtureByDateRangeForTeamResponseSubscription
        
            @staticmethod
            def rate_limit() -> typing.Type['SportFixtureByDateRangeForTeamResponseRateLimit']:
                return SportFixtureByDateRangeForTeamResponseRateLimit
            timezone = schemas.StrSchema
            __annotations__ = {
                "data": data,
                "pagination": pagination,
                "subscription": subscription,
                "rate_limit": rate_limit,
                "timezone": timezone,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'SportFixtureByDateRangeForTeamResponseData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pagination"]) -> 'SportFixtureByDateRangeForTeamResponsePagination': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscription"]) -> 'SportFixtureByDateRangeForTeamResponseSubscription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate_limit"]) -> 'SportFixtureByDateRangeForTeamResponseRateLimit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "pagination", "subscription", "rate_limit", "timezone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['SportFixtureByDateRangeForTeamResponseData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pagination"]) -> typing.Union['SportFixtureByDateRangeForTeamResponsePagination', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscription"]) -> typing.Union['SportFixtureByDateRangeForTeamResponseSubscription', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate_limit"]) -> typing.Union['SportFixtureByDateRangeForTeamResponseRateLimit', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "pagination", "subscription", "rate_limit", "timezone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union['SportFixtureByDateRangeForTeamResponseData', schemas.Unset] = schemas.unset,
        pagination: typing.Union['SportFixtureByDateRangeForTeamResponsePagination', schemas.Unset] = schemas.unset,
        subscription: typing.Union['SportFixtureByDateRangeForTeamResponseSubscription', schemas.Unset] = schemas.unset,
        rate_limit: typing.Union['SportFixtureByDateRangeForTeamResponseRateLimit', schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportFixtureByDateRangeForTeamResponse':
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

from sportmonks.model.sport_fixture_by_date_range_for_team_response_data import SportFixtureByDateRangeForTeamResponseData
from sportmonks.model.sport_fixture_by_date_range_for_team_response_pagination import SportFixtureByDateRangeForTeamResponsePagination
from sportmonks.model.sport_fixture_by_date_range_for_team_response_rate_limit import SportFixtureByDateRangeForTeamResponseRateLimit
from sportmonks.model.sport_fixture_by_date_range_for_team_response_subscription import SportFixtureByDateRangeForTeamResponseSubscription
