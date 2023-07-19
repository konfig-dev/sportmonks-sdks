# coding: utf-8

"""
    SportMonks

    Surpass the competition with superior sports data

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from sportmonks import Sportmonks

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        sportmonks = Sportmonks(
            version="VERSION",
            sport="SPORT",
            api_key=os.environ["SPORTMONKS_API_TOKEN"],
        )
        self.assertIsNotNone(sportmonks)

    def test_simple(self):
        sportmonks = Sportmonks(
            version="v3",
            sport="football",
            api_key=os.environ["SPORTMONKS_API_TOKEN"],
        )
        cities = sportmonks.cities.all()
        pprint(cities.body)

        teams = sportmonks.sport.teams_all()
        if "data" not in teams.body:
            raise Exception('Missing "data"')
        first_team = teams.body["data"]

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
