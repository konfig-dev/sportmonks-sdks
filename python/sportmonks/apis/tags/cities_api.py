# coding: utf-8

"""
    SportMonks

    Surpass the competition with superior sports data

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from sportmonks.paths.version_core_cities.get import All
from sportmonks.paths.version_core_cities_city_id.get import GetById
from sportmonks.paths.version_core_cities_search_name.get import Search


class CitiesApi(
    All,
    GetById,
    Search,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
