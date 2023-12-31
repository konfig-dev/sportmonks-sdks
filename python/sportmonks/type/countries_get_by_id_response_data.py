# coding: utf-8

"""
    SportMonks

    Surpass the competition with superior sports data

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal

from sportmonks.type.countries_get_by_id_response_data_borders import CountriesGetByIdResponseDataBorders

class RequiredCountriesGetByIdResponseData(TypedDict):
    pass

class OptionalCountriesGetByIdResponseData(TypedDict, total=False):
    id: typing.Union[int, float]

    continent_id: typing.Union[int, float]

    name: str

    official_name: str

    fifa_name: str

    iso2: str

    iso3: str

    latitude: str

    longitude: str

    borders: CountriesGetByIdResponseDataBorders

    image_path: str

class CountriesGetByIdResponseData(RequiredCountriesGetByIdResponseData, OptionalCountriesGetByIdResponseData):
    pass
