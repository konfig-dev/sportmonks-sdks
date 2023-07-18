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


class SportTopScorersBySeasonIdResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class data(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                season_id = schemas.NumberSchema
                                player_id = schemas.NumberSchema
                                type_id = schemas.NumberSchema
                                team_id = schemas.NumberSchema
                                position = schemas.NumberSchema
                                total = schemas.NumberSchema
                                
                                
                                class points(
                                    schemas.StrBase,
                                    schemas.NoneBase,
                                    schemas.Schema,
                                    schemas.NoneStrMixin
                                ):
                                
                                
                                    def __new__(
                                        cls,
                                        *args: typing.Union[None, str, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'points':
                                        return super().__new__(
                                            cls,
                                            *args,
                                            _configuration=_configuration,
                                        )
                                __annotations__ = {
                                    "season_id": season_id,
                                    "player_id": player_id,
                                    "type_id": type_id,
                                    "team_id": team_id,
                                    "position": position,
                                    "total": total,
                                    "points": points,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["season_id"]) -> MetaOapg.properties.season_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["player_id"]) -> MetaOapg.properties.player_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["type_id"]) -> MetaOapg.properties.type_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["team_id"]) -> MetaOapg.properties.team_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["points"]) -> MetaOapg.properties.points: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["season_id", "player_id", "type_id", "team_id", "position", "total", "points", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["season_id"]) -> typing.Union[MetaOapg.properties.season_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["player_id"]) -> typing.Union[MetaOapg.properties.player_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["type_id"]) -> typing.Union[MetaOapg.properties.type_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["team_id"]) -> typing.Union[MetaOapg.properties.team_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> typing.Union[MetaOapg.properties.position, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> typing.Union[MetaOapg.properties.total, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["points"]) -> typing.Union[MetaOapg.properties.points, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["season_id", "player_id", "type_id", "team_id", "position", "total", "points", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            season_id: typing.Union[MetaOapg.properties.season_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                            player_id: typing.Union[MetaOapg.properties.player_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                            type_id: typing.Union[MetaOapg.properties.type_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                            team_id: typing.Union[MetaOapg.properties.team_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                            position: typing.Union[MetaOapg.properties.position, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                            total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                            points: typing.Union[MetaOapg.properties.points, None, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                season_id=season_id,
                                player_id=player_id,
                                type_id=type_id,
                                team_id=team_id,
                                position=position,
                                total=total,
                                points=points,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class pagination(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        count = schemas.NumberSchema
                        per_page = schemas.NumberSchema
                        current_page = schemas.NumberSchema
                        next_page = schemas.StrSchema
                        has_more = schemas.BoolSchema
                        __annotations__ = {
                            "count": count,
                            "per_page": per_page,
                            "current_page": current_page,
                            "next_page": next_page,
                            "has_more": has_more,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["per_page"]) -> MetaOapg.properties.per_page: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["current_page"]) -> MetaOapg.properties.current_page: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["next_page"]) -> MetaOapg.properties.next_page: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["has_more"]) -> MetaOapg.properties.has_more: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["count", "per_page", "current_page", "next_page", "has_more", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["per_page"]) -> typing.Union[MetaOapg.properties.per_page, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["current_page"]) -> typing.Union[MetaOapg.properties.current_page, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["next_page"]) -> typing.Union[MetaOapg.properties.next_page, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["has_more"]) -> typing.Union[MetaOapg.properties.has_more, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["count", "per_page", "current_page", "next_page", "has_more", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    per_page: typing.Union[MetaOapg.properties.per_page, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    current_page: typing.Union[MetaOapg.properties.current_page, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    next_page: typing.Union[MetaOapg.properties.next_page, str, schemas.Unset] = schemas.unset,
                    has_more: typing.Union[MetaOapg.properties.has_more, bool, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'pagination':
                    return super().__new__(
                        cls,
                        *args,
                        count=count,
                        per_page=per_page,
                        current_page=current_page,
                        next_page=next_page,
                        has_more=has_more,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class subscription(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                
                                
                                class meta(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        items = schemas.StrSchema
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'meta':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                
                                
                                class plans(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        
                                        class items(
                                            schemas.DictSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                
                                                class properties:
                                                    plan = schemas.StrSchema
                                                    sport = schemas.StrSchema
                                                    category = schemas.StrSchema
                                                    __annotations__ = {
                                                        "plan": plan,
                                                        "sport": sport,
                                                        "category": category,
                                                    }
                                            
                                            @typing.overload
                                            def __getitem__(self, name: typing_extensions.Literal["plan"]) -> MetaOapg.properties.plan: ...
                                            
                                            @typing.overload
                                            def __getitem__(self, name: typing_extensions.Literal["sport"]) -> MetaOapg.properties.sport: ...
                                            
                                            @typing.overload
                                            def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
                                            
                                            @typing.overload
                                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                            
                                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["plan", "sport", "category", ], str]):
                                                # dict_instance[name] accessor
                                                return super().__getitem__(name)
                                            
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: typing_extensions.Literal["plan"]) -> typing.Union[MetaOapg.properties.plan, schemas.Unset]: ...
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: typing_extensions.Literal["sport"]) -> typing.Union[MetaOapg.properties.sport, schemas.Unset]: ...
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
                                            
                                            @typing.overload
                                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                            
                                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["plan", "sport", "category", ], str]):
                                                return super().get_item_oapg(name)
                                            
                                        
                                            def __new__(
                                                cls,
                                                *args: typing.Union[dict, frozendict.frozendict, ],
                                                plan: typing.Union[MetaOapg.properties.plan, str, schemas.Unset] = schemas.unset,
                                                sport: typing.Union[MetaOapg.properties.sport, str, schemas.Unset] = schemas.unset,
                                                category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
                                                _configuration: typing.Optional[schemas.Configuration] = None,
                                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                            ) -> 'items':
                                                return super().__new__(
                                                    cls,
                                                    *args,
                                                    plan=plan,
                                                    sport=sport,
                                                    category=category,
                                                    _configuration=_configuration,
                                                    **kwargs,
                                                )
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'plans':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                
                                
                                class add_ons(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        items = schemas.StrSchema
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'add_ons':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                
                                
                                class widgets(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        items = schemas.StrSchema
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'widgets':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> MetaOapg.items:
                                        return super().__getitem__(i)
                                __annotations__ = {
                                    "meta": meta,
                                    "plans": plans,
                                    "add_ons": add_ons,
                                    "widgets": widgets,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["meta"]) -> MetaOapg.properties.meta: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["plans"]) -> MetaOapg.properties.plans: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["add_ons"]) -> MetaOapg.properties.add_ons: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["widgets"]) -> MetaOapg.properties.widgets: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["meta", "plans", "add_ons", "widgets", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union[MetaOapg.properties.meta, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["plans"]) -> typing.Union[MetaOapg.properties.plans, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["add_ons"]) -> typing.Union[MetaOapg.properties.add_ons, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["widgets"]) -> typing.Union[MetaOapg.properties.widgets, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["meta", "plans", "add_ons", "widgets", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            meta: typing.Union[MetaOapg.properties.meta, list, tuple, schemas.Unset] = schemas.unset,
                            plans: typing.Union[MetaOapg.properties.plans, list, tuple, schemas.Unset] = schemas.unset,
                            add_ons: typing.Union[MetaOapg.properties.add_ons, list, tuple, schemas.Unset] = schemas.unset,
                            widgets: typing.Union[MetaOapg.properties.widgets, list, tuple, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
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
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'subscription':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class rate_limit(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        resets_in_seconds = schemas.NumberSchema
                        remaining = schemas.NumberSchema
                        requested_entity = schemas.StrSchema
                        __annotations__ = {
                            "resets_in_seconds": resets_in_seconds,
                            "remaining": remaining,
                            "requested_entity": requested_entity,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["resets_in_seconds"]) -> MetaOapg.properties.resets_in_seconds: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["remaining"]) -> MetaOapg.properties.remaining: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["requested_entity"]) -> MetaOapg.properties.requested_entity: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["resets_in_seconds", "remaining", "requested_entity", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["resets_in_seconds"]) -> typing.Union[MetaOapg.properties.resets_in_seconds, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["remaining"]) -> typing.Union[MetaOapg.properties.remaining, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["requested_entity"]) -> typing.Union[MetaOapg.properties.requested_entity, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resets_in_seconds", "remaining", "requested_entity", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    resets_in_seconds: typing.Union[MetaOapg.properties.resets_in_seconds, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    remaining: typing.Union[MetaOapg.properties.remaining, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                    requested_entity: typing.Union[MetaOapg.properties.requested_entity, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'rate_limit':
                    return super().__new__(
                        cls,
                        *args,
                        resets_in_seconds=resets_in_seconds,
                        remaining=remaining,
                        requested_entity=requested_entity,
                        _configuration=_configuration,
                        **kwargs,
                    )
            timezone = schemas.StrSchema
            __annotations__ = {
                "data": data,
                "pagination": pagination,
                "subscription": subscription,
                "rate_limit": rate_limit,
                "timezone": timezone,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pagination"]) -> MetaOapg.properties.pagination: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscription"]) -> MetaOapg.properties.subscription: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate_limit"]) -> MetaOapg.properties.rate_limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timezone"]) -> MetaOapg.properties.timezone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "pagination", "subscription", "rate_limit", "timezone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pagination"]) -> typing.Union[MetaOapg.properties.pagination, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscription"]) -> typing.Union[MetaOapg.properties.subscription, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate_limit"]) -> typing.Union[MetaOapg.properties.rate_limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timezone"]) -> typing.Union[MetaOapg.properties.timezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "pagination", "subscription", "rate_limit", "timezone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union[MetaOapg.properties.data, list, tuple, schemas.Unset] = schemas.unset,
        pagination: typing.Union[MetaOapg.properties.pagination, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        subscription: typing.Union[MetaOapg.properties.subscription, list, tuple, schemas.Unset] = schemas.unset,
        rate_limit: typing.Union[MetaOapg.properties.rate_limit, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        timezone: typing.Union[MetaOapg.properties.timezone, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportTopScorersBySeasonIdResponse':
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
