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


class SportOddsPreMatchByFixtureIdResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['SportOddsPreMatchByFixtureIdResponseData']:
                return SportOddsPreMatchByFixtureIdResponseData
        
            @staticmethod
            def subscription() -> typing.Type['SportOddsPreMatchByFixtureIdResponseSubscription']:
                return SportOddsPreMatchByFixtureIdResponseSubscription
        
            @staticmethod
            def rate_limit() -> typing.Type['SportOddsPreMatchByFixtureIdResponseRateLimit']:
                return SportOddsPreMatchByFixtureIdResponseRateLimit
            timezone = schemas.StrSchema
            __annotations__ = {
                "data": data,
                "subscription": subscription,
                "rate_limit": rate_limit,
                "timezone": timezone,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'SportOddsPreMatchByFixtureIdResponseData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscription"]) -> 'SportOddsPreMatchByFixtureIdResponseSubscription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate_limit"]) -> 'SportOddsPreMatchByFixtureIdResponseRateLimit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "subscription", "rate_limit", "timezone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['SportOddsPreMatchByFixtureIdResponseData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscription"]) -> typing.Union['SportOddsPreMatchByFixtureIdResponseSubscription', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate_limit"]) -> typing.Union['SportOddsPreMatchByFixtureIdResponseRateLimit', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "subscription", "rate_limit", "timezone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union['SportOddsPreMatchByFixtureIdResponseData', schemas.Unset] = schemas.unset,
        subscription: typing.Union['SportOddsPreMatchByFixtureIdResponseSubscription', schemas.Unset] = schemas.unset,
        rate_limit: typing.Union['SportOddsPreMatchByFixtureIdResponseRateLimit', schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportOddsPreMatchByFixtureIdResponse':
        return super().__new__(
            cls,
            *args,
            data=data,
            subscription=subscription,
            rate_limit=rate_limit,
            timezone=timezone,
            _configuration=_configuration,
            **kwargs,
        )

from sportmonks.model.sport_odds_pre_match_by_fixture_id_response_data import SportOddsPreMatchByFixtureIdResponseData
from sportmonks.model.sport_odds_pre_match_by_fixture_id_response_rate_limit import SportOddsPreMatchByFixtureIdResponseRateLimit
from sportmonks.model.sport_odds_pre_match_by_fixture_id_response_subscription import SportOddsPreMatchByFixtureIdResponseSubscription
