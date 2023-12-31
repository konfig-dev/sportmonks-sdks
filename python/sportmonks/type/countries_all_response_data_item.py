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

from sportmonks.type.countries_all_response_data_item_borders import CountriesAllResponseDataItemBorders

class RequiredCountriesAllResponseDataItem(TypedDict):
    pass

class OptionalCountriesAllResponseDataItem(TypedDict, total=False):
    id: typing.Union[int, float]

    continent_id: typing.Union[int, float]

    name: str

    official_name: str

    fifa_name: typing.Optional[str]

    iso2: str

    iso3: str

    latitude: typing.Optional[str]

    longitude: typing.Optional[str]

    borders: CountriesAllResponseDataItemBorders

    image_path: str

class CountriesAllResponseDataItem(RequiredCountriesAllResponseDataItem, OptionalCountriesAllResponseDataItem):
    pass
