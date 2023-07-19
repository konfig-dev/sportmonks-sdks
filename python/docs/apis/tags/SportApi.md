<a name="__pageTop"></a>
# sportmonks.apis.tags.sport_api.SportApi

All URIs are relative to *https://api.sportmonks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**coach_by_id**](#coach_by_id) | **get** /{version}/{sport}/coaches/{coachId} | By ID
[**coaches_all**](#coaches_all) | **get** /{version}/{sport}/coaches | All
[**coaches_by_country_id**](#coaches_by_country_id) | **get** /{version}/{sport}/coaches/countries/{countryId} | By Country ID
[**coaches_latest**](#coaches_latest) | **get** /{version}/{sport}/coaches/latest | Last updated
[**coaches_search**](#coaches_search) | **get** /{version}/{sport}/coaches/search/{name} | Search
[**commentaries_all**](#commentaries_all) | **get** /{version}/{sport}/commentaries | All
[**commentaries_by_fixture_id**](#commentaries_by_fixture_id) | **get** /{version}/{sport}/commentaries/fixtures/{fixtureId} | By Fixture ID
[**fixture_by_date_range_for_team**](#fixture_by_date_range_for_team) | **get** /{version}/{sport}/fixtures/between/{startDate}/{endDate}/{teamId} | By Date Range for Team
[**fixture_by_id**](#fixture_by_id) | **get** /{version}/{sport}/fixtures/{fixtureId} | Fixture ID
[**fixtures_all**](#fixtures_all) | **get** /{version}/{sport}/fixtures | All
[**fixtures_by_date**](#fixtures_by_date) | **get** /{version}/{sport}/fixtures/date/{date} | By Date
[**fixtures_by_date_range**](#fixtures_by_date_range) | **get** /{version}/{sport}/fixtures/between/{startDate}/{endDate} | By Date Range
[**fixtures_by_ids**](#fixtures_by_ids) | **get** /{version}/{sport}/fixtures/multi/{fixtureIds} | By IDs
[**fixtures_head_to_head**](#fixtures_head_to_head) | **get** /{version}/{sport}/fixtures/head-to-head/{firstTeam}/{secondTeam} | Head to Head
[**fixtures_latest**](#fixtures_latest) | **get** /{version}/{sport}/fixtures/latest | Last Updated
[**fixtures_search**](#fixtures_search) | **get** /{version}/{sport}/fixtures/search/{name} | Search
[**league_by_id**](#league_by_id) | **get** /{version}/{sport}/leagues/{leagueId} | By ID
[**league_enrichments**](#league_enrichments) | **get** /{version}/{sport}/leagues/{leagueId}/includes | Enrichments
[**league_shirts**](#league_shirts) | **get** /{version}/{sport}/leagues/{leagueId}/jerseys | Shirts By League ID
[**leagues_all**](#leagues_all) | **get** /{version}/{sport}/leagues | All
[**leagues_by_country_id**](#leagues_by_country_id) | **get** /{version}/{sport}/leagues/countries/{countryId} | By Country ID
[**leagues_by_date**](#leagues_by_date) | **get** /{version}/{sport}/leagues/date/{date} | By Date
[**leagues_by_team_id**](#leagues_by_team_id) | **get** /{version}/{sport}/teams/{teamId}/leagues | Leagues By Team ID
[**leagues_current_by_team_id**](#leagues_current_by_team_id) | **get** /{version}/{sport}/teams/{teamId}/leagues/current | Current Leagues By Team ID
[**leagues_live**](#leagues_live) | **get** /{version}/{sport}/leagues/live | Live
[**leagues_search**](#leagues_search) | **get** /{version}/{sport}/leagues/search/{name} | Search
[**livescores_all**](#livescores_all) | **get** /{version}/{sport}/livescores | All
[**livescores_all_in_play**](#livescores_all_in_play) | **get** /{version}/{sport}/livescores/inplay | All In-play
[**livescores_latest**](#livescores_latest) | **get** /{version}/{sport}/livescores/latest | Last Updated In-play
[**news_all_post_match**](#news_all_post_match) | **get** /{version}/{sport}/news/post-match | All Post Match
[**news_all_pre_match**](#news_all_pre_match) | **get** /{version}/{sport}/news/pre-match | All Pre-match
[**news_post_match_by_season_id**](#news_post_match_by_season_id) | **get** /{version}/{sport}/news/post-match/seasons/{seasonId} | Post Match by Season ID
[**news_pre_match_by_season_id**](#news_pre_match_by_season_id) | **get** /{version}/{sport}/news/pre-match/seasons/{seasonId} | Pre-match By Season ID
[**news_upcoming_post_match**](#news_upcoming_post_match) | **get** /{version}/{sport}/news/post-match/upcoming | Upcoming Post Match
[**news_upcoming_pre_match**](#news_upcoming_pre_match) | **get** /{version}/{sport}/news/pre-match/upcoming | Upcoming Pre-match
[**odds_all_in_play**](#odds_all_in_play) | **get** /{version}/{sport}/odds/inplay | All In-play
[**odds_all_pre_match**](#odds_all_pre_match) | **get** /{version}/{sport}/odds/pre-match | All Pre-match
[**odds_in_play_by_fixture_and_bookmaker_id**](#odds_in_play_by_fixture_and_bookmaker_id) | **get** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}/bookmakers/{bookmakerId} | In-play by Fixture and Bookmaker ID
[**odds_in_play_by_fixture_and_market_id**](#odds_in_play_by_fixture_and_market_id) | **get** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}/markets/{marketId} | In-play by Fixture and Market ID
[**odds_in_play_by_fixture_id**](#odds_in_play_by_fixture_id) | **get** /{version}/{sport}/odds/inplay/fixtures/{fixtureId} | In-play by Fixture ID
[**odds_latest_in_play**](#odds_latest_in_play) | **get** /{version}/{sport}/odds/inplay/latest | Latest In-play
[**odds_latest_pre_match**](#odds_latest_pre_match) | **get** /{version}/{sport}/odds/pre-match/latest | Last Updated Pre-match
[**odds_pre_match_by_fixture_and_bookmaker_id**](#odds_pre_match_by_fixture_and_bookmaker_id) | **get** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}/bookmakers/{bookmakerId} | Pre-match by Fixture and Bookmaker ID
[**odds_pre_match_by_fixture_and_market_id**](#odds_pre_match_by_fixture_and_market_id) | **get** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}/markets/{marketId} | Pre-match by Fixture and Market ID
[**odds_pre_match_by_fixture_id**](#odds_pre_match_by_fixture_id) | **get** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId} | Pre-match by Fixture ID
[**player_by_id**](#player_by_id) | **get** /{version}/{sport}/players/{playerId} | By ID
[**players_all**](#players_all) | **get** /{version}/{sport}/players | All
[**players_by_country_id**](#players_by_country_id) | **get** /{version}/{sport}/players/countries/{countryId} | By Country ID
[**players_latest**](#players_latest) | **get** /{version}/{sport}/players/latest | Latest Updated
[**players_search**](#players_search) | **get** /{version}/{sport}/players/search/{name} | Search
[**predictions_all**](#predictions_all) | **get** /{version}/{sport}/predictions/probabilities | All
[**predictions_all_value_bets**](#predictions_all_value_bets) | **get** /{version}/{sport}/predictions/value-bets | All Value Bets
[**predictions_by_fixture_id**](#predictions_by_fixture_id) | **get** /{version}/{sport}/predictions/probabilities/fixtures/{fixtureId} | By Fixture ID
[**predictions_value_bets_by_fixture_id**](#predictions_value_bets_by_fixture_id) | **get** /{version}/{sport}/predictions/value-bets/fixtures/{fixtureId} | Value Bets by Fixture ID
[**referee_by_id**](#referee_by_id) | **get** /{version}/{sport}/referees/{refereeId} | By ID
[**referees_all**](#referees_all) | **get** /{version}/{sport}/referees | All
[**referees_by_country_id**](#referees_by_country_id) | **get** /{version}/{sport}/referees/countries/{countryId} | By Country ID
[**referees_by_season_id**](#referees_by_season_id) | **get** /{version}/{sport}/referees/seasons/{seasonId} | By Season ID
[**referees_search**](#referees_search) | **get** /{version}/{sport}/referees/search/{name} | Search
[**rivals_all**](#rivals_all) | **get** /{version}/{sport}/rivals | All
[**rivals_by_team_id**](#rivals_by_team_id) | **get** /{version}/{sport}/rivals/teams/{teamId} | By Team ID
[**round_by_id**](#round_by_id) | **get** /{version}/{sport}/rounds/{roundId} | By ID
[**rounds_all**](#rounds_all) | **get** /{version}/{sport}/rounds | All
[**rounds_by_season_id**](#rounds_by_season_id) | **get** /{version}/{sport}/rounds/seasons/{seasonId} | Season ID
[**rounds_search**](#rounds_search) | **get** /{version}/{sport}/rounds/search/{name} | Search
[**schedules_by_season_id**](#schedules_by_season_id) | **get** /{version}/{sport}/schedules/seasons/{seasonId} | By Season ID
[**schedules_by_team_and_season_id**](#schedules_by_team_and_season_id) | **get** /{version}/{sport}/schedules/seasons/{seasonId}/teams/{teamId} | By Team and Season ID
[**schedules_by_team_id**](#schedules_by_team_id) | **get** /{version}/{sport}/schedules/teams/{teamId} | By Team ID
[**season_by_id**](#season_by_id) | **get** /{version}/{sport}/seasons/{seasonId} | By ID
[**seasons_all**](#seasons_all) | **get** /{version}/{sport}/seasons | All
[**seasons_by_team_id**](#seasons_by_team_id) | **get** /{version}/{sport}/seasons/teams/{teamId} | By Team ID
[**seasons_search**](#seasons_search) | **get** /{version}/{sport}/seasons/search/{name} | Search
[**squads_by_season_and_team_id**](#squads_by_season_and_team_id) | **get** /{version}/{sport}/squads/seasons/{seasonId}/teams/{teamId} | By Season and Team ID
[**squads_by_team_id**](#squads_by_team_id) | **get** /{version}/{sport}/squads/teams/{teamId} | By Team ID
[**stage_by_id**](#stage_by_id) | **get** /{version}/{sport}/stages/{stageId} | By ID
[**stages_all**](#stages_all) | **get** /{version}/{sport}/stages | All
[**stages_by_season_id**](#stages_by_season_id) | **get** /{version}/{sport}/stages/seasons/{seasonId} | By Season ID
[**stages_search**](#stages_search) | **get** /{version}/{sport}/stages/search/{name} | Search
[**standing_corrections_by_season_id**](#standing_corrections_by_season_id) | **get** /{version}/{sport}/standings/corrections/seasons/{seasonId} | Correction by Season ID
[**standings_all**](#standings_all) | **get** /{version}/{sport}/standings | All
[**standings_by_round_id**](#standings_by_round_id) | **get** /{version}/{sport}/standings/rounds/{roundId} | By Round ID
[**standings_by_season_id**](#standings_by_season_id) | **get** /{version}/{sport}/standings/seasons/{seasonId} | By Season ID
[**standings_live_by_league_id**](#standings_live_by_league_id) | **get** /{version}/{sport}/standings/live/leagues/{leagueId} | By League ID
[**state_by_id**](#state_by_id) | **get** /{version}/{sport}/states/{stateId} | By ID
[**states_by_sport**](#states_by_sport) | **get** /{version}/{sport}/states | By Sport
[**teams_all**](#teams_all) | **get** /{version}/{sport}/teams | All
[**teams_by_country_id**](#teams_by_country_id) | **get** /{version}/{sport}/teams/countries/{countryId} | By Country ID
[**teams_by_id**](#teams_by_id) | **get** /{version}/{sport}/teams/{teamId} | By ID
[**teams_by_season_id**](#teams_by_season_id) | **get** /{version}/{sport}/teams/seasons/{seasonId} | By Season ID
[**teams_search**](#teams_search) | **get** /{version}/{sport}/teams/search/{name} | Search
[**top_scorers_by_season_id**](#top_scorers_by_season_id) | **get** /{version}/{sport}/topscorers/seasons/{seasonId} | By Season ID
[**top_scorers_by_stage_id**](#top_scorers_by_stage_id) | **get** /{version}/{sport}/topscorers/stages/{stageId} | By Stage ID
[**tranfers_by_date_range**](#tranfers_by_date_range) | **get** /{version}/{sport}/transfers/between/{startDate}/{endDate} | By Date Range
[**transfer_by_id**](#transfer_by_id) | **get** /{version}/{sport}/transfers/{transferId} | By ID
[**transfers_all**](#transfers_all) | **get** /{version}/{sport}/transfers | All
[**transfers_by_player_id**](#transfers_by_player_id) | **get** /{version}/{sport}/transfers/players/{playerId} | By Player ID
[**transfers_by_team_id**](#transfers_by_team_id) | **get** /{version}/{sport}/transfers/teams/{teamId} | By Team ID
[**transfers_latest**](#transfers_latest) | **get** /{version}/{sport}/transfers/latest | Last Updated
[**tv_station_by_id**](#tv_station_by_id) | **get** /{version}/{sport}/tv-stations/{tvStationId} | By ID
[**tv_stations_all**](#tv_stations_all) | **get** /{version}/{sport}/tv-stations | All
[**tv_stations_by_fixture_id**](#tv_stations_by_fixture_id) | **get** /{version}/{sport}/tv-stations/fixtures/{fixtureId} | By Fixture ID
[**venue_by_id**](#venue_by_id) | **get** /{version}/{sport}/venues/{venueId} | By ID
[**venues_all**](#venues_all) | **get** /{version}/{sport}/venues | All
[**venues_by_season_id**](#venues_by_season_id) | **get** /{version}/{sport}/venues/seasons/{seasonId} | By Season ID
[**venues_search**](#venues_search) | **get** /{version}/{sport}/venues/search/{name} | Search

# **coach_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By ID
    coach_by_id_response = sportmonks.sport.coach_by_id(
        coach_id=171906,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(coach_by_id_response.body)
    pprint(coach_by_id_response.body["data"])
    pprint(coach_by_id_response.body["subscription"])
    pprint(coach_by_id_response.body["rate_limit"])
    pprint(coach_by_id_response.body["timezone"])
    pprint(coach_by_id_response.headers)
    pprint(coach_by_id_response.status)
    pprint(coach_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.coach_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
coachId | CoachIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CoachIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#coach_by_id.ApiResponseForDefault) | 

#### coach_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportCoachByIdResponse**](../../models/SportCoachByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **coaches_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    coaches_all_response = sportmonks.sport.coaches_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(coaches_all_response.body)
    pprint(coaches_all_response.body["data"])
    pprint(coaches_all_response.body["pagination"])
    pprint(coaches_all_response.body["subscription"])
    pprint(coaches_all_response.body["rate_limit"])
    pprint(coaches_all_response.body["timezone"])
    pprint(coaches_all_response.headers)
    pprint(coaches_all_response.status)
    pprint(coaches_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.coaches_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#coaches_all.ApiResponseForDefault) | 

#### coaches_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportCoachesAllResponse**](../../models/SportCoachesAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **coaches_by_country_id**

By Country ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Country ID
    coaches_by_country_id_response = sportmonks.sport.coaches_by_country_id(
        country_id=320,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(coaches_by_country_id_response.body)
    pprint(coaches_by_country_id_response.body["data"])
    pprint(coaches_by_country_id_response.body["pagination"])
    pprint(coaches_by_country_id_response.body["subscription"])
    pprint(coaches_by_country_id_response.body["rate_limit"])
    pprint(coaches_by_country_id_response.body["timezone"])
    pprint(coaches_by_country_id_response.headers)
    pprint(coaches_by_country_id_response.status)
    pprint(coaches_by_country_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.coaches_by_country_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
countryId | CountryIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CountryIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#coaches_by_country_id.ApiResponseForDefault) | 

#### coaches_by_country_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportCoachesByCountryIdResponse**](../../models/SportCoachesByCountryIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **coaches_latest**

Last updated

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Last updated
    coaches_latest_response = sportmonks.sport.coaches_latest(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(coaches_latest_response.body)
    pprint(coaches_latest_response.body["data"])
    pprint(coaches_latest_response.body["message"])
    pprint(coaches_latest_response.body["subscription"])
    pprint(coaches_latest_response.body["rate_limit"])
    pprint(coaches_latest_response.body["timezone"])
    pprint(coaches_latest_response.headers)
    pprint(coaches_latest_response.status)
    pprint(coaches_latest_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.coaches_latest: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#coaches_latest.ApiResponseForDefault) | 

#### coaches_latest.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportCoachesLatestResponse**](../../models/SportCoachesLatestResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **coaches_search**

Search

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Search
    coaches_search_response = sportmonks.sport.coaches_search(
        name="John",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(coaches_search_response.body)
    pprint(coaches_search_response.body["data"])
    pprint(coaches_search_response.body["pagination"])
    pprint(coaches_search_response.body["subscription"])
    pprint(coaches_search_response.body["rate_limit"])
    pprint(coaches_search_response.body["timezone"])
    pprint(coaches_search_response.headers)
    pprint(coaches_search_response.status)
    pprint(coaches_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.coaches_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
name | NameSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#coaches_search.ApiResponseForDefault) | 

#### coaches_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportCoachesSearchResponse**](../../models/SportCoachesSearchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **commentaries_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    commentaries_all_response = sportmonks.sport.commentaries_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(commentaries_all_response.body)
    pprint(commentaries_all_response.body["data"])
    pprint(commentaries_all_response.body["pagination"])
    pprint(commentaries_all_response.body["subscription"])
    pprint(commentaries_all_response.body["rate_limit"])
    pprint(commentaries_all_response.body["timezone"])
    pprint(commentaries_all_response.headers)
    pprint(commentaries_all_response.status)
    pprint(commentaries_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.commentaries_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#commentaries_all.ApiResponseForDefault) | 

#### commentaries_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportCommentariesAllResponse**](../../models/SportCommentariesAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **commentaries_by_fixture_id**

By Fixture ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Fixture ID
    commentaries_by_fixture_id_response = sportmonks.sport.commentaries_by_fixture_id(
        fixture_id=16808591,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(commentaries_by_fixture_id_response.body)
    pprint(commentaries_by_fixture_id_response.body["data"])
    pprint(commentaries_by_fixture_id_response.body["message"])
    pprint(commentaries_by_fixture_id_response.body["subscription"])
    pprint(commentaries_by_fixture_id_response.body["rate_limit"])
    pprint(commentaries_by_fixture_id_response.body["timezone"])
    pprint(commentaries_by_fixture_id_response.headers)
    pprint(commentaries_by_fixture_id_response.status)
    pprint(commentaries_by_fixture_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.commentaries_by_fixture_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
fixtureId | FixtureIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#commentaries_by_fixture_id.ApiResponseForDefault) | 

#### commentaries_by_fixture_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportCommentariesByFixtureIdResponse**](../../models/SportCommentariesByFixtureIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fixture_by_date_range_for_team**

By Date Range for Team

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Date Range for Team
    fixture_by_date_range_for_team_response = (
        sportmonks.sport.fixture_by_date_range_for_team(
            start_date="maiores",  # required
            end_date="voluptates",  # required
            team_id="ut",  # required
            version="v3",  # optional
            sport="football",  # optional
        )
    )
    pprint(fixture_by_date_range_for_team_response.body)
    pprint(fixture_by_date_range_for_team_response.body["data"])
    pprint(fixture_by_date_range_for_team_response.body["pagination"])
    pprint(fixture_by_date_range_for_team_response.body["subscription"])
    pprint(fixture_by_date_range_for_team_response.body["rate_limit"])
    pprint(fixture_by_date_range_for_team_response.body["timezone"])
    pprint(fixture_by_date_range_for_team_response.headers)
    pprint(fixture_by_date_range_for_team_response.status)
    pprint(fixture_by_date_range_for_team_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.fixture_by_date_range_for_team: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
startDate | StartDateSchema | | 
endDate | EndDateSchema | | 
teamId | TeamIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EndDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fixture_by_date_range_for_team.ApiResponseForDefault) | 

#### fixture_by_date_range_for_team.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportFixtureByDateRangeForTeamResponse**](../../models/SportFixtureByDateRangeForTeamResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fixture_by_id**

Fixture ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Fixture ID
    fixture_by_id_response = sportmonks.sport.fixture_by_id(
        fixture_id=18528480,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(fixture_by_id_response.body)
    pprint(fixture_by_id_response.body["data"])
    pprint(fixture_by_id_response.body["pagination"])
    pprint(fixture_by_id_response.body["subscription"])
    pprint(fixture_by_id_response.body["rate_limit"])
    pprint(fixture_by_id_response.body["timezone"])
    pprint(fixture_by_id_response.headers)
    pprint(fixture_by_id_response.status)
    pprint(fixture_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.fixture_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
fixtureId | FixtureIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fixture_by_id.ApiResponseForDefault) | 

#### fixture_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportFixtureByIdResponse**](../../models/SportFixtureByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fixtures_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    fixtures_all_response = sportmonks.sport.fixtures_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(fixtures_all_response.body)
    pprint(fixtures_all_response.body["data"])
    pprint(fixtures_all_response.body["pagination"])
    pprint(fixtures_all_response.body["subscription"])
    pprint(fixtures_all_response.body["rate_limit"])
    pprint(fixtures_all_response.body["timezone"])
    pprint(fixtures_all_response.headers)
    pprint(fixtures_all_response.status)
    pprint(fixtures_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.fixtures_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fixtures_all.ApiResponseForDefault) | 

#### fixtures_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportFixturesAllResponse**](../../models/SportFixturesAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fixtures_by_date**

By Date

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Date
    fixtures_by_date_response = sportmonks.sport.fixtures_by_date(
        date="2022-07-24",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(fixtures_by_date_response.body)
    pprint(fixtures_by_date_response.body["data"])
    pprint(fixtures_by_date_response.body["pagination"])
    pprint(fixtures_by_date_response.body["subscription"])
    pprint(fixtures_by_date_response.body["rate_limit"])
    pprint(fixtures_by_date_response.body["timezone"])
    pprint(fixtures_by_date_response.headers)
    pprint(fixtures_by_date_response.status)
    pprint(fixtures_by_date_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.fixtures_by_date: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
date | DateSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fixtures_by_date.ApiResponseForDefault) | 

#### fixtures_by_date.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportFixturesByDateResponse**](../../models/SportFixturesByDateResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fixtures_by_date_range**

By Date Range

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Date Range
    fixtures_by_date_range_response = sportmonks.sport.fixtures_by_date_range(
        start_date="2022-07-17",  # required
        end_date="2022-07-25",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(fixtures_by_date_range_response.body)
    pprint(fixtures_by_date_range_response.body["data"])
    pprint(fixtures_by_date_range_response.body["pagination"])
    pprint(fixtures_by_date_range_response.body["subscription"])
    pprint(fixtures_by_date_range_response.body["rate_limit"])
    pprint(fixtures_by_date_range_response.body["timezone"])
    pprint(fixtures_by_date_range_response.headers)
    pprint(fixtures_by_date_range_response.status)
    pprint(fixtures_by_date_range_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.fixtures_by_date_range: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
startDate | StartDateSchema | | 
endDate | EndDateSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EndDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fixtures_by_date_range.ApiResponseForDefault) | 

#### fixtures_by_date_range.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportFixturesByDateRangeResponse**](../../models/SportFixturesByDateRangeResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fixtures_by_ids**

By IDs

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By IDs
    fixtures_by_ids_response = sportmonks.sport.fixtures_by_ids(
        fixture_ids="18528484%2C18531140",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(fixtures_by_ids_response.body)
    pprint(fixtures_by_ids_response.body["data"])
    pprint(fixtures_by_ids_response.body["subscription"])
    pprint(fixtures_by_ids_response.body["rate_limit"])
    pprint(fixtures_by_ids_response.body["timezone"])
    pprint(fixtures_by_ids_response.headers)
    pprint(fixtures_by_ids_response.status)
    pprint(fixtures_by_ids_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.fixtures_by_ids: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
fixtureIds | FixtureIdsSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fixtures_by_ids.ApiResponseForDefault) | 

#### fixtures_by_ids.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportFixturesByIdsResponse**](../../models/SportFixturesByIdsResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fixtures_head_to_head**

Head to Head

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Head to Head
    fixtures_head_to_head_response = sportmonks.sport.fixtures_head_to_head(
        first_team=2650,  # required
        second_team=86,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(fixtures_head_to_head_response.body)
    pprint(fixtures_head_to_head_response.body["data"])
    pprint(fixtures_head_to_head_response.body["subscription"])
    pprint(fixtures_head_to_head_response.body["rate_limit"])
    pprint(fixtures_head_to_head_response.body["timezone"])
    pprint(fixtures_head_to_head_response.headers)
    pprint(fixtures_head_to_head_response.status)
    pprint(fixtures_head_to_head_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.fixtures_head_to_head: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
firstTeam | FirstTeamSchema | | 
secondTeam | SecondTeamSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FirstTeamSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SecondTeamSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fixtures_head_to_head.ApiResponseForDefault) | 

#### fixtures_head_to_head.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportFixturesHeadToHeadResponse**](../../models/SportFixturesHeadToHeadResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fixtures_latest**

Last Updated

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Last Updated
    fixtures_latest_response = sportmonks.sport.fixtures_latest(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(fixtures_latest_response.headers)
    pprint(fixtures_latest_response.status)
    pprint(fixtures_latest_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.fixtures_latest: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fixtures_latest.ApiResponseForDefault) | 

#### fixtures_latest.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fixtures_search**

Search

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Search
    fixtures_search_response = sportmonks.sport.fixtures_search(
        name="havn",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(fixtures_search_response.body)
    pprint(fixtures_search_response.body["data"])
    pprint(fixtures_search_response.body["pagination"])
    pprint(fixtures_search_response.body["subscription"])
    pprint(fixtures_search_response.body["rate_limit"])
    pprint(fixtures_search_response.body["timezone"])
    pprint(fixtures_search_response.headers)
    pprint(fixtures_search_response.status)
    pprint(fixtures_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.fixtures_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
name | NameSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fixtures_search.ApiResponseForDefault) | 

#### fixtures_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportFixturesSearchResponse**](../../models/SportFixturesSearchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **league_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By ID
    league_by_id_response = sportmonks.sport.league_by_id(
        league_id=271,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(league_by_id_response.body)
    pprint(league_by_id_response.body["data"])
    pprint(league_by_id_response.body["subscription"])
    pprint(league_by_id_response.body["rate_limit"])
    pprint(league_by_id_response.body["timezone"])
    pprint(league_by_id_response.headers)
    pprint(league_by_id_response.status)
    pprint(league_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.league_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
leagueId | LeagueIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LeagueIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#league_by_id.ApiResponseForDefault) | 

#### league_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportLeagueByIdResponse**](../../models/SportLeagueByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **league_enrichments**

Enrichments

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Enrichments
    league_enrichments_response = sportmonks.sport.league_enrichments(
        league_id=271,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(league_enrichments_response.headers)
    pprint(league_enrichments_response.status)
    pprint(league_enrichments_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.league_enrichments: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
leagueId | LeagueIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LeagueIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#league_enrichments.ApiResponseForDefault) | 

#### league_enrichments.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **league_shirts**

Shirts By League ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Shirts By League ID
    league_shirts_response = sportmonks.sport.league_shirts(
        league_id=271,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(league_shirts_response.headers)
    pprint(league_shirts_response.status)
    pprint(league_shirts_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.league_shirts: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
leagueId | LeagueIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LeagueIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#league_shirts.ApiResponseForDefault) | 

#### league_shirts.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **leagues_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    leagues_all_response = sportmonks.sport.leagues_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(leagues_all_response.body)
    pprint(leagues_all_response.body["data"])
    pprint(leagues_all_response.body["pagination"])
    pprint(leagues_all_response.body["subscription"])
    pprint(leagues_all_response.body["rate_limit"])
    pprint(leagues_all_response.body["timezone"])
    pprint(leagues_all_response.headers)
    pprint(leagues_all_response.status)
    pprint(leagues_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.leagues_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#leagues_all.ApiResponseForDefault) | 

#### leagues_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportLeaguesAllResponse**](../../models/SportLeaguesAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **leagues_by_country_id**

By Country ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Country ID
    leagues_by_country_id_response = sportmonks.sport.leagues_by_country_id(
        country_id=320,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(leagues_by_country_id_response.body)
    pprint(leagues_by_country_id_response.body["data"])
    pprint(leagues_by_country_id_response.body["pagination"])
    pprint(leagues_by_country_id_response.body["subscription"])
    pprint(leagues_by_country_id_response.body["rate_limit"])
    pprint(leagues_by_country_id_response.body["timezone"])
    pprint(leagues_by_country_id_response.headers)
    pprint(leagues_by_country_id_response.status)
    pprint(leagues_by_country_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.leagues_by_country_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
countryId | CountryIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CountryIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#leagues_by_country_id.ApiResponseForDefault) | 

#### leagues_by_country_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportLeaguesByCountryIdResponse**](../../models/SportLeaguesByCountryIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **leagues_by_date**

By Date

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Date
    leagues_by_date_response = sportmonks.sport.leagues_by_date(
        date="2022-07-15",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(leagues_by_date_response.body)
    pprint(leagues_by_date_response.body["data"])
    pprint(leagues_by_date_response.body["pagination"])
    pprint(leagues_by_date_response.body["subscription"])
    pprint(leagues_by_date_response.body["rate_limit"])
    pprint(leagues_by_date_response.body["timezone"])
    pprint(leagues_by_date_response.headers)
    pprint(leagues_by_date_response.status)
    pprint(leagues_by_date_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.leagues_by_date: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
date | DateSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#leagues_by_date.ApiResponseForDefault) | 

#### leagues_by_date.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportLeaguesByDateResponse**](../../models/SportLeaguesByDateResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **leagues_by_team_id**

Leagues By Team ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Leagues By Team ID
    leagues_by_team_id_response = sportmonks.sport.leagues_by_team_id(
        team_id=180,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(leagues_by_team_id_response.headers)
    pprint(leagues_by_team_id_response.status)
    pprint(leagues_by_team_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.leagues_by_team_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
teamId | TeamIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#leagues_by_team_id.ApiResponseForDefault) | 

#### leagues_by_team_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **leagues_current_by_team_id**

Current Leagues By Team ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Current Leagues By Team ID
    leagues_current_by_team_id_response = sportmonks.sport.leagues_current_by_team_id(
        team_id=180,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(leagues_current_by_team_id_response.headers)
    pprint(leagues_current_by_team_id_response.status)
    pprint(leagues_current_by_team_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.leagues_current_by_team_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
teamId | TeamIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#leagues_current_by_team_id.ApiResponseForDefault) | 

#### leagues_current_by_team_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **leagues_live**

Live

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Live
    leagues_live_response = sportmonks.sport.leagues_live(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(leagues_live_response.body)
    pprint(leagues_live_response.body["data"])
    pprint(leagues_live_response.body["subscription"])
    pprint(leagues_live_response.body["rate_limit"])
    pprint(leagues_live_response.body["timezone"])
    pprint(leagues_live_response.headers)
    pprint(leagues_live_response.status)
    pprint(leagues_live_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.leagues_live: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#leagues_live.ApiResponseForDefault) | 

#### leagues_live.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportLeaguesLiveResponse**](../../models/SportLeaguesLiveResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **leagues_search**

Search

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Search
    leagues_search_response = sportmonks.sport.leagues_search(
        name="Super",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(leagues_search_response.body)
    pprint(leagues_search_response.body["data"])
    pprint(leagues_search_response.body["pagination"])
    pprint(leagues_search_response.body["subscription"])
    pprint(leagues_search_response.body["rate_limit"])
    pprint(leagues_search_response.body["timezone"])
    pprint(leagues_search_response.headers)
    pprint(leagues_search_response.status)
    pprint(leagues_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.leagues_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
name | NameSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#leagues_search.ApiResponseForDefault) | 

#### leagues_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportLeaguesSearchResponse**](../../models/SportLeaguesSearchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **livescores_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    livescores_all_response = sportmonks.sport.livescores_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(livescores_all_response.body)
    pprint(livescores_all_response.body["data"])
    pprint(livescores_all_response.body["subscription"])
    pprint(livescores_all_response.body["rate_limit"])
    pprint(livescores_all_response.body["timezone"])
    pprint(livescores_all_response.headers)
    pprint(livescores_all_response.status)
    pprint(livescores_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.livescores_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#livescores_all.ApiResponseForDefault) | 

#### livescores_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportLivescoresAllResponse**](../../models/SportLivescoresAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **livescores_all_in_play**

All In-play

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All In-play
    livescores_all_in_play_response = sportmonks.sport.livescores_all_in_play(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(livescores_all_in_play_response.body)
    pprint(livescores_all_in_play_response.body["data"])
    pprint(livescores_all_in_play_response.body["subscription"])
    pprint(livescores_all_in_play_response.body["rate_limit"])
    pprint(livescores_all_in_play_response.body["timezone"])
    pprint(livescores_all_in_play_response.headers)
    pprint(livescores_all_in_play_response.status)
    pprint(livescores_all_in_play_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.livescores_all_in_play: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#livescores_all_in_play.ApiResponseForDefault) | 

#### livescores_all_in_play.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportLivescoresAllInPlayResponse**](../../models/SportLivescoresAllInPlayResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **livescores_latest**

Last Updated In-play

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Last Updated In-play
    livescores_latest_response = sportmonks.sport.livescores_latest(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(livescores_latest_response.body)
    pprint(livescores_latest_response.body["data"])
    pprint(livescores_latest_response.body["subscription"])
    pprint(livescores_latest_response.body["rate_limit"])
    pprint(livescores_latest_response.body["timezone"])
    pprint(livescores_latest_response.headers)
    pprint(livescores_latest_response.status)
    pprint(livescores_latest_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.livescores_latest: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#livescores_latest.ApiResponseForDefault) | 

#### livescores_latest.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportLivescoresLatestResponse**](../../models/SportLivescoresLatestResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **news_all_post_match**

All Post Match

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All Post Match
    news_all_post_match_response = sportmonks.sport.news_all_post_match(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(news_all_post_match_response.headers)
    pprint(news_all_post_match_response.status)
    pprint(news_all_post_match_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.news_all_post_match: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#news_all_post_match.ApiResponseForDefault) | 

#### news_all_post_match.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **news_all_pre_match**

All Pre-match

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All Pre-match
    news_all_pre_match_response = sportmonks.sport.news_all_pre_match(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(news_all_pre_match_response.body)
    pprint(news_all_pre_match_response.body["data"])
    pprint(news_all_pre_match_response.body["pagination"])
    pprint(news_all_pre_match_response.body["subscription"])
    pprint(news_all_pre_match_response.body["rate_limit"])
    pprint(news_all_pre_match_response.body["timezone"])
    pprint(news_all_pre_match_response.headers)
    pprint(news_all_pre_match_response.status)
    pprint(news_all_pre_match_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.news_all_pre_match: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#news_all_pre_match.ApiResponseFor200) | OK

#### news_all_pre_match.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportNewsAllPreMatchResponse**](../../models/SportNewsAllPreMatchResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Date | DateSchema | | optional
Server | ServerSchema | | optional
Cache-Control | CacheControlSchema | | optional
X-RateLimit-Limit | XRateLimitLimitSchema | | optional
X-RateLimit-Remaining | XRateLimitRemainingSchema | | optional
Vary | VarySchema | | optional
Content-Encoding | ContentEncodingSchema | | optional
X-Robots-Tag | XRobotsTagSchema | | optional
Content-Length | ContentLengthSchema | | optional

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRateLimitLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XRateLimitRemainingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRobotsTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **news_post_match_by_season_id**

Post Match by Season ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Post Match by Season ID
    news_post_match_by_season_id_response = (
        sportmonks.sport.news_post_match_by_season_id(
            season_id=19686,  # required
            version="v3",  # optional
            sport="football",  # optional
        )
    )
    pprint(news_post_match_by_season_id_response.headers)
    pprint(news_post_match_by_season_id_response.status)
    pprint(news_post_match_by_season_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.news_post_match_by_season_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#news_post_match_by_season_id.ApiResponseForDefault) | 

#### news_post_match_by_season_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **news_pre_match_by_season_id**

Pre-match By Season ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Pre-match By Season ID
    news_pre_match_by_season_id_response = sportmonks.sport.news_pre_match_by_season_id(
        season_id=19734,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(news_pre_match_by_season_id_response.body)
    pprint(news_pre_match_by_season_id_response.body["data"])
    pprint(news_pre_match_by_season_id_response.body["pagination"])
    pprint(news_pre_match_by_season_id_response.body["subscription"])
    pprint(news_pre_match_by_season_id_response.body["rate_limit"])
    pprint(news_pre_match_by_season_id_response.body["timezone"])
    pprint(news_pre_match_by_season_id_response.headers)
    pprint(news_pre_match_by_season_id_response.status)
    pprint(news_pre_match_by_season_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.news_pre_match_by_season_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#news_pre_match_by_season_id.ApiResponseFor200) | OK

#### news_pre_match_by_season_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportNewsPreMatchBySeasonIdResponse**](../../models/SportNewsPreMatchBySeasonIdResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Date | DateSchema | | optional
Server | ServerSchema | | optional
Cache-Control | CacheControlSchema | | optional
X-RateLimit-Limit | XRateLimitLimitSchema | | optional
X-RateLimit-Remaining | XRateLimitRemainingSchema | | optional
Vary | VarySchema | | optional
Content-Encoding | ContentEncodingSchema | | optional
X-Robots-Tag | XRobotsTagSchema | | optional
Content-Length | ContentLengthSchema | | optional

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRateLimitLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XRateLimitRemainingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRobotsTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **news_upcoming_post_match**

Upcoming Post Match

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Upcoming Post Match
    news_upcoming_post_match_response = sportmonks.sport.news_upcoming_post_match(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(news_upcoming_post_match_response.headers)
    pprint(news_upcoming_post_match_response.status)
    pprint(news_upcoming_post_match_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.news_upcoming_post_match: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('text/plain', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#news_upcoming_post_match.ApiResponseForDefault) | 

#### news_upcoming_post_match.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyTextPlain, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyTextPlain

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **news_upcoming_pre_match**

Upcoming Pre-match

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Upcoming Pre-match
    news_upcoming_pre_match_response = sportmonks.sport.news_upcoming_pre_match(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(news_upcoming_pre_match_response.body)
    pprint(news_upcoming_pre_match_response.body["data"])
    pprint(news_upcoming_pre_match_response.body["pagination"])
    pprint(news_upcoming_pre_match_response.body["subscription"])
    pprint(news_upcoming_pre_match_response.body["rate_limit"])
    pprint(news_upcoming_pre_match_response.body["timezone"])
    pprint(news_upcoming_pre_match_response.headers)
    pprint(news_upcoming_pre_match_response.status)
    pprint(news_upcoming_pre_match_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.news_upcoming_pre_match: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#news_upcoming_pre_match.ApiResponseFor200) | OK

#### news_upcoming_pre_match.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportNewsUpcomingPreMatchResponse**](../../models/SportNewsUpcomingPreMatchResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Date | DateSchema | | optional
Server | ServerSchema | | optional
Cache-Control | CacheControlSchema | | optional
X-RateLimit-Limit | XRateLimitLimitSchema | | optional
X-RateLimit-Remaining | XRateLimitRemainingSchema | | optional
Vary | VarySchema | | optional
Content-Encoding | ContentEncodingSchema | | optional
X-Robots-Tag | XRobotsTagSchema | | optional
Content-Length | ContentLengthSchema | | optional

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRateLimitLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XRateLimitRemainingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRobotsTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **odds_all_in_play**

All In-play

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All In-play
    odds_all_in_play_response = sportmonks.sport.odds_all_in_play(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(odds_all_in_play_response.body)
    pprint(odds_all_in_play_response.body["data"])
    pprint(odds_all_in_play_response.body["pagination"])
    pprint(odds_all_in_play_response.body["subscription"])
    pprint(odds_all_in_play_response.body["rate_limit"])
    pprint(odds_all_in_play_response.body["timezone"])
    pprint(odds_all_in_play_response.headers)
    pprint(odds_all_in_play_response.status)
    pprint(odds_all_in_play_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.odds_all_in_play: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#odds_all_in_play.ApiResponseFor200) | OK

#### odds_all_in_play.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportOddsAllInPlayResponse**](../../models/SportOddsAllInPlayResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Date | DateSchema | | optional
Server | ServerSchema | | optional
Cache-Control | CacheControlSchema | | optional
X-RateLimit-Limit | XRateLimitLimitSchema | | optional
X-RateLimit-Remaining | XRateLimitRemainingSchema | | optional
Vary | VarySchema | | optional
Content-Encoding | ContentEncodingSchema | | optional
X-Robots-Tag | XRobotsTagSchema | | optional
Content-Length | ContentLengthSchema | | optional

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRateLimitLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XRateLimitRemainingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRobotsTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **odds_all_pre_match**

All Pre-match

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All Pre-match
    odds_all_pre_match_response = sportmonks.sport.odds_all_pre_match(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(odds_all_pre_match_response.body)
    pprint(odds_all_pre_match_response.body["data"])
    pprint(odds_all_pre_match_response.body["pagination"])
    pprint(odds_all_pre_match_response.body["subscription"])
    pprint(odds_all_pre_match_response.body["rate_limit"])
    pprint(odds_all_pre_match_response.body["timezone"])
    pprint(odds_all_pre_match_response.headers)
    pprint(odds_all_pre_match_response.status)
    pprint(odds_all_pre_match_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.odds_all_pre_match: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#odds_all_pre_match.ApiResponseForDefault) | 

#### odds_all_pre_match.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportOddsAllPreMatchResponse**](../../models/SportOddsAllPreMatchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **odds_in_play_by_fixture_and_bookmaker_id**

In-play by Fixture and Bookmaker ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # In-play by Fixture and Bookmaker ID
    odds_in_play_by_fixture_and_bookmaker_id_response = (
        sportmonks.sport.odds_in_play_by_fixture_and_bookmaker_id(
            fixture_id=18535046,  # required
            bookmaker_id=6,  # required
            version="v3",  # optional
            sport="football",  # optional
        )
    )
    pprint(odds_in_play_by_fixture_and_bookmaker_id_response.headers)
    pprint(odds_in_play_by_fixture_and_bookmaker_id_response.status)
    pprint(odds_in_play_by_fixture_and_bookmaker_id_response.round_trip_time)
except ApiException as e:
    print(
        "Exception when calling SportApi.odds_in_play_by_fixture_and_bookmaker_id: %s\n"
        % e
    )
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
fixtureId | FixtureIdSchema | | 
bookmakerId | BookmakerIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BookmakerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#odds_in_play_by_fixture_and_bookmaker_id.ApiResponseFor200) | Successful response

#### odds_in_play_by_fixture_and_bookmaker_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **odds_in_play_by_fixture_and_market_id**

In-play by Fixture and Market ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # In-play by Fixture and Market ID
    odds_in_play_by_fixture_and_market_id_response = (
        sportmonks.sport.odds_in_play_by_fixture_and_market_id(
            fixture_id=233366,  # required
            market_id=56,  # required
            version="v3",  # optional
            sport="football",  # optional
        )
    )
    pprint(odds_in_play_by_fixture_and_market_id_response.headers)
    pprint(odds_in_play_by_fixture_and_market_id_response.status)
    pprint(odds_in_play_by_fixture_and_market_id_response.round_trip_time)
except ApiException as e:
    print(
        "Exception when calling SportApi.odds_in_play_by_fixture_and_market_id: %s\n"
        % e
    )
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
fixtureId | FixtureIdSchema | | 
marketId | MarketIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# MarketIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#odds_in_play_by_fixture_and_market_id.ApiResponseFor200) | Successful response

#### odds_in_play_by_fixture_and_market_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **odds_in_play_by_fixture_id**

In-play by Fixture ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # In-play by Fixture ID
    odds_in_play_by_fixture_id_response = sportmonks.sport.odds_in_play_by_fixture_id(
        fixture_id=18535046,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(odds_in_play_by_fixture_id_response.body)
    pprint(odds_in_play_by_fixture_id_response.body["data"])
    pprint(odds_in_play_by_fixture_id_response.body["subscription"])
    pprint(odds_in_play_by_fixture_id_response.body["rate_limit"])
    pprint(odds_in_play_by_fixture_id_response.body["timezone"])
    pprint(odds_in_play_by_fixture_id_response.headers)
    pprint(odds_in_play_by_fixture_id_response.status)
    pprint(odds_in_play_by_fixture_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.odds_in_play_by_fixture_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
fixtureId | FixtureIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#odds_in_play_by_fixture_id.ApiResponseFor200) | OK

#### odds_in_play_by_fixture_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportOddsInPlayByFixtureIdResponse**](../../models/SportOddsInPlayByFixtureIdResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Date | DateSchema | | optional
Server | ServerSchema | | optional
Cache-Control | CacheControlSchema | | optional
X-RateLimit-Limit | XRateLimitLimitSchema | | optional
X-RateLimit-Remaining | XRateLimitRemainingSchema | | optional
Vary | VarySchema | | optional
Content-Encoding | ContentEncodingSchema | | optional
X-Robots-Tag | XRobotsTagSchema | | optional
Content-Length | ContentLengthSchema | | optional

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRateLimitLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XRateLimitRemainingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRobotsTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **odds_latest_in_play**

Latest In-play

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Latest In-play
    odds_latest_in_play_response = sportmonks.sport.odds_latest_in_play(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(odds_latest_in_play_response.headers)
    pprint(odds_latest_in_play_response.status)
    pprint(odds_latest_in_play_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.odds_latest_in_play: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#odds_latest_in_play.ApiResponseFor200) | Successful response

#### odds_latest_in_play.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **odds_latest_pre_match**

Last Updated Pre-match

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Last Updated Pre-match
    odds_latest_pre_match_response = sportmonks.sport.odds_latest_pre_match(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(odds_latest_pre_match_response.headers)
    pprint(odds_latest_pre_match_response.status)
    pprint(odds_latest_pre_match_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.odds_latest_pre_match: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#odds_latest_pre_match.ApiResponseFor200) | Successful response

#### odds_latest_pre_match.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **odds_pre_match_by_fixture_and_bookmaker_id**

Pre-match by Fixture and Bookmaker ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Pre-match by Fixture and Bookmaker ID
    odds_pre_match_by_fixture_and_bookmaker_id_response = (
        sportmonks.sport.odds_pre_match_by_fixture_and_bookmaker_id(
            fixture_id=233366,  # required
            bookmaker_id=6,  # required
            version="v3",  # optional
            sport="football",  # optional
        )
    )
    pprint(odds_pre_match_by_fixture_and_bookmaker_id_response.body)
    pprint(odds_pre_match_by_fixture_and_bookmaker_id_response.body["data"])
    pprint(odds_pre_match_by_fixture_and_bookmaker_id_response.body["subscription"])
    pprint(odds_pre_match_by_fixture_and_bookmaker_id_response.body["rate_limit"])
    pprint(odds_pre_match_by_fixture_and_bookmaker_id_response.body["timezone"])
    pprint(odds_pre_match_by_fixture_and_bookmaker_id_response.headers)
    pprint(odds_pre_match_by_fixture_and_bookmaker_id_response.status)
    pprint(odds_pre_match_by_fixture_and_bookmaker_id_response.round_trip_time)
except ApiException as e:
    print(
        "Exception when calling SportApi.odds_pre_match_by_fixture_and_bookmaker_id: %s\n"
        % e
    )
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
fixtureId | FixtureIdSchema | | 
bookmakerId | BookmakerIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BookmakerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#odds_pre_match_by_fixture_and_bookmaker_id.ApiResponseForDefault) | 

#### odds_pre_match_by_fixture_and_bookmaker_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportOddsPreMatchByFixtureAndBookmakerIdResponse**](../../models/SportOddsPreMatchByFixtureAndBookmakerIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **odds_pre_match_by_fixture_and_market_id**

Pre-match by Fixture and Market ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Pre-match by Fixture and Market ID
    odds_pre_match_by_fixture_and_market_id_response = (
        sportmonks.sport.odds_pre_match_by_fixture_and_market_id(
            fixture_id=233366,  # required
            market_id=56,  # required
            version="v3",  # optional
            sport="football",  # optional
        )
    )
    pprint(odds_pre_match_by_fixture_and_market_id_response.body)
    pprint(odds_pre_match_by_fixture_and_market_id_response.body["data"])
    pprint(odds_pre_match_by_fixture_and_market_id_response.body["subscription"])
    pprint(odds_pre_match_by_fixture_and_market_id_response.body["rate_limit"])
    pprint(odds_pre_match_by_fixture_and_market_id_response.body["timezone"])
    pprint(odds_pre_match_by_fixture_and_market_id_response.headers)
    pprint(odds_pre_match_by_fixture_and_market_id_response.status)
    pprint(odds_pre_match_by_fixture_and_market_id_response.round_trip_time)
except ApiException as e:
    print(
        "Exception when calling SportApi.odds_pre_match_by_fixture_and_market_id: %s\n"
        % e
    )
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
fixtureId | FixtureIdSchema | | 
marketId | MarketIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# MarketIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#odds_pre_match_by_fixture_and_market_id.ApiResponseForDefault) | 

#### odds_pre_match_by_fixture_and_market_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportOddsPreMatchByFixtureAndMarketIdResponse**](../../models/SportOddsPreMatchByFixtureAndMarketIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **odds_pre_match_by_fixture_id**

Pre-match by Fixture ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Pre-match by Fixture ID
    odds_pre_match_by_fixture_id_response = (
        sportmonks.sport.odds_pre_match_by_fixture_id(
            fixture_id=233366,  # required
            version="v3",  # optional
            sport="football",  # optional
        )
    )
    pprint(odds_pre_match_by_fixture_id_response.body)
    pprint(odds_pre_match_by_fixture_id_response.body["data"])
    pprint(odds_pre_match_by_fixture_id_response.body["subscription"])
    pprint(odds_pre_match_by_fixture_id_response.body["rate_limit"])
    pprint(odds_pre_match_by_fixture_id_response.body["timezone"])
    pprint(odds_pre_match_by_fixture_id_response.headers)
    pprint(odds_pre_match_by_fixture_id_response.status)
    pprint(odds_pre_match_by_fixture_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.odds_pre_match_by_fixture_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
fixtureId | FixtureIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#odds_pre_match_by_fixture_id.ApiResponseForDefault) | 

#### odds_pre_match_by_fixture_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportOddsPreMatchByFixtureIdResponse**](../../models/SportOddsPreMatchByFixtureIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **player_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By ID
    player_by_id_response = sportmonks.sport.player_by_id(
        player_id=14,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(player_by_id_response.body)
    pprint(player_by_id_response.body["data"])
    pprint(player_by_id_response.body["subscription"])
    pprint(player_by_id_response.body["rate_limit"])
    pprint(player_by_id_response.body["timezone"])
    pprint(player_by_id_response.headers)
    pprint(player_by_id_response.status)
    pprint(player_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.player_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
playerId | PlayerIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PlayerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#player_by_id.ApiResponseForDefault) | 

#### player_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportPlayerByIdResponse**](../../models/SportPlayerByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    players_all_response = sportmonks.sport.players_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(players_all_response.body)
    pprint(players_all_response.body["data"])
    pprint(players_all_response.body["pagination"])
    pprint(players_all_response.body["subscription"])
    pprint(players_all_response.body["rate_limit"])
    pprint(players_all_response.body["timezone"])
    pprint(players_all_response.headers)
    pprint(players_all_response.status)
    pprint(players_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.players_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#players_all.ApiResponseForDefault) | 

#### players_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportPlayersAllResponse**](../../models/SportPlayersAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_by_country_id**

By Country ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Country ID
    players_by_country_id_response = sportmonks.sport.players_by_country_id(
        country_id=320,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(players_by_country_id_response.body)
    pprint(players_by_country_id_response.body["data"])
    pprint(players_by_country_id_response.body["pagination"])
    pprint(players_by_country_id_response.body["subscription"])
    pprint(players_by_country_id_response.body["rate_limit"])
    pprint(players_by_country_id_response.body["timezone"])
    pprint(players_by_country_id_response.headers)
    pprint(players_by_country_id_response.status)
    pprint(players_by_country_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.players_by_country_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
countryId | CountryIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CountryIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#players_by_country_id.ApiResponseForDefault) | 

#### players_by_country_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportPlayersByCountryIdResponse**](../../models/SportPlayersByCountryIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_latest**

Latest Updated

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Latest Updated
    players_latest_response = sportmonks.sport.players_latest(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(players_latest_response.body)
    pprint(players_latest_response.body["data"])
    pprint(players_latest_response.body["subscription"])
    pprint(players_latest_response.body["rate_limit"])
    pprint(players_latest_response.body["timezone"])
    pprint(players_latest_response.headers)
    pprint(players_latest_response.status)
    pprint(players_latest_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.players_latest: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#players_latest.ApiResponseForDefault) | 

#### players_latest.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportPlayersLatestResponse**](../../models/SportPlayersLatestResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **players_search**

Search

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Search
    players_search_response = sportmonks.sport.players_search(
        name="Agg",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(players_search_response.body)
    pprint(players_search_response.body["data"])
    pprint(players_search_response.body["pagination"])
    pprint(players_search_response.body["subscription"])
    pprint(players_search_response.body["rate_limit"])
    pprint(players_search_response.body["timezone"])
    pprint(players_search_response.headers)
    pprint(players_search_response.status)
    pprint(players_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.players_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
name | NameSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#players_search.ApiResponseForDefault) | 

#### players_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportPlayersSearchResponse**](../../models/SportPlayersSearchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **predictions_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    predictions_all_response = sportmonks.sport.predictions_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(predictions_all_response.body)
    pprint(predictions_all_response.body["data"])
    pprint(predictions_all_response.body["pagination"])
    pprint(predictions_all_response.body["subscription"])
    pprint(predictions_all_response.body["rate_limit"])
    pprint(predictions_all_response.body["timezone"])
    pprint(predictions_all_response.headers)
    pprint(predictions_all_response.status)
    pprint(predictions_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.predictions_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#predictions_all.ApiResponseFor200) | OK

#### predictions_all.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportPredictionsAllResponse**](../../models/SportPredictionsAllResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Date | DateSchema | | optional
Server | ServerSchema | | optional
Cache-Control | CacheControlSchema | | optional
X-RateLimit-Limit | XRateLimitLimitSchema | | optional
X-RateLimit-Remaining | XRateLimitRemainingSchema | | optional
Vary | VarySchema | | optional
Content-Encoding | ContentEncodingSchema | | optional
X-Robots-Tag | XRobotsTagSchema | | optional
Content-Length | ContentLengthSchema | | optional

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRateLimitLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XRateLimitRemainingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRobotsTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **predictions_all_value_bets**

All Value Bets

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All Value Bets
    predictions_all_value_bets_response = sportmonks.sport.predictions_all_value_bets(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(predictions_all_value_bets_response.body)
    pprint(predictions_all_value_bets_response.body["data"])
    pprint(predictions_all_value_bets_response.body["pagination"])
    pprint(predictions_all_value_bets_response.body["subscription"])
    pprint(predictions_all_value_bets_response.body["rate_limit"])
    pprint(predictions_all_value_bets_response.body["timezone"])
    pprint(predictions_all_value_bets_response.headers)
    pprint(predictions_all_value_bets_response.status)
    pprint(predictions_all_value_bets_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.predictions_all_value_bets: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#predictions_all_value_bets.ApiResponseFor200) | OK

#### predictions_all_value_bets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportPredictionsAllValueBetsResponse**](../../models/SportPredictionsAllValueBetsResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Date | DateSchema | | optional
Server | ServerSchema | | optional
Cache-Control | CacheControlSchema | | optional
X-RateLimit-Limit | XRateLimitLimitSchema | | optional
X-RateLimit-Remaining | XRateLimitRemainingSchema | | optional
Vary | VarySchema | | optional
Content-Encoding | ContentEncodingSchema | | optional
X-Robots-Tag | XRobotsTagSchema | | optional
Content-Length | ContentLengthSchema | | optional

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRateLimitLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XRateLimitRemainingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRobotsTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **predictions_by_fixture_id**

By Fixture ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Fixture ID
    predictions_by_fixture_id_response = sportmonks.sport.predictions_by_fixture_id(
        fixture_id=16774022,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(predictions_by_fixture_id_response.body)
    pprint(predictions_by_fixture_id_response.body["data"])
    pprint(predictions_by_fixture_id_response.body["pagination"])
    pprint(predictions_by_fixture_id_response.body["subscription"])
    pprint(predictions_by_fixture_id_response.body["rate_limit"])
    pprint(predictions_by_fixture_id_response.body["timezone"])
    pprint(predictions_by_fixture_id_response.headers)
    pprint(predictions_by_fixture_id_response.status)
    pprint(predictions_by_fixture_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.predictions_by_fixture_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
fixtureId | FixtureIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#predictions_by_fixture_id.ApiResponseFor200) | OK

#### predictions_by_fixture_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportPredictionsByFixtureIdResponse**](../../models/SportPredictionsByFixtureIdResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Date | DateSchema | | optional
Server | ServerSchema | | optional
Cache-Control | CacheControlSchema | | optional
X-RateLimit-Limit | XRateLimitLimitSchema | | optional
X-RateLimit-Remaining | XRateLimitRemainingSchema | | optional
Vary | VarySchema | | optional
Content-Encoding | ContentEncodingSchema | | optional
X-Robots-Tag | XRobotsTagSchema | | optional
Content-Length | ContentLengthSchema | | optional

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRateLimitLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XRateLimitRemainingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRobotsTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **predictions_value_bets_by_fixture_id**

Value Bets by Fixture ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Value Bets by Fixture ID
    predictions_value_bets_by_fixture_id_response = (
        sportmonks.sport.predictions_value_bets_by_fixture_id(
            fixture_id=18535050,  # required
            version="v3",  # optional
            sport="football",  # optional
        )
    )
    pprint(predictions_value_bets_by_fixture_id_response.headers)
    pprint(predictions_value_bets_by_fixture_id_response.status)
    pprint(predictions_value_bets_by_fixture_id_response.round_trip_time)
except ApiException as e:
    print(
        "Exception when calling SportApi.predictions_value_bets_by_fixture_id: %s\n" % e
    )
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
fixtureId | FixtureIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#predictions_value_bets_by_fixture_id.ApiResponseFor200) | Successful response

#### predictions_value_bets_by_fixture_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **referee_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By ID
    referee_by_id_response = sportmonks.sport.referee_by_id(
        referee_id=11698,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(referee_by_id_response.body)
    pprint(referee_by_id_response.body["data"])
    pprint(referee_by_id_response.body["subscription"])
    pprint(referee_by_id_response.body["rate_limit"])
    pprint(referee_by_id_response.body["timezone"])
    pprint(referee_by_id_response.headers)
    pprint(referee_by_id_response.status)
    pprint(referee_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.referee_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
refereeId | RefereeIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RefereeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#referee_by_id.ApiResponseForDefault) | 

#### referee_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportRefereeByIdResponse**](../../models/SportRefereeByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **referees_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    referees_all_response = sportmonks.sport.referees_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(referees_all_response.body)
    pprint(referees_all_response.body["data"])
    pprint(referees_all_response.body["pagination"])
    pprint(referees_all_response.body["subscription"])
    pprint(referees_all_response.body["rate_limit"])
    pprint(referees_all_response.body["timezone"])
    pprint(referees_all_response.headers)
    pprint(referees_all_response.status)
    pprint(referees_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.referees_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#referees_all.ApiResponseForDefault) | 

#### referees_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportRefereesAllResponse**](../../models/SportRefereesAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **referees_by_country_id**

By Country ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Country ID
    referees_by_country_id_response = sportmonks.sport.referees_by_country_id(
        country_id=320,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(referees_by_country_id_response.body)
    pprint(referees_by_country_id_response.body["data"])
    pprint(referees_by_country_id_response.body["pagination"])
    pprint(referees_by_country_id_response.body["subscription"])
    pprint(referees_by_country_id_response.body["rate_limit"])
    pprint(referees_by_country_id_response.body["timezone"])
    pprint(referees_by_country_id_response.headers)
    pprint(referees_by_country_id_response.status)
    pprint(referees_by_country_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.referees_by_country_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
countryId | CountryIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CountryIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#referees_by_country_id.ApiResponseForDefault) | 

#### referees_by_country_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportRefereesByCountryIdResponse**](../../models/SportRefereesByCountryIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **referees_by_season_id**

By Season ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Season ID
    referees_by_season_id_response = sportmonks.sport.referees_by_season_id(
        season_id=19686,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(referees_by_season_id_response.body)
    pprint(referees_by_season_id_response.body["data"])
    pprint(referees_by_season_id_response.body["pagination"])
    pprint(referees_by_season_id_response.body["subscription"])
    pprint(referees_by_season_id_response.body["rate_limit"])
    pprint(referees_by_season_id_response.body["timezone"])
    pprint(referees_by_season_id_response.headers)
    pprint(referees_by_season_id_response.status)
    pprint(referees_by_season_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.referees_by_season_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#referees_by_season_id.ApiResponseForDefault) | 

#### referees_by_season_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportRefereesBySeasonIdResponse**](../../models/SportRefereesBySeasonIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **referees_search**

Search

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Search
    referees_search_response = sportmonks.sport.referees_search(
        name="Munch",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(referees_search_response.body)
    pprint(referees_search_response.body["data"])
    pprint(referees_search_response.body["pagination"])
    pprint(referees_search_response.body["subscription"])
    pprint(referees_search_response.body["rate_limit"])
    pprint(referees_search_response.body["timezone"])
    pprint(referees_search_response.headers)
    pprint(referees_search_response.status)
    pprint(referees_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.referees_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
name | NameSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#referees_search.ApiResponseForDefault) | 

#### referees_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportRefereesSearchResponse**](../../models/SportRefereesSearchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **rivals_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    rivals_all_response = sportmonks.sport.rivals_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(rivals_all_response.body)
    pprint(rivals_all_response.body["data"])
    pprint(rivals_all_response.body["pagination"])
    pprint(rivals_all_response.body["subscription"])
    pprint(rivals_all_response.body["rate_limit"])
    pprint(rivals_all_response.body["timezone"])
    pprint(rivals_all_response.headers)
    pprint(rivals_all_response.status)
    pprint(rivals_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.rivals_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#rivals_all.ApiResponseFor200) | OK

#### rivals_all.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportRivalsAllResponse**](../../models/SportRivalsAllResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Date | DateSchema | | optional
Server | ServerSchema | | optional
Cache-Control | CacheControlSchema | | optional
X-RateLimit-Limit | XRateLimitLimitSchema | | optional
X-RateLimit-Remaining | XRateLimitRemainingSchema | | optional
Vary | VarySchema | | optional
Content-Encoding | ContentEncodingSchema | | optional
X-Robots-Tag | XRobotsTagSchema | | optional
Content-Length | ContentLengthSchema | | optional

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRateLimitLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XRateLimitRemainingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRobotsTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **rivals_by_team_id**

By Team ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Team ID
    rivals_by_team_id_response = sportmonks.sport.rivals_by_team_id(
        team_id=53,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(rivals_by_team_id_response.body)
    pprint(rivals_by_team_id_response.body["data"])
    pprint(rivals_by_team_id_response.body["subscription"])
    pprint(rivals_by_team_id_response.body["rate_limit"])
    pprint(rivals_by_team_id_response.body["timezone"])
    pprint(rivals_by_team_id_response.headers)
    pprint(rivals_by_team_id_response.status)
    pprint(rivals_by_team_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.rivals_by_team_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
teamId | TeamIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#rivals_by_team_id.ApiResponseFor200) | OK

#### rivals_by_team_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportRivalsByTeamIdResponse**](../../models/SportRivalsByTeamIdResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Date | DateSchema | | optional
Server | ServerSchema | | optional
Cache-Control | CacheControlSchema | | optional
X-RateLimit-Limit | XRateLimitLimitSchema | | optional
X-RateLimit-Remaining | XRateLimitRemainingSchema | | optional
Vary | VarySchema | | optional
Content-Encoding | ContentEncodingSchema | | optional
X-Robots-Tag | XRobotsTagSchema | | optional
Content-Length | ContentLengthSchema | | optional

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRateLimitLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XRateLimitRemainingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRobotsTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **round_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By ID
    round_by_id_response = sportmonks.sport.round_by_id(
        round_id=23317,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(round_by_id_response.body)
    pprint(round_by_id_response.body["data"])
    pprint(round_by_id_response.body["subscription"])
    pprint(round_by_id_response.body["rate_limit"])
    pprint(round_by_id_response.body["timezone"])
    pprint(round_by_id_response.headers)
    pprint(round_by_id_response.status)
    pprint(round_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.round_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
roundId | RoundIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RoundIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#round_by_id.ApiResponseForDefault) | 

#### round_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportRoundByIdResponse**](../../models/SportRoundByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **rounds_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    rounds_all_response = sportmonks.sport.rounds_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(rounds_all_response.body)
    pprint(rounds_all_response.body["data"])
    pprint(rounds_all_response.body["pagination"])
    pprint(rounds_all_response.body["subscription"])
    pprint(rounds_all_response.body["rate_limit"])
    pprint(rounds_all_response.body["timezone"])
    pprint(rounds_all_response.headers)
    pprint(rounds_all_response.status)
    pprint(rounds_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.rounds_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#rounds_all.ApiResponseForDefault) | 

#### rounds_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportRoundsAllResponse**](../../models/SportRoundsAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **rounds_by_season_id**

Season ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Season ID
    rounds_by_season_id_response = sportmonks.sport.rounds_by_season_id(
        season_id=19686,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(rounds_by_season_id_response.body)
    pprint(rounds_by_season_id_response.body["data"])
    pprint(rounds_by_season_id_response.body["subscription"])
    pprint(rounds_by_season_id_response.body["rate_limit"])
    pprint(rounds_by_season_id_response.body["timezone"])
    pprint(rounds_by_season_id_response.headers)
    pprint(rounds_by_season_id_response.status)
    pprint(rounds_by_season_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.rounds_by_season_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#rounds_by_season_id.ApiResponseForDefault) | 

#### rounds_by_season_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportRoundsBySeasonIdResponse**](../../models/SportRoundsBySeasonIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **rounds_search**

Search

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Search
    rounds_search_response = sportmonks.sport.rounds_search(
        name=2,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(rounds_search_response.body)
    pprint(rounds_search_response.body["data"])
    pprint(rounds_search_response.body["pagination"])
    pprint(rounds_search_response.body["subscription"])
    pprint(rounds_search_response.body["rate_limit"])
    pprint(rounds_search_response.body["timezone"])
    pprint(rounds_search_response.headers)
    pprint(rounds_search_response.status)
    pprint(rounds_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.rounds_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
name | NameSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#rounds_search.ApiResponseForDefault) | 

#### rounds_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportRoundsSearchResponse**](../../models/SportRoundsSearchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **schedules_by_season_id**

By Season ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Season ID
    schedules_by_season_id_response = sportmonks.sport.schedules_by_season_id(
        season_id=19686,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(schedules_by_season_id_response.body)
    pprint(schedules_by_season_id_response.body["data"])
    pprint(schedules_by_season_id_response.body["subscription"])
    pprint(schedules_by_season_id_response.body["rate_limit"])
    pprint(schedules_by_season_id_response.body["timezone"])
    pprint(schedules_by_season_id_response.headers)
    pprint(schedules_by_season_id_response.status)
    pprint(schedules_by_season_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.schedules_by_season_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#schedules_by_season_id.ApiResponseForDefault) | 

#### schedules_by_season_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportSchedulesBySeasonIdResponse**](../../models/SportSchedulesBySeasonIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **schedules_by_team_and_season_id**

By Team and Season ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Team and Season ID
    schedules_by_team_and_season_id_response = (
        sportmonks.sport.schedules_by_team_and_season_id(
            season_id=19686,  # required
            team_id=282,  # required
            version="v3",  # optional
            sport="football",  # optional
        )
    )
    pprint(schedules_by_team_and_season_id_response.body)
    pprint(schedules_by_team_and_season_id_response.body["data"])
    pprint(schedules_by_team_and_season_id_response.body["subscription"])
    pprint(schedules_by_team_and_season_id_response.body["rate_limit"])
    pprint(schedules_by_team_and_season_id_response.body["timezone"])
    pprint(schedules_by_team_and_season_id_response.headers)
    pprint(schedules_by_team_and_season_id_response.status)
    pprint(schedules_by_team_and_season_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.schedules_by_team_and_season_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 
teamId | TeamIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#schedules_by_team_and_season_id.ApiResponseForDefault) | 

#### schedules_by_team_and_season_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportSchedulesByTeamAndSeasonIdResponse**](../../models/SportSchedulesByTeamAndSeasonIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **schedules_by_team_id**

By Team ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Team ID
    schedules_by_team_id_response = sportmonks.sport.schedules_by_team_id(
        team_id=282,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(schedules_by_team_id_response.body)
    pprint(schedules_by_team_id_response.body["data"])
    pprint(schedules_by_team_id_response.body["subscription"])
    pprint(schedules_by_team_id_response.body["rate_limit"])
    pprint(schedules_by_team_id_response.body["timezone"])
    pprint(schedules_by_team_id_response.headers)
    pprint(schedules_by_team_id_response.status)
    pprint(schedules_by_team_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.schedules_by_team_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
teamId | TeamIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#schedules_by_team_id.ApiResponseForDefault) | 

#### schedules_by_team_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportSchedulesByTeamIdResponse**](../../models/SportSchedulesByTeamIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **season_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By ID
    season_by_id_response = sportmonks.sport.season_by_id(
        season_id=19686,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(season_by_id_response.body)
    pprint(season_by_id_response.body["data"])
    pprint(season_by_id_response.body["subscription"])
    pprint(season_by_id_response.body["rate_limit"])
    pprint(season_by_id_response.body["timezone"])
    pprint(season_by_id_response.headers)
    pprint(season_by_id_response.status)
    pprint(season_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.season_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#season_by_id.ApiResponseForDefault) | 

#### season_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportSeasonByIdResponse**](../../models/SportSeasonByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **seasons_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    seasons_all_response = sportmonks.sport.seasons_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(seasons_all_response.body)
    pprint(seasons_all_response.body["data"])
    pprint(seasons_all_response.body["pagination"])
    pprint(seasons_all_response.body["subscription"])
    pprint(seasons_all_response.body["rate_limit"])
    pprint(seasons_all_response.body["timezone"])
    pprint(seasons_all_response.headers)
    pprint(seasons_all_response.status)
    pprint(seasons_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.seasons_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#seasons_all.ApiResponseForDefault) | 

#### seasons_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportSeasonsAllResponse**](../../models/SportSeasonsAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **seasons_by_team_id**

By Team ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Team ID
    seasons_by_team_id_response = sportmonks.sport.seasons_by_team_id(
        team_id=282,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(seasons_by_team_id_response.headers)
    pprint(seasons_by_team_id_response.status)
    pprint(seasons_by_team_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.seasons_by_team_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
teamId | TeamIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#seasons_by_team_id.ApiResponseForDefault) | 

#### seasons_by_team_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **seasons_search**

Search

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Search
    seasons_search_response = sportmonks.sport.seasons_search(
        name=2022,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(seasons_search_response.body)
    pprint(seasons_search_response.body["data"])
    pprint(seasons_search_response.body["pagination"])
    pprint(seasons_search_response.body["subscription"])
    pprint(seasons_search_response.body["rate_limit"])
    pprint(seasons_search_response.body["timezone"])
    pprint(seasons_search_response.headers)
    pprint(seasons_search_response.status)
    pprint(seasons_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.seasons_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
name | NameSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#seasons_search.ApiResponseForDefault) | 

#### seasons_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportSeasonsSearchResponse**](../../models/SportSeasonsSearchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **squads_by_season_and_team_id**

By Season and Team ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Season and Team ID
    squads_by_season_and_team_id_response = (
        sportmonks.sport.squads_by_season_and_team_id(
            season_id=19686,  # required
            team_id=282,  # required
            version="v3",  # optional
            sport="football",  # optional
        )
    )
    pprint(squads_by_season_and_team_id_response.body)
    pprint(squads_by_season_and_team_id_response.body["data"])
    pprint(squads_by_season_and_team_id_response.body["message"])
    pprint(squads_by_season_and_team_id_response.body["subscription"])
    pprint(squads_by_season_and_team_id_response.body["rate_limit"])
    pprint(squads_by_season_and_team_id_response.body["timezone"])
    pprint(squads_by_season_and_team_id_response.headers)
    pprint(squads_by_season_and_team_id_response.status)
    pprint(squads_by_season_and_team_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.squads_by_season_and_team_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 
teamId | TeamIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#squads_by_season_and_team_id.ApiResponseForDefault) | 

#### squads_by_season_and_team_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportSquadsBySeasonAndTeamIdResponse**](../../models/SportSquadsBySeasonAndTeamIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **squads_by_team_id**

By Team ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Team ID
    squads_by_team_id_response = sportmonks.sport.squads_by_team_id(
        team_id=282,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(squads_by_team_id_response.body)
    pprint(squads_by_team_id_response.body["data"])
    pprint(squads_by_team_id_response.body["subscription"])
    pprint(squads_by_team_id_response.body["rate_limit"])
    pprint(squads_by_team_id_response.body["timezone"])
    pprint(squads_by_team_id_response.headers)
    pprint(squads_by_team_id_response.status)
    pprint(squads_by_team_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.squads_by_team_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
teamId | TeamIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#squads_by_team_id.ApiResponseForDefault) | 

#### squads_by_team_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportSquadsByTeamIdResponse**](../../models/SportSquadsByTeamIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **stage_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By ID
    stage_by_id_response = sportmonks.sport.stage_by_id(
        stage_id=1100,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(stage_by_id_response.body)
    pprint(stage_by_id_response.body["data"])
    pprint(stage_by_id_response.body["subscription"])
    pprint(stage_by_id_response.body["rate_limit"])
    pprint(stage_by_id_response.body["timezone"])
    pprint(stage_by_id_response.headers)
    pprint(stage_by_id_response.status)
    pprint(stage_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.stage_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
stageId | StageIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#stage_by_id.ApiResponseForDefault) | 

#### stage_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportStageByIdResponse**](../../models/SportStageByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **stages_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    stages_all_response = sportmonks.sport.stages_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(stages_all_response.body)
    pprint(stages_all_response.body["data"])
    pprint(stages_all_response.body["pagination"])
    pprint(stages_all_response.body["subscription"])
    pprint(stages_all_response.body["rate_limit"])
    pprint(stages_all_response.body["timezone"])
    pprint(stages_all_response.headers)
    pprint(stages_all_response.status)
    pprint(stages_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.stages_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#stages_all.ApiResponseForDefault) | 

#### stages_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportStagesAllResponse**](../../models/SportStagesAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **stages_by_season_id**

By Season ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Season ID
    stages_by_season_id_response = sportmonks.sport.stages_by_season_id(
        season_id=19686,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(stages_by_season_id_response.body)
    pprint(stages_by_season_id_response.body["data"])
    pprint(stages_by_season_id_response.body["subscription"])
    pprint(stages_by_season_id_response.body["rate_limit"])
    pprint(stages_by_season_id_response.body["timezone"])
    pprint(stages_by_season_id_response.headers)
    pprint(stages_by_season_id_response.status)
    pprint(stages_by_season_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.stages_by_season_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#stages_by_season_id.ApiResponseForDefault) | 

#### stages_by_season_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportStagesBySeasonIdResponse**](../../models/SportStagesBySeasonIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **stages_search**

Search

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Search
    stages_search_response = sportmonks.sport.stages_search(
        name="Championship",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(stages_search_response.body)
    pprint(stages_search_response.body["data"])
    pprint(stages_search_response.body["pagination"])
    pprint(stages_search_response.body["subscription"])
    pprint(stages_search_response.body["rate_limit"])
    pprint(stages_search_response.body["timezone"])
    pprint(stages_search_response.headers)
    pprint(stages_search_response.status)
    pprint(stages_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.stages_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
name | NameSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#stages_search.ApiResponseForDefault) | 

#### stages_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportStagesSearchResponse**](../../models/SportStagesSearchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **standing_corrections_by_season_id**

Correction by Season ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Correction by Season ID
    standing_corrections_by_season_id_response = (
        sportmonks.sport.standing_corrections_by_season_id(
            season_id=19686,  # required
            version="v3",  # optional
            sport="football",  # optional
        )
    )
    pprint(standing_corrections_by_season_id_response.body)
    pprint(standing_corrections_by_season_id_response.body["data"])
    pprint(standing_corrections_by_season_id_response.body["message"])
    pprint(standing_corrections_by_season_id_response.body["subscription"])
    pprint(standing_corrections_by_season_id_response.body["rate_limit"])
    pprint(standing_corrections_by_season_id_response.body["timezone"])
    pprint(standing_corrections_by_season_id_response.headers)
    pprint(standing_corrections_by_season_id_response.status)
    pprint(standing_corrections_by_season_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.standing_corrections_by_season_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#standing_corrections_by_season_id.ApiResponseForDefault) | 

#### standing_corrections_by_season_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportStandingCorrectionsBySeasonIdResponse**](../../models/SportStandingCorrectionsBySeasonIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **standings_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    standings_all_response = sportmonks.sport.standings_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(standings_all_response.body)
    pprint(standings_all_response.body["data"])
    pprint(standings_all_response.body["pagination"])
    pprint(standings_all_response.body["subscription"])
    pprint(standings_all_response.body["rate_limit"])
    pprint(standings_all_response.body["timezone"])
    pprint(standings_all_response.headers)
    pprint(standings_all_response.status)
    pprint(standings_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.standings_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#standings_all.ApiResponseForDefault) | 

#### standings_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportStandingsAllResponse**](../../models/SportStandingsAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **standings_by_round_id**

By Round ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Round ID
    standings_by_round_id_response = sportmonks.sport.standings_by_round_id(
        round_id=23318,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(standings_by_round_id_response.body)
    pprint(standings_by_round_id_response.body["data"])
    pprint(standings_by_round_id_response.body["message"])
    pprint(standings_by_round_id_response.body["subscription"])
    pprint(standings_by_round_id_response.body["rate_limit"])
    pprint(standings_by_round_id_response.body["timezone"])
    pprint(standings_by_round_id_response.headers)
    pprint(standings_by_round_id_response.status)
    pprint(standings_by_round_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.standings_by_round_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
roundId | RoundIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RoundIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#standings_by_round_id.ApiResponseForDefault) | 

#### standings_by_round_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportStandingsByRoundIdResponse**](../../models/SportStandingsByRoundIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **standings_by_season_id**

By Season ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Season ID
    standings_by_season_id_response = sportmonks.sport.standings_by_season_id(
        season_id=19686,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(standings_by_season_id_response.body)
    pprint(standings_by_season_id_response.body["data"])
    pprint(standings_by_season_id_response.body["subscription"])
    pprint(standings_by_season_id_response.body["rate_limit"])
    pprint(standings_by_season_id_response.body["timezone"])
    pprint(standings_by_season_id_response.headers)
    pprint(standings_by_season_id_response.status)
    pprint(standings_by_season_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.standings_by_season_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#standings_by_season_id.ApiResponseForDefault) | 

#### standings_by_season_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportStandingsBySeasonIdResponse**](../../models/SportStandingsBySeasonIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **standings_live_by_league_id**

By League ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By League ID
    standings_live_by_league_id_response = sportmonks.sport.standings_live_by_league_id(
        league_id=271,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(standings_live_by_league_id_response.body)
    pprint(standings_live_by_league_id_response.body["data"])
    pprint(standings_live_by_league_id_response.body["subscription"])
    pprint(standings_live_by_league_id_response.body["rate_limit"])
    pprint(standings_live_by_league_id_response.body["timezone"])
    pprint(standings_live_by_league_id_response.headers)
    pprint(standings_live_by_league_id_response.status)
    pprint(standings_live_by_league_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.standings_live_by_league_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
leagueId | LeagueIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LeagueIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#standings_live_by_league_id.ApiResponseFor200) | OK

#### standings_live_by_league_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportStandingsLiveByLeagueIdResponse**](../../models/SportStandingsLiveByLeagueIdResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Date | DateSchema | | optional
Server | ServerSchema | | optional
Cache-Control | CacheControlSchema | | optional
X-RateLimit-Limit | XRateLimitLimitSchema | | optional
X-RateLimit-Remaining | XRateLimitRemainingSchema | | optional
Vary | VarySchema | | optional
Content-Encoding | ContentEncodingSchema | | optional
X-Robots-Tag | XRobotsTagSchema | | optional
Content-Length | ContentLengthSchema | | optional

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRateLimitLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XRateLimitRemainingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRobotsTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **state_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By ID
    state_by_id_response = sportmonks.sport.state_by_id(
        state_id=1,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(state_by_id_response.body)
    pprint(state_by_id_response.body["data"])
    pprint(state_by_id_response.body["subscription"])
    pprint(state_by_id_response.body["rate_limit"])
    pprint(state_by_id_response.body["timezone"])
    pprint(state_by_id_response.headers)
    pprint(state_by_id_response.status)
    pprint(state_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.state_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
stateId | StateIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#state_by_id.ApiResponseForDefault) | 

#### state_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportStateByIdResponse**](../../models/SportStateByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **states_by_sport**

By Sport

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Sport
    states_by_sport_response = sportmonks.sport.states_by_sport(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(states_by_sport_response.body)
    pprint(states_by_sport_response.body["data"])
    pprint(states_by_sport_response.body["pagination"])
    pprint(states_by_sport_response.body["subscription"])
    pprint(states_by_sport_response.body["rate_limit"])
    pprint(states_by_sport_response.body["timezone"])
    pprint(states_by_sport_response.headers)
    pprint(states_by_sport_response.status)
    pprint(states_by_sport_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.states_by_sport: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#states_by_sport.ApiResponseForDefault) | 

#### states_by_sport.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportStatesBySportResponse**](../../models/SportStatesBySportResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **teams_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    teams_all_response = sportmonks.sport.teams_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(teams_all_response.body)
    pprint(teams_all_response.body["data"])
    pprint(teams_all_response.body["pagination"])
    pprint(teams_all_response.body["subscription"])
    pprint(teams_all_response.body["rate_limit"])
    pprint(teams_all_response.body["timezone"])
    pprint(teams_all_response.headers)
    pprint(teams_all_response.status)
    pprint(teams_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.teams_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#teams_all.ApiResponseForDefault) | 

#### teams_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTeamsAllResponse**](../../models/SportTeamsAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **teams_by_country_id**

By Country ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Country ID
    teams_by_country_id_response = sportmonks.sport.teams_by_country_id(
        country_id=320,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(teams_by_country_id_response.body)
    pprint(teams_by_country_id_response.body["data"])
    pprint(teams_by_country_id_response.body["pagination"])
    pprint(teams_by_country_id_response.body["subscription"])
    pprint(teams_by_country_id_response.body["rate_limit"])
    pprint(teams_by_country_id_response.body["timezone"])
    pprint(teams_by_country_id_response.headers)
    pprint(teams_by_country_id_response.status)
    pprint(teams_by_country_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.teams_by_country_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
countryId | CountryIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CountryIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#teams_by_country_id.ApiResponseForDefault) | 

#### teams_by_country_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTeamsByCountryIdResponse**](../../models/SportTeamsByCountryIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **teams_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By ID
    teams_by_id_response = sportmonks.sport.teams_by_id(
        team_id=180,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(teams_by_id_response.body)
    pprint(teams_by_id_response.body["data"])
    pprint(teams_by_id_response.body["subscription"])
    pprint(teams_by_id_response.body["rate_limit"])
    pprint(teams_by_id_response.body["timezone"])
    pprint(teams_by_id_response.headers)
    pprint(teams_by_id_response.status)
    pprint(teams_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.teams_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
teamId | TeamIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#teams_by_id.ApiResponseForDefault) | 

#### teams_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTeamsByIdResponse**](../../models/SportTeamsByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **teams_by_season_id**

By Season ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Season ID
    teams_by_season_id_response = sportmonks.sport.teams_by_season_id(
        season_id=19686,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(teams_by_season_id_response.body)
    pprint(teams_by_season_id_response.body["data"])
    pprint(teams_by_season_id_response.body["subscription"])
    pprint(teams_by_season_id_response.body["rate_limit"])
    pprint(teams_by_season_id_response.body["timezone"])
    pprint(teams_by_season_id_response.headers)
    pprint(teams_by_season_id_response.status)
    pprint(teams_by_season_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.teams_by_season_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#teams_by_season_id.ApiResponseForDefault) | 

#### teams_by_season_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTeamsBySeasonIdResponse**](../../models/SportTeamsBySeasonIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **teams_search**

Search

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Search
    teams_search_response = sportmonks.sport.teams_search(
        name="Hors",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(teams_search_response.body)
    pprint(teams_search_response.body["data"])
    pprint(teams_search_response.body["pagination"])
    pprint(teams_search_response.body["subscription"])
    pprint(teams_search_response.body["rate_limit"])
    pprint(teams_search_response.body["timezone"])
    pprint(teams_search_response.headers)
    pprint(teams_search_response.status)
    pprint(teams_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.teams_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
name | NameSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#teams_search.ApiResponseForDefault) | 

#### teams_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTeamsSearchResponse**](../../models/SportTeamsSearchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **top_scorers_by_season_id**

By Season ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Season ID
    top_scorers_by_season_id_response = sportmonks.sport.top_scorers_by_season_id(
        season_id=19686,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(top_scorers_by_season_id_response.body)
    pprint(top_scorers_by_season_id_response.body["data"])
    pprint(top_scorers_by_season_id_response.body["pagination"])
    pprint(top_scorers_by_season_id_response.body["subscription"])
    pprint(top_scorers_by_season_id_response.body["rate_limit"])
    pprint(top_scorers_by_season_id_response.body["timezone"])
    pprint(top_scorers_by_season_id_response.headers)
    pprint(top_scorers_by_season_id_response.status)
    pprint(top_scorers_by_season_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.top_scorers_by_season_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#top_scorers_by_season_id.ApiResponseForDefault) | 

#### top_scorers_by_season_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTopScorersBySeasonIdResponse**](../../models/SportTopScorersBySeasonIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **top_scorers_by_stage_id**

By Stage ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Stage ID
    top_scorers_by_stage_id_response = sportmonks.sport.top_scorers_by_stage_id(
        stage_id=1100,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(top_scorers_by_stage_id_response.body)
    pprint(top_scorers_by_stage_id_response.body["data"])
    pprint(top_scorers_by_stage_id_response.body["pagination"])
    pprint(top_scorers_by_stage_id_response.body["subscription"])
    pprint(top_scorers_by_stage_id_response.body["rate_limit"])
    pprint(top_scorers_by_stage_id_response.body["timezone"])
    pprint(top_scorers_by_stage_id_response.headers)
    pprint(top_scorers_by_stage_id_response.status)
    pprint(top_scorers_by_stage_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.top_scorers_by_stage_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
stageId | StageIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#top_scorers_by_stage_id.ApiResponseForDefault) | 

#### top_scorers_by_stage_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTopScorersByStageIdResponse**](../../models/SportTopScorersByStageIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tranfers_by_date_range**

By Date Range

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Date Range
    tranfers_by_date_range_response = sportmonks.sport.tranfers_by_date_range(
        start_date="2021-12-27",  # required
        end_date="2021-12-30",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(tranfers_by_date_range_response.body)
    pprint(tranfers_by_date_range_response.body["data"])
    pprint(tranfers_by_date_range_response.body["pagination"])
    pprint(tranfers_by_date_range_response.body["subscription"])
    pprint(tranfers_by_date_range_response.body["rate_limit"])
    pprint(tranfers_by_date_range_response.body["timezone"])
    pprint(tranfers_by_date_range_response.headers)
    pprint(tranfers_by_date_range_response.status)
    pprint(tranfers_by_date_range_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.tranfers_by_date_range: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
startDate | StartDateSchema | | 
endDate | EndDateSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EndDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#tranfers_by_date_range.ApiResponseForDefault) | 

#### tranfers_by_date_range.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTranfersByDateRangeResponse**](../../models/SportTranfersByDateRangeResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **transfer_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By ID
    transfer_by_id_response = sportmonks.sport.transfer_by_id(
        transfer_id=1,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(transfer_by_id_response.body)
    pprint(transfer_by_id_response.body["data"])
    pprint(transfer_by_id_response.body["subscription"])
    pprint(transfer_by_id_response.body["rate_limit"])
    pprint(transfer_by_id_response.body["timezone"])
    pprint(transfer_by_id_response.headers)
    pprint(transfer_by_id_response.status)
    pprint(transfer_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.transfer_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
transferId | TransferIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TransferIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#transfer_by_id.ApiResponseFor200) | OK

#### transfer_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTransferByIdResponse**](../../models/SportTransferByIdResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Date | DateSchema | | optional
Server | ServerSchema | | optional
Cache-Control | CacheControlSchema | | optional
X-RateLimit-Limit | XRateLimitLimitSchema | | optional
X-RateLimit-Remaining | XRateLimitRemainingSchema | | optional
Vary | VarySchema | | optional
Content-Encoding | ContentEncodingSchema | | optional
X-Robots-Tag | XRobotsTagSchema | | optional
Content-Length | ContentLengthSchema | | optional

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRateLimitLimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# XRateLimitRemainingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VarySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRobotsTagSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **transfers_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    transfers_all_response = sportmonks.sport.transfers_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(transfers_all_response.body)
    pprint(transfers_all_response.body["data"])
    pprint(transfers_all_response.body["pagination"])
    pprint(transfers_all_response.body["subscription"])
    pprint(transfers_all_response.body["rate_limit"])
    pprint(transfers_all_response.body["timezone"])
    pprint(transfers_all_response.headers)
    pprint(transfers_all_response.status)
    pprint(transfers_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.transfers_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#transfers_all.ApiResponseForDefault) | 

#### transfers_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTransfersAllResponse**](../../models/SportTransfersAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **transfers_by_player_id**

By Player ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Player ID
    transfers_by_player_id_response = sportmonks.sport.transfers_by_player_id(
        player_id=35659846,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(transfers_by_player_id_response.body)
    pprint(transfers_by_player_id_response.body["data"])
    pprint(transfers_by_player_id_response.body["pagination"])
    pprint(transfers_by_player_id_response.body["subscription"])
    pprint(transfers_by_player_id_response.body["rate_limit"])
    pprint(transfers_by_player_id_response.body["timezone"])
    pprint(transfers_by_player_id_response.headers)
    pprint(transfers_by_player_id_response.status)
    pprint(transfers_by_player_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.transfers_by_player_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
playerId | PlayerIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PlayerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#transfers_by_player_id.ApiResponseForDefault) | 

#### transfers_by_player_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTransfersByPlayerIdResponse**](../../models/SportTransfersByPlayerIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **transfers_by_team_id**

By Team ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Team ID
    transfers_by_team_id_response = sportmonks.sport.transfers_by_team_id(
        team_id=3736,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(transfers_by_team_id_response.body)
    pprint(transfers_by_team_id_response.body["data"])
    pprint(transfers_by_team_id_response.body["pagination"])
    pprint(transfers_by_team_id_response.body["subscription"])
    pprint(transfers_by_team_id_response.body["rate_limit"])
    pprint(transfers_by_team_id_response.body["timezone"])
    pprint(transfers_by_team_id_response.headers)
    pprint(transfers_by_team_id_response.status)
    pprint(transfers_by_team_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.transfers_by_team_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
teamId | TeamIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TeamIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#transfers_by_team_id.ApiResponseForDefault) | 

#### transfers_by_team_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTransfersByTeamIdResponse**](../../models/SportTransfersByTeamIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **transfers_latest**

Last Updated

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Last Updated
    transfers_latest_response = sportmonks.sport.transfers_latest(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(transfers_latest_response.body)
    pprint(transfers_latest_response.body["data"])
    pprint(transfers_latest_response.body["pagination"])
    pprint(transfers_latest_response.body["subscription"])
    pprint(transfers_latest_response.body["rate_limit"])
    pprint(transfers_latest_response.body["timezone"])
    pprint(transfers_latest_response.headers)
    pprint(transfers_latest_response.status)
    pprint(transfers_latest_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.transfers_latest: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#transfers_latest.ApiResponseForDefault) | 

#### transfers_latest.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTransfersLatestResponse**](../../models/SportTransfersLatestResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tv_station_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By ID
    tv_station_by_id_response = sportmonks.sport.tv_station_by_id(
        tv_station_id=33,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(tv_station_by_id_response.body)
    pprint(tv_station_by_id_response.body["data"])
    pprint(tv_station_by_id_response.body["subscription"])
    pprint(tv_station_by_id_response.body["rate_limit"])
    pprint(tv_station_by_id_response.body["timezone"])
    pprint(tv_station_by_id_response.headers)
    pprint(tv_station_by_id_response.status)
    pprint(tv_station_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.tv_station_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
tvStationId | TvStationIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TvStationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#tv_station_by_id.ApiResponseForDefault) | 

#### tv_station_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTvStationByIdResponse**](../../models/SportTvStationByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tv_stations_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    tv_stations_all_response = sportmonks.sport.tv_stations_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(tv_stations_all_response.body)
    pprint(tv_stations_all_response.body["data"])
    pprint(tv_stations_all_response.body["pagination"])
    pprint(tv_stations_all_response.body["subscription"])
    pprint(tv_stations_all_response.body["rate_limit"])
    pprint(tv_stations_all_response.body["timezone"])
    pprint(tv_stations_all_response.headers)
    pprint(tv_stations_all_response.status)
    pprint(tv_stations_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.tv_stations_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#tv_stations_all.ApiResponseForDefault) | 

#### tv_stations_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTvStationsAllResponse**](../../models/SportTvStationsAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tv_stations_by_fixture_id**

By Fixture ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Fixture ID
    tv_stations_by_fixture_id_response = sportmonks.sport.tv_stations_by_fixture_id(
        fixture_id=16808591,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(tv_stations_by_fixture_id_response.body)
    pprint(tv_stations_by_fixture_id_response.body["data"])
    pprint(tv_stations_by_fixture_id_response.body["message"])
    pprint(tv_stations_by_fixture_id_response.body["subscription"])
    pprint(tv_stations_by_fixture_id_response.body["rate_limit"])
    pprint(tv_stations_by_fixture_id_response.body["timezone"])
    pprint(tv_stations_by_fixture_id_response.headers)
    pprint(tv_stations_by_fixture_id_response.status)
    pprint(tv_stations_by_fixture_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.tv_stations_by_fixture_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
fixtureId | FixtureIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#tv_stations_by_fixture_id.ApiResponseForDefault) | 

#### tv_stations_by_fixture_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportTvStationsByFixtureIdResponse**](../../models/SportTvStationsByFixtureIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **venue_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By ID
    venue_by_id_response = sportmonks.sport.venue_by_id(
        venue_id=219,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(venue_by_id_response.body)
    pprint(venue_by_id_response.body["data"])
    pprint(venue_by_id_response.body["subscription"])
    pprint(venue_by_id_response.body["rate_limit"])
    pprint(venue_by_id_response.body["timezone"])
    pprint(venue_by_id_response.headers)
    pprint(venue_by_id_response.status)
    pprint(venue_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.venue_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
venueId | VenueIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VenueIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#venue_by_id.ApiResponseForDefault) | 

#### venue_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportVenueByIdResponse**](../../models/SportVenueByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **venues_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # All
    venues_all_response = sportmonks.sport.venues_all(
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(venues_all_response.body)
    pprint(venues_all_response.body["data"])
    pprint(venues_all_response.body["pagination"])
    pprint(venues_all_response.body["subscription"])
    pprint(venues_all_response.body["rate_limit"])
    pprint(venues_all_response.body["timezone"])
    pprint(venues_all_response.headers)
    pprint(venues_all_response.status)
    pprint(venues_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.venues_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#venues_all.ApiResponseForDefault) | 

#### venues_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportVenuesAllResponse**](../../models/SportVenuesAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **venues_by_season_id**

By Season ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # By Season ID
    venues_by_season_id_response = sportmonks.sport.venues_by_season_id(
        season_id=19686,  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(venues_by_season_id_response.body)
    pprint(venues_by_season_id_response.body["data"])
    pprint(venues_by_season_id_response.body["subscription"])
    pprint(venues_by_season_id_response.body["rate_limit"])
    pprint(venues_by_season_id_response.body["timezone"])
    pprint(venues_by_season_id_response.headers)
    pprint(venues_by_season_id_response.status)
    pprint(venues_by_season_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.venues_by_season_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
seasonId | SeasonIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SeasonIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#venues_by_season_id.ApiResponseForDefault) | 

#### venues_by_season_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportVenuesBySeasonIdResponse**](../../models/SportVenuesBySeasonIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **venues_search**

Search

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
    version="VERSION",
    sport="SPORT",
    # Configure API key authorization: apikeyAuth
    api_key="YOUR_API_KEY",
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # api_key_prefix = {'apikeyAuth': 'Bearer'},
)

try:
    # Search
    venues_search_response = sportmonks.sport.venues_search(
        name="Park",  # required
        version="v3",  # optional
        sport="football",  # optional
    )
    pprint(venues_search_response.body)
    pprint(venues_search_response.body["data"])
    pprint(venues_search_response.body["pagination"])
    pprint(venues_search_response.body["subscription"])
    pprint(venues_search_response.body["rate_limit"])
    pprint(venues_search_response.body["timezone"])
    pprint(venues_search_response.headers)
    pprint(venues_search_response.status)
    pprint(venues_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling SportApi.venues_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | optional
sport | SportSchema | | optional
name | NameSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#venues_search.ApiResponseForDefault) | 

#### venues_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SportVenuesSearchResponse**](../../models/SportVenuesSearchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

