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


class SportOddsAllPreMatchResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.NumberSchema
            fixture_id = schemas.NumberSchema
            market_id = schemas.NumberSchema
            bookmaker_id = schemas.NumberSchema
            label = schemas.StrSchema
            value = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class sort_order(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sort_order':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            market_description = schemas.StrSchema
            probability = schemas.StrSchema
            dp3 = schemas.StrSchema
            fractional = schemas.StrSchema
            american = schemas.StrSchema
            
            
            class winning(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'winning':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            stopped = schemas.BoolSchema
            
            
            class total(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'total':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class handicap(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'handicap':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class participants(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'participants':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            created_at = schemas.StrSchema
            updated_at = schemas.StrSchema
            
            
            class original_label(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'original_label':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            latest_bookmaker_update = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "fixture_id": fixture_id,
                "market_id": market_id,
                "bookmaker_id": bookmaker_id,
                "label": label,
                "value": value,
                "name": name,
                "sort_order": sort_order,
                "market_description": market_description,
                "probability": probability,
                "dp3": dp3,
                "fractional": fractional,
                "american": american,
                "winning": winning,
                "stopped": stopped,
                "total": total,
                "handicap": handicap,
                "participants": participants,
                "created_at": created_at,
                "updated_at": updated_at,
                "original_label": original_label,
                "latest_bookmaker_update": latest_bookmaker_update,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fixture_id"]) -> MetaOapg.properties.fixture_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["market_id"]) -> MetaOapg.properties.market_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bookmaker_id"]) -> MetaOapg.properties.bookmaker_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sort_order"]) -> MetaOapg.properties.sort_order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["market_description"]) -> MetaOapg.properties.market_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["probability"]) -> MetaOapg.properties.probability: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dp3"]) -> MetaOapg.properties.dp3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fractional"]) -> MetaOapg.properties.fractional: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["american"]) -> MetaOapg.properties.american: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["winning"]) -> MetaOapg.properties.winning: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stopped"]) -> MetaOapg.properties.stopped: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["handicap"]) -> MetaOapg.properties.handicap: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["participants"]) -> MetaOapg.properties.participants: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["original_label"]) -> MetaOapg.properties.original_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latest_bookmaker_update"]) -> MetaOapg.properties.latest_bookmaker_update: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "fixture_id", "market_id", "bookmaker_id", "label", "value", "name", "sort_order", "market_description", "probability", "dp3", "fractional", "american", "winning", "stopped", "total", "handicap", "participants", "created_at", "updated_at", "original_label", "latest_bookmaker_update", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fixture_id"]) -> typing.Union[MetaOapg.properties.fixture_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["market_id"]) -> typing.Union[MetaOapg.properties.market_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bookmaker_id"]) -> typing.Union[MetaOapg.properties.bookmaker_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sort_order"]) -> typing.Union[MetaOapg.properties.sort_order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["market_description"]) -> typing.Union[MetaOapg.properties.market_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["probability"]) -> typing.Union[MetaOapg.properties.probability, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dp3"]) -> typing.Union[MetaOapg.properties.dp3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fractional"]) -> typing.Union[MetaOapg.properties.fractional, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["american"]) -> typing.Union[MetaOapg.properties.american, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["winning"]) -> typing.Union[MetaOapg.properties.winning, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stopped"]) -> typing.Union[MetaOapg.properties.stopped, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["handicap"]) -> typing.Union[MetaOapg.properties.handicap, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["participants"]) -> typing.Union[MetaOapg.properties.participants, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["original_label"]) -> typing.Union[MetaOapg.properties.original_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latest_bookmaker_update"]) -> typing.Union[MetaOapg.properties.latest_bookmaker_update, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "fixture_id", "market_id", "bookmaker_id", "label", "value", "name", "sort_order", "market_description", "probability", "dp3", "fractional", "american", "winning", "stopped", "total", "handicap", "participants", "created_at", "updated_at", "original_label", "latest_bookmaker_update", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        fixture_id: typing.Union[MetaOapg.properties.fixture_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        market_id: typing.Union[MetaOapg.properties.market_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        bookmaker_id: typing.Union[MetaOapg.properties.bookmaker_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        sort_order: typing.Union[MetaOapg.properties.sort_order, None, str, schemas.Unset] = schemas.unset,
        market_description: typing.Union[MetaOapg.properties.market_description, str, schemas.Unset] = schemas.unset,
        probability: typing.Union[MetaOapg.properties.probability, str, schemas.Unset] = schemas.unset,
        dp3: typing.Union[MetaOapg.properties.dp3, str, schemas.Unset] = schemas.unset,
        fractional: typing.Union[MetaOapg.properties.fractional, str, schemas.Unset] = schemas.unset,
        american: typing.Union[MetaOapg.properties.american, str, schemas.Unset] = schemas.unset,
        winning: typing.Union[MetaOapg.properties.winning, None, str, schemas.Unset] = schemas.unset,
        stopped: typing.Union[MetaOapg.properties.stopped, bool, schemas.Unset] = schemas.unset,
        total: typing.Union[MetaOapg.properties.total, None, str, schemas.Unset] = schemas.unset,
        handicap: typing.Union[MetaOapg.properties.handicap, None, str, schemas.Unset] = schemas.unset,
        participants: typing.Union[MetaOapg.properties.participants, None, str, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, schemas.Unset] = schemas.unset,
        original_label: typing.Union[MetaOapg.properties.original_label, None, str, schemas.Unset] = schemas.unset,
        latest_bookmaker_update: typing.Union[MetaOapg.properties.latest_bookmaker_update, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportOddsAllPreMatchResponseDataItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            fixture_id=fixture_id,
            market_id=market_id,
            bookmaker_id=bookmaker_id,
            label=label,
            value=value,
            name=name,
            sort_order=sort_order,
            market_description=market_description,
            probability=probability,
            dp3=dp3,
            fractional=fractional,
            american=american,
            winning=winning,
            stopped=stopped,
            total=total,
            handicap=handicap,
            participants=participants,
            created_at=created_at,
            updated_at=updated_at,
            original_label=original_label,
            latest_bookmaker_update=latest_bookmaker_update,
            _configuration=_configuration,
            **kwargs,
        )
