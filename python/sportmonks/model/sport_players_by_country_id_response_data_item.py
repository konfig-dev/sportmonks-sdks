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


class SportPlayersByCountryIdResponseDataItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.NumberSchema
            sport_id = schemas.NumberSchema
            country_id = schemas.NumberSchema
            nationality_id = schemas.NumberSchema
            
            
            class city_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'city_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class position_id(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.NumberSchema
                    
                    
                    class one_of_1(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'one_of_1':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.one_of_0,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'position_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class detailed_position_id(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class one_of_0(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'one_of_0':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    one_of_1 = schemas.NumberSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.one_of_0,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'detailed_position_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            type_id = schemas.NumberSchema
            common_name = schemas.StrSchema
            firstname = schemas.StrSchema
            lastname = schemas.StrSchema
            name = schemas.StrSchema
            display_name = schemas.StrSchema
            image_path = schemas.StrSchema
            
            
            class height(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.NumberSchema
                    
                    
                    class one_of_1(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'one_of_1':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.one_of_0,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'height':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class weight(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    one_of_0 = schemas.NumberSchema
                    
                    
                    class one_of_1(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'one_of_1':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.one_of_0,
                            cls.one_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'weight':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            date_of_birth = schemas.StrSchema
            gender = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "sport_id": sport_id,
                "country_id": country_id,
                "nationality_id": nationality_id,
                "city_id": city_id,
                "position_id": position_id,
                "detailed_position_id": detailed_position_id,
                "type_id": type_id,
                "common_name": common_name,
                "firstname": firstname,
                "lastname": lastname,
                "name": name,
                "display_name": display_name,
                "image_path": image_path,
                "height": height,
                "weight": weight,
                "date_of_birth": date_of_birth,
                "gender": gender,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sport_id"]) -> MetaOapg.properties.sport_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_id"]) -> MetaOapg.properties.country_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nationality_id"]) -> MetaOapg.properties.nationality_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city_id"]) -> MetaOapg.properties.city_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position_id"]) -> MetaOapg.properties.position_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detailed_position_id"]) -> MetaOapg.properties.detailed_position_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type_id"]) -> MetaOapg.properties.type_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["common_name"]) -> MetaOapg.properties.common_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstname"]) -> MetaOapg.properties.firstname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastname"]) -> MetaOapg.properties.lastname: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_path"]) -> MetaOapg.properties.image_path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["weight"]) -> MetaOapg.properties.weight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_of_birth"]) -> MetaOapg.properties.date_of_birth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "country_id", "nationality_id", "city_id", "position_id", "detailed_position_id", "type_id", "common_name", "firstname", "lastname", "name", "display_name", "image_path", "height", "weight", "date_of_birth", "gender", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sport_id"]) -> typing.Union[MetaOapg.properties.sport_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_id"]) -> typing.Union[MetaOapg.properties.country_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nationality_id"]) -> typing.Union[MetaOapg.properties.nationality_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city_id"]) -> typing.Union[MetaOapg.properties.city_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position_id"]) -> typing.Union[MetaOapg.properties.position_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detailed_position_id"]) -> typing.Union[MetaOapg.properties.detailed_position_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type_id"]) -> typing.Union[MetaOapg.properties.type_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["common_name"]) -> typing.Union[MetaOapg.properties.common_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstname"]) -> typing.Union[MetaOapg.properties.firstname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastname"]) -> typing.Union[MetaOapg.properties.lastname, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_path"]) -> typing.Union[MetaOapg.properties.image_path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> typing.Union[MetaOapg.properties.height, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["weight"]) -> typing.Union[MetaOapg.properties.weight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_of_birth"]) -> typing.Union[MetaOapg.properties.date_of_birth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> typing.Union[MetaOapg.properties.gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "sport_id", "country_id", "nationality_id", "city_id", "position_id", "detailed_position_id", "type_id", "common_name", "firstname", "lastname", "name", "display_name", "image_path", "height", "weight", "date_of_birth", "gender", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sport_id: typing.Union[MetaOapg.properties.sport_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        country_id: typing.Union[MetaOapg.properties.country_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        nationality_id: typing.Union[MetaOapg.properties.nationality_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        city_id: typing.Union[MetaOapg.properties.city_id, None, str, schemas.Unset] = schemas.unset,
        position_id: typing.Union[MetaOapg.properties.position_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        detailed_position_id: typing.Union[MetaOapg.properties.detailed_position_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        type_id: typing.Union[MetaOapg.properties.type_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        common_name: typing.Union[MetaOapg.properties.common_name, str, schemas.Unset] = schemas.unset,
        firstname: typing.Union[MetaOapg.properties.firstname, str, schemas.Unset] = schemas.unset,
        lastname: typing.Union[MetaOapg.properties.lastname, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        image_path: typing.Union[MetaOapg.properties.image_path, str, schemas.Unset] = schemas.unset,
        height: typing.Union[MetaOapg.properties.height, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        weight: typing.Union[MetaOapg.properties.weight, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        date_of_birth: typing.Union[MetaOapg.properties.date_of_birth, str, schemas.Unset] = schemas.unset,
        gender: typing.Union[MetaOapg.properties.gender, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SportPlayersByCountryIdResponseDataItem':
        return super().__new__(
            cls,
            *args,
            id=id,
            sport_id=sport_id,
            country_id=country_id,
            nationality_id=nationality_id,
            city_id=city_id,
            position_id=position_id,
            detailed_position_id=detailed_position_id,
            type_id=type_id,
            common_name=common_name,
            firstname=firstname,
            lastname=lastname,
            name=name,
            display_name=display_name,
            image_path=image_path,
            height=height,
            weight=weight,
            date_of_birth=date_of_birth,
            gender=gender,
            _configuration=_configuration,
            **kwargs,
        )
