# sportmonks-python-sdk@0.1.0
Surpass the competition with superior sports data


## Requirements

Python >=3.7

## Installing

```sh
pip install sportmonks-python-sdk==0.1.0
```

## Getting Started

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="v3",
    sport="football",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    all_response = sportmonks.cities.all(
        version="v3",  # optional
    )
    pprint(all_response.body)
    pprint(all_response.body["data"])
    pprint(all_response.body["pagination"])
    pprint(all_response.body["subscription"])
    pprint(all_response.body["rate_limit"])
    pprint(all_response.body["timezone"])
    pprint(all_response.headers)
    pprint(all_response.status)
    pprint(all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling CitiesApi.all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="v3",
    sport="football",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)


async def main():
    try:
        # All
        all_response = await sportmonks.cities.aall(
            version="v3",  # optional
        )
        pprint(all_response.body)
        pprint(all_response.body["data"])
        pprint(all_response.body["pagination"])
        pprint(all_response.body["subscription"])
        pprint(all_response.body["rate_limit"])
        pprint(all_response.body["timezone"])
        pprint(all_response.headers)
        pprint(all_response.status)
        pprint(all_response.round_trip_time)
    except ApiException as e:
        print("Exception when calling CitiesApi.all: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```


## Documentation for API Endpoints

All URIs are relative to *https://api.sportmonks.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CitiesApi* | [**all**](docs/apis/tags/CitiesApi.md#all) | **GET** /{version}/core/cities | All
*CitiesApi* | [**get_by_id**](docs/apis/tags/CitiesApi.md#get_by_id) | **GET** /{version}/core/cities/{cityId} | By ID
*CitiesApi* | [**search**](docs/apis/tags/CitiesApi.md#search) | **GET** /{version}/core/cities/search/{name} | Search
*ContinentsApi* | [**all**](docs/apis/tags/ContinentsApi.md#all) | **GET** /{version}/core/continents | All
*ContinentsApi* | [**get_by_id**](docs/apis/tags/ContinentsApi.md#get_by_id) | **GET** /{version}/core/continents/{continentId} | By ID
*CountriesApi* | [**all**](docs/apis/tags/CountriesApi.md#all) | **GET** /{version}/core/countries | All
*CountriesApi* | [**get_by_id**](docs/apis/tags/CountriesApi.md#get_by_id) | **GET** /{version}/core/countries/{countryId} | By ID
*CountriesApi* | [**search**](docs/apis/tags/CountriesApi.md#search) | **GET** /{version}/core/countries/search/{name} | Search
*MyApi* | [**enrichments**](docs/apis/tags/MyApi.md#enrichments) | **GET** /{version}/my/enrichments | All
*MyApi* | [**leagues**](docs/apis/tags/MyApi.md#leagues) | **GET** /{version}/my/leagues | All
*MyApi* | [**resources**](docs/apis/tags/MyApi.md#resources) | **GET** /{version}/my/resources | All
*OddsApi* | [**bookmaker_by_id**](docs/apis/tags/OddsApi.md#bookmaker_by_id) | **GET** /{version}/odds/bookmakers/{bookmakerId} | By ID
*OddsApi* | [**bookmakers_all**](docs/apis/tags/OddsApi.md#bookmakers_all) | **GET** /{version}/odds/bookmakers | All
*OddsApi* | [**bookmakers_by_fixture_id**](docs/apis/tags/OddsApi.md#bookmakers_by_fixture_id) | **GET** /{version}/odds/bookmakers/fixtures/{fixtureId} | By Fixture ID
*OddsApi* | [**bookmakers_mapping_by_fixture_id**](docs/apis/tags/OddsApi.md#bookmakers_mapping_by_fixture_id) | **GET** /{version}/odds/bookmakers/fixtures/{fixtureId}/mapping | Mapping by Fixture ID
*OddsApi* | [**bookmakers_search**](docs/apis/tags/OddsApi.md#bookmakers_search) | **GET** /{version}/odds/bookmakers/search/{name} | Search
*OddsApi* | [**fixtures_upcoming_by_market_id**](docs/apis/tags/OddsApi.md#fixtures_upcoming_by_market_id) | **GET** /{version}/{sport}/fixtures/upcoming/markets/{marketId} | Upcoming Fixtures by Market ID
*OddsApi* | [**market_by_id**](docs/apis/tags/OddsApi.md#market_by_id) | **GET** /{version}/odds/markets/{marketId} | By ID
*OddsApi* | [**markets_all**](docs/apis/tags/OddsApi.md#markets_all) | **GET** /{version}/odds/markets | All
*OddsApi* | [**markets_search**](docs/apis/tags/OddsApi.md#markets_search) | **GET** /{version}/odds/markets/search/{name} | Search
*RegionsApi* | [**all**](docs/apis/tags/RegionsApi.md#all) | **GET** /{version}/core/regions | All
*RegionsApi* | [**get_by_id**](docs/apis/tags/RegionsApi.md#get_by_id) | **GET** /{version}/core/regions/{regionId} | By ID
*RegionsApi* | [**search**](docs/apis/tags/RegionsApi.md#search) | **GET** /{version}/core/regions/search/{name} | Search
*SportApi* | [**coach_by_id**](docs/apis/tags/SportApi.md#coach_by_id) | **GET** /{version}/{sport}/coaches/{coachId} | By ID
*SportApi* | [**coaches_all**](docs/apis/tags/SportApi.md#coaches_all) | **GET** /{version}/{sport}/coaches | All
*SportApi* | [**coaches_by_country_id**](docs/apis/tags/SportApi.md#coaches_by_country_id) | **GET** /{version}/{sport}/coaches/countries/{countryId} | By Country ID
*SportApi* | [**coaches_latest**](docs/apis/tags/SportApi.md#coaches_latest) | **GET** /{version}/{sport}/coaches/latest | Last updated
*SportApi* | [**coaches_search**](docs/apis/tags/SportApi.md#coaches_search) | **GET** /{version}/{sport}/coaches/search/{name} | Search
*SportApi* | [**commentaries_all**](docs/apis/tags/SportApi.md#commentaries_all) | **GET** /{version}/{sport}/commentaries | All
*SportApi* | [**commentaries_by_fixture_id**](docs/apis/tags/SportApi.md#commentaries_by_fixture_id) | **GET** /{version}/{sport}/commentaries/fixtures/{fixtureId} | By Fixture ID
*SportApi* | [**fixture_by_date_range_for_team**](docs/apis/tags/SportApi.md#fixture_by_date_range_for_team) | **GET** /{version}/{sport}/fixtures/between/{startDate}/{endDate}/{teamId} | By Date Range for Team
*SportApi* | [**fixture_by_id**](docs/apis/tags/SportApi.md#fixture_by_id) | **GET** /{version}/{sport}/fixtures/{fixtureId} | Fixture ID
*SportApi* | [**fixtures_all**](docs/apis/tags/SportApi.md#fixtures_all) | **GET** /{version}/{sport}/fixtures | All
*SportApi* | [**fixtures_by_date**](docs/apis/tags/SportApi.md#fixtures_by_date) | **GET** /{version}/{sport}/fixtures/date/{date} | By Date
*SportApi* | [**fixtures_by_date_range**](docs/apis/tags/SportApi.md#fixtures_by_date_range) | **GET** /{version}/{sport}/fixtures/between/{startDate}/{endDate} | By Date Range
*SportApi* | [**fixtures_by_ids**](docs/apis/tags/SportApi.md#fixtures_by_ids) | **GET** /{version}/{sport}/fixtures/multi/{fixtureIds} | By IDs
*SportApi* | [**fixtures_head_to_head**](docs/apis/tags/SportApi.md#fixtures_head_to_head) | **GET** /{version}/{sport}/fixtures/head-to-head/{firstTeam}/{secondTeam} | Head to Head
*SportApi* | [**fixtures_latest**](docs/apis/tags/SportApi.md#fixtures_latest) | **GET** /{version}/{sport}/fixtures/latest | Last Updated
*SportApi* | [**fixtures_search**](docs/apis/tags/SportApi.md#fixtures_search) | **GET** /{version}/{sport}/fixtures/search/{name} | Search
*SportApi* | [**league_by_id**](docs/apis/tags/SportApi.md#league_by_id) | **GET** /{version}/{sport}/leagues/{leagueId} | By ID
*SportApi* | [**league_enrichments**](docs/apis/tags/SportApi.md#league_enrichments) | **GET** /{version}/{sport}/leagues/{leagueId}/includes | Enrichments
*SportApi* | [**league_shirts**](docs/apis/tags/SportApi.md#league_shirts) | **GET** /{version}/{sport}/leagues/{leagueId}/jerseys | Shirts By League ID
*SportApi* | [**leagues_all**](docs/apis/tags/SportApi.md#leagues_all) | **GET** /{version}/{sport}/leagues | All
*SportApi* | [**leagues_by_country_id**](docs/apis/tags/SportApi.md#leagues_by_country_id) | **GET** /{version}/{sport}/leagues/countries/{countryId} | By Country ID
*SportApi* | [**leagues_by_date**](docs/apis/tags/SportApi.md#leagues_by_date) | **GET** /{version}/{sport}/leagues/date/{date} | By Date
*SportApi* | [**leagues_by_team_id**](docs/apis/tags/SportApi.md#leagues_by_team_id) | **GET** /{version}/{sport}/teams/{teamId}/leagues | Leagues By Team ID
*SportApi* | [**leagues_current_by_team_id**](docs/apis/tags/SportApi.md#leagues_current_by_team_id) | **GET** /{version}/{sport}/teams/{teamId}/leagues/current | Current Leagues By Team ID
*SportApi* | [**leagues_live**](docs/apis/tags/SportApi.md#leagues_live) | **GET** /{version}/{sport}/leagues/live | Live
*SportApi* | [**leagues_search**](docs/apis/tags/SportApi.md#leagues_search) | **GET** /{version}/{sport}/leagues/search/{name} | Search
*SportApi* | [**livescores_all**](docs/apis/tags/SportApi.md#livescores_all) | **GET** /{version}/{sport}/livescores | All
*SportApi* | [**livescores_all_in_play**](docs/apis/tags/SportApi.md#livescores_all_in_play) | **GET** /{version}/{sport}/livescores/inplay | All In-play
*SportApi* | [**livescores_latest**](docs/apis/tags/SportApi.md#livescores_latest) | **GET** /{version}/{sport}/livescores/latest | Last Updated In-play
*SportApi* | [**news_all_post_match**](docs/apis/tags/SportApi.md#news_all_post_match) | **GET** /{version}/{sport}/news/post-match | All Post Match
*SportApi* | [**news_all_pre_match**](docs/apis/tags/SportApi.md#news_all_pre_match) | **GET** /{version}/{sport}/news/pre-match | All Pre-match
*SportApi* | [**news_post_match_by_season_id**](docs/apis/tags/SportApi.md#news_post_match_by_season_id) | **GET** /{version}/{sport}/news/post-match/seasons/{seasonId} | Post Match by Season ID
*SportApi* | [**news_pre_match_by_season_id**](docs/apis/tags/SportApi.md#news_pre_match_by_season_id) | **GET** /{version}/{sport}/news/pre-match/seasons/{seasonId} | Pre-match By Season ID
*SportApi* | [**news_upcoming_post_match**](docs/apis/tags/SportApi.md#news_upcoming_post_match) | **GET** /{version}/{sport}/news/post-match/upcoming | Upcoming Post Match
*SportApi* | [**news_upcoming_pre_match**](docs/apis/tags/SportApi.md#news_upcoming_pre_match) | **GET** /{version}/{sport}/news/pre-match/upcoming | Upcoming Pre-match
*SportApi* | [**odds_all_in_play**](docs/apis/tags/SportApi.md#odds_all_in_play) | **GET** /{version}/{sport}/odds/inplay | All In-play
*SportApi* | [**odds_all_pre_match**](docs/apis/tags/SportApi.md#odds_all_pre_match) | **GET** /{version}/{sport}/odds/pre-match | All Pre-match
*SportApi* | [**odds_in_play_by_fixture_and_bookmaker_id**](docs/apis/tags/SportApi.md#odds_in_play_by_fixture_and_bookmaker_id) | **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}/bookmakers/{bookmakerId} | In-play by Fixture and Bookmaker ID
*SportApi* | [**odds_in_play_by_fixture_and_market_id**](docs/apis/tags/SportApi.md#odds_in_play_by_fixture_and_market_id) | **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}/markets/{marketId} | In-play by Fixture and Market ID
*SportApi* | [**odds_in_play_by_fixture_id**](docs/apis/tags/SportApi.md#odds_in_play_by_fixture_id) | **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId} | In-play by Fixture ID
*SportApi* | [**odds_latest_in_play**](docs/apis/tags/SportApi.md#odds_latest_in_play) | **GET** /{version}/{sport}/odds/inplay/latest | Latest In-play
*SportApi* | [**odds_latest_pre_match**](docs/apis/tags/SportApi.md#odds_latest_pre_match) | **GET** /{version}/{sport}/odds/pre-match/latest | Last Updated Pre-match
*SportApi* | [**odds_pre_match_by_fixture_and_bookmaker_id**](docs/apis/tags/SportApi.md#odds_pre_match_by_fixture_and_bookmaker_id) | **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}/bookmakers/{bookmakerId} | Pre-match by Fixture and Bookmaker ID
*SportApi* | [**odds_pre_match_by_fixture_and_market_id**](docs/apis/tags/SportApi.md#odds_pre_match_by_fixture_and_market_id) | **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}/markets/{marketId} | Pre-match by Fixture and Market ID
*SportApi* | [**odds_pre_match_by_fixture_id**](docs/apis/tags/SportApi.md#odds_pre_match_by_fixture_id) | **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId} | Pre-match by Fixture ID
*SportApi* | [**player_by_id**](docs/apis/tags/SportApi.md#player_by_id) | **GET** /{version}/{sport}/players/{playerId} | By ID
*SportApi* | [**players_all**](docs/apis/tags/SportApi.md#players_all) | **GET** /{version}/{sport}/players | All
*SportApi* | [**players_by_country_id**](docs/apis/tags/SportApi.md#players_by_country_id) | **GET** /{version}/{sport}/players/countries/{countryId} | By Country ID
*SportApi* | [**players_latest**](docs/apis/tags/SportApi.md#players_latest) | **GET** /{version}/{sport}/players/latest | Latest Updated
*SportApi* | [**players_search**](docs/apis/tags/SportApi.md#players_search) | **GET** /{version}/{sport}/players/search/{name} | Search
*SportApi* | [**predictions_all**](docs/apis/tags/SportApi.md#predictions_all) | **GET** /{version}/{sport}/predictions/probabilities | All
*SportApi* | [**predictions_all_value_bets**](docs/apis/tags/SportApi.md#predictions_all_value_bets) | **GET** /{version}/{sport}/predictions/value-bets | All Value Bets
*SportApi* | [**predictions_by_fixture_id**](docs/apis/tags/SportApi.md#predictions_by_fixture_id) | **GET** /{version}/{sport}/predictions/probabilities/fixtures/{fixtureId} | By Fixture ID
*SportApi* | [**predictions_value_bets_by_fixture_id**](docs/apis/tags/SportApi.md#predictions_value_bets_by_fixture_id) | **GET** /{version}/{sport}/predictions/value-bets/fixtures/{fixtureId} | Value Bets by Fixture ID
*SportApi* | [**referee_by_id**](docs/apis/tags/SportApi.md#referee_by_id) | **GET** /{version}/{sport}/referees/{refereeId} | By ID
*SportApi* | [**referees_all**](docs/apis/tags/SportApi.md#referees_all) | **GET** /{version}/{sport}/referees | All
*SportApi* | [**referees_by_country_id**](docs/apis/tags/SportApi.md#referees_by_country_id) | **GET** /{version}/{sport}/referees/countries/{countryId} | By Country ID
*SportApi* | [**referees_by_season_id**](docs/apis/tags/SportApi.md#referees_by_season_id) | **GET** /{version}/{sport}/referees/seasons/{seasonId} | By Season ID
*SportApi* | [**referees_search**](docs/apis/tags/SportApi.md#referees_search) | **GET** /{version}/{sport}/referees/search/{name} | Search
*SportApi* | [**rivals_all**](docs/apis/tags/SportApi.md#rivals_all) | **GET** /{version}/{sport}/rivals | All
*SportApi* | [**rivals_by_team_id**](docs/apis/tags/SportApi.md#rivals_by_team_id) | **GET** /{version}/{sport}/rivals/teams/{teamId} | By Team ID
*SportApi* | [**round_by_id**](docs/apis/tags/SportApi.md#round_by_id) | **GET** /{version}/{sport}/rounds/{roundId} | By ID
*SportApi* | [**rounds_all**](docs/apis/tags/SportApi.md#rounds_all) | **GET** /{version}/{sport}/rounds | All
*SportApi* | [**rounds_by_season_id**](docs/apis/tags/SportApi.md#rounds_by_season_id) | **GET** /{version}/{sport}/rounds/seasons/{seasonId} | Season ID
*SportApi* | [**rounds_search**](docs/apis/tags/SportApi.md#rounds_search) | **GET** /{version}/{sport}/rounds/search/{name} | Search
*SportApi* | [**schedules_by_season_id**](docs/apis/tags/SportApi.md#schedules_by_season_id) | **GET** /{version}/{sport}/schedules/seasons/{seasonId} | By Season ID
*SportApi* | [**schedules_by_team_and_season_id**](docs/apis/tags/SportApi.md#schedules_by_team_and_season_id) | **GET** /{version}/{sport}/schedules/seasons/{seasonId}/teams/{teamId} | By Team and Season ID
*SportApi* | [**schedules_by_team_id**](docs/apis/tags/SportApi.md#schedules_by_team_id) | **GET** /{version}/{sport}/schedules/teams/{teamId} | By Team ID
*SportApi* | [**season_by_id**](docs/apis/tags/SportApi.md#season_by_id) | **GET** /{version}/{sport}/seasons/{seasonId} | By ID
*SportApi* | [**seasons_all**](docs/apis/tags/SportApi.md#seasons_all) | **GET** /{version}/{sport}/seasons | All
*SportApi* | [**seasons_by_team_id**](docs/apis/tags/SportApi.md#seasons_by_team_id) | **GET** /{version}/{sport}/seasons/teams/{teamId} | By Team ID
*SportApi* | [**seasons_search**](docs/apis/tags/SportApi.md#seasons_search) | **GET** /{version}/{sport}/seasons/search/{name} | Search
*SportApi* | [**squads_by_season_and_team_id**](docs/apis/tags/SportApi.md#squads_by_season_and_team_id) | **GET** /{version}/{sport}/squads/seasons/{seasonId}/teams/{teamId} | By Season and Team ID
*SportApi* | [**squads_by_team_id**](docs/apis/tags/SportApi.md#squads_by_team_id) | **GET** /{version}/{sport}/squads/teams/{teamId} | By Team ID
*SportApi* | [**stage_by_id**](docs/apis/tags/SportApi.md#stage_by_id) | **GET** /{version}/{sport}/stages/{stageId} | By ID
*SportApi* | [**stages_all**](docs/apis/tags/SportApi.md#stages_all) | **GET** /{version}/{sport}/stages | All
*SportApi* | [**stages_by_season_id**](docs/apis/tags/SportApi.md#stages_by_season_id) | **GET** /{version}/{sport}/stages/seasons/{seasonId} | By Season ID
*SportApi* | [**stages_search**](docs/apis/tags/SportApi.md#stages_search) | **GET** /{version}/{sport}/stages/search/{name} | Search
*SportApi* | [**standing_corrections_by_season_id**](docs/apis/tags/SportApi.md#standing_corrections_by_season_id) | **GET** /{version}/{sport}/standings/corrections/seasons/{seasonId} | Correction by Season ID
*SportApi* | [**standings_all**](docs/apis/tags/SportApi.md#standings_all) | **GET** /{version}/{sport}/standings | All
*SportApi* | [**standings_by_round_id**](docs/apis/tags/SportApi.md#standings_by_round_id) | **GET** /{version}/{sport}/standings/rounds/{roundId} | By Round ID
*SportApi* | [**standings_by_season_id**](docs/apis/tags/SportApi.md#standings_by_season_id) | **GET** /{version}/{sport}/standings/seasons/{seasonId} | By Season ID
*SportApi* | [**standings_live_by_league_id**](docs/apis/tags/SportApi.md#standings_live_by_league_id) | **GET** /{version}/{sport}/standings/live/leagues/{leagueId} | By League ID
*SportApi* | [**state_by_id**](docs/apis/tags/SportApi.md#state_by_id) | **GET** /{version}/{sport}/states/{stateId} | By ID
*SportApi* | [**states_by_sport**](docs/apis/tags/SportApi.md#states_by_sport) | **GET** /{version}/{sport}/states | By Sport
*SportApi* | [**teams_all**](docs/apis/tags/SportApi.md#teams_all) | **GET** /{version}/{sport}/teams | All
*SportApi* | [**teams_by_country_id**](docs/apis/tags/SportApi.md#teams_by_country_id) | **GET** /{version}/{sport}/teams/countries/{countryId} | By Country ID
*SportApi* | [**teams_by_id**](docs/apis/tags/SportApi.md#teams_by_id) | **GET** /{version}/{sport}/teams/{teamId} | By ID
*SportApi* | [**teams_by_season_id**](docs/apis/tags/SportApi.md#teams_by_season_id) | **GET** /{version}/{sport}/teams/seasons/{seasonId} | By Season ID
*SportApi* | [**teams_search**](docs/apis/tags/SportApi.md#teams_search) | **GET** /{version}/{sport}/teams/search/{name} | Search
*SportApi* | [**top_scorers_by_season_id**](docs/apis/tags/SportApi.md#top_scorers_by_season_id) | **GET** /{version}/{sport}/topscorers/seasons/{seasonId} | By Season ID
*SportApi* | [**top_scorers_by_stage_id**](docs/apis/tags/SportApi.md#top_scorers_by_stage_id) | **GET** /{version}/{sport}/topscorers/stages/{stageId} | By Stage ID
*SportApi* | [**tranfers_by_date_range**](docs/apis/tags/SportApi.md#tranfers_by_date_range) | **GET** /{version}/{sport}/transfers/between/{startDate}/{endDate} | By Date Range
*SportApi* | [**transfer_by_id**](docs/apis/tags/SportApi.md#transfer_by_id) | **GET** /{version}/{sport}/transfers/{transferId} | By ID
*SportApi* | [**transfers_all**](docs/apis/tags/SportApi.md#transfers_all) | **GET** /{version}/{sport}/transfers | All
*SportApi* | [**transfers_by_player_id**](docs/apis/tags/SportApi.md#transfers_by_player_id) | **GET** /{version}/{sport}/transfers/players/{playerId} | By Player ID
*SportApi* | [**transfers_by_team_id**](docs/apis/tags/SportApi.md#transfers_by_team_id) | **GET** /{version}/{sport}/transfers/teams/{teamId} | By Team ID
*SportApi* | [**transfers_latest**](docs/apis/tags/SportApi.md#transfers_latest) | **GET** /{version}/{sport}/transfers/latest | Last Updated
*SportApi* | [**tv_station_by_id**](docs/apis/tags/SportApi.md#tv_station_by_id) | **GET** /{version}/{sport}/tv-stations/{tvStationId} | By ID
*SportApi* | [**tv_stations_all**](docs/apis/tags/SportApi.md#tv_stations_all) | **GET** /{version}/{sport}/tv-stations | All
*SportApi* | [**tv_stations_by_fixture_id**](docs/apis/tags/SportApi.md#tv_stations_by_fixture_id) | **GET** /{version}/{sport}/tv-stations/fixtures/{fixtureId} | By Fixture ID
*SportApi* | [**venue_by_id**](docs/apis/tags/SportApi.md#venue_by_id) | **GET** /{version}/{sport}/venues/{venueId} | By ID
*SportApi* | [**venues_all**](docs/apis/tags/SportApi.md#venues_all) | **GET** /{version}/{sport}/venues | All
*SportApi* | [**venues_by_season_id**](docs/apis/tags/SportApi.md#venues_by_season_id) | **GET** /{version}/{sport}/venues/seasons/{seasonId} | By Season ID
*SportApi* | [**venues_search**](docs/apis/tags/SportApi.md#venues_search) | **GET** /{version}/{sport}/venues/search/{name} | Search
*TypesApi* | [**all**](docs/apis/tags/TypesApi.md#all) | **GET** /{version}/core/types | All
*TypesApi* | [**get_by_id**](docs/apis/tags/TypesApi.md#get_by_id) | **GET** /{version}/core/types/{typeId} | By ID


## Author
This Python package is automatically generated by [Konfig](https://konfigthis.com)
