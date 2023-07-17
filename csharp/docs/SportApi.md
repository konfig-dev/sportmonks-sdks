# Sportmonks.Net.Api.SportApi

All URIs are relative to *https://api.sportmonks.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CoachById**](SportApi.md#coachbyid) | **GET** /{version}/{sport}/coaches/{coachId} | By ID |
| [**CoachesAll**](SportApi.md#coachesall) | **GET** /{version}/{sport}/coaches | All |
| [**CoachesByCountryId**](SportApi.md#coachesbycountryid) | **GET** /{version}/{sport}/coaches/countries/{countryId} | By Country ID |
| [**CoachesLatest**](SportApi.md#coacheslatest) | **GET** /{version}/{sport}/coaches/latest | Last updated |
| [**CoachesSearch**](SportApi.md#coachessearch) | **GET** /{version}/{sport}/coaches/search/{name} | Search |
| [**CommentariesAll**](SportApi.md#commentariesall) | **GET** /{version}/{sport}/commentaries | All |
| [**CommentariesByFixtureId**](SportApi.md#commentariesbyfixtureid) | **GET** /{version}/{sport}/commentaries/fixtures/{fixtureId} | By Fixture ID |
| [**FixtureByDateRangeForTeam**](SportApi.md#fixturebydaterangeforteam) | **GET** /{version}/{sport}/fixtures/between/{startDate}/{endDate}/{teamId} | By Date Range for Team |
| [**FixtureById**](SportApi.md#fixturebyid) | **GET** /{version}/{sport}/fixtures/{fixtureId} | Fixture ID |
| [**FixturesAll**](SportApi.md#fixturesall) | **GET** /{version}/{sport}/fixtures | All |
| [**FixturesByDate**](SportApi.md#fixturesbydate) | **GET** /{version}/{sport}/fixtures/date/{date} | By Date |
| [**FixturesByDateRange**](SportApi.md#fixturesbydaterange) | **GET** /{version}/{sport}/fixtures/between/{startDate}/{endDate} | By Date Range |
| [**FixturesByIds**](SportApi.md#fixturesbyids) | **GET** /{version}/{sport}/fixtures/multi/{fixtureIds} | By IDs |
| [**FixturesHeadToHead**](SportApi.md#fixturesheadtohead) | **GET** /{version}/{sport}/fixtures/head-to-head/{firstTeam}/{secondTeam} | Head to Head |
| [**FixturesLatest**](SportApi.md#fixtureslatest) | **GET** /{version}/{sport}/fixtures/latest | Last Updated |
| [**FixturesSearch**](SportApi.md#fixturessearch) | **GET** /{version}/{sport}/fixtures/search/{name} | Search |
| [**LeagueById**](SportApi.md#leaguebyid) | **GET** /{version}/{sport}/leagues/{leagueId} | By ID |
| [**LeagueEnrichments**](SportApi.md#leagueenrichments) | **GET** /{version}/{sport}/leagues/{leagueId}/includes | Enrichments |
| [**LeagueShirts**](SportApi.md#leagueshirts) | **GET** /{version}/{sport}/leagues/{leagueId}/jerseys | Shirts By League ID |
| [**LeaguesAll**](SportApi.md#leaguesall) | **GET** /{version}/{sport}/leagues | All |
| [**LeaguesByCountryId**](SportApi.md#leaguesbycountryid) | **GET** /{version}/{sport}/leagues/countries/{countryId} | By Country ID |
| [**LeaguesByDate**](SportApi.md#leaguesbydate) | **GET** /{version}/{sport}/leagues/date/{date} | By Date |
| [**LeaguesByTeamId**](SportApi.md#leaguesbyteamid) | **GET** /{version}/{sport}/teams/{teamId}/leagues | Leagues By Team ID |
| [**LeaguesCurrentByTeamId**](SportApi.md#leaguescurrentbyteamid) | **GET** /{version}/{sport}/teams/{teamId}/leagues/current | Current Leagues By Team ID |
| [**LeaguesLive**](SportApi.md#leagueslive) | **GET** /{version}/{sport}/leagues/live | Live |
| [**LeaguesSearch**](SportApi.md#leaguessearch) | **GET** /{version}/{sport}/leagues/search/{name} | Search |
| [**LivescoresAll**](SportApi.md#livescoresall) | **GET** /{version}/{sport}/livescores | All |
| [**LivescoresAllInPlay**](SportApi.md#livescoresallinplay) | **GET** /{version}/{sport}/livescores/inplay | All In-play |
| [**LivescoresLatest**](SportApi.md#livescoreslatest) | **GET** /{version}/{sport}/livescores/latest | Last Updated In-play |
| [**NewsAllPostMatch**](SportApi.md#newsallpostmatch) | **GET** /{version}/{sport}/news/post-match | All Post Match |
| [**NewsAllPreMatch**](SportApi.md#newsallprematch) | **GET** /{version}/{sport}/news/pre-match | All Pre-match |
| [**NewsPostMatchBySeasonId**](SportApi.md#newspostmatchbyseasonid) | **GET** /{version}/{sport}/news/post-match/seasons/{seasonId} | Post Match by Season ID |
| [**NewsPreMatchBySeasonId**](SportApi.md#newsprematchbyseasonid) | **GET** /{version}/{sport}/news/pre-match/seasons/{seasonId} | Pre-match By Season ID |
| [**NewsUpcomingPostMatch**](SportApi.md#newsupcomingpostmatch) | **GET** /{version}/{sport}/news/post-match/upcoming | Upcoming Post Match |
| [**NewsUpcomingPreMatch**](SportApi.md#newsupcomingprematch) | **GET** /{version}/{sport}/news/pre-match/upcoming | Upcoming Pre-match |
| [**OddsAllInPlay**](SportApi.md#oddsallinplay) | **GET** /{version}/{sport}/odds/inplay | All In-play |
| [**OddsAllPreMatch**](SportApi.md#oddsallprematch) | **GET** /{version}/{sport}/odds/pre-match | All Pre-match |
| [**OddsInPlayByFixtureAndBookmakerId**](SportApi.md#oddsinplaybyfixtureandbookmakerid) | **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}/bookmakers/{bookmakerId} | In-play by Fixture and Bookmaker ID |
| [**OddsInPlayByFixtureAndMarketId**](SportApi.md#oddsinplaybyfixtureandmarketid) | **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}/markets/{marketId} | In-play by Fixture and Market ID |
| [**OddsInPlayByFixtureId**](SportApi.md#oddsinplaybyfixtureid) | **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId} | In-play by Fixture ID |
| [**OddsLatestInPlay**](SportApi.md#oddslatestinplay) | **GET** /{version}/{sport}/odds/inplay/latest | Latest In-play |
| [**OddsLatestPreMatch**](SportApi.md#oddslatestprematch) | **GET** /{version}/{sport}/odds/pre-match/latest | Last Updated Pre-match |
| [**OddsPreMatchByFixtureAndBookmakerId**](SportApi.md#oddsprematchbyfixtureandbookmakerid) | **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}/bookmakers/{bookmakerId} | Pre-match by Fixture and Bookmaker ID |
| [**OddsPreMatchByFixtureAndMarketId**](SportApi.md#oddsprematchbyfixtureandmarketid) | **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}/markets/{marketId} | Pre-match by Fixture and Market ID |
| [**OddsPreMatchByFixtureId**](SportApi.md#oddsprematchbyfixtureid) | **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId} | Pre-match by Fixture ID |
| [**PlayerById**](SportApi.md#playerbyid) | **GET** /{version}/{sport}/players/{playerId} | By ID |
| [**PlayersAll**](SportApi.md#playersall) | **GET** /{version}/{sport}/players | All |
| [**PlayersByCountryId**](SportApi.md#playersbycountryid) | **GET** /{version}/{sport}/players/countries/{countryId} | By Country ID |
| [**PlayersLatest**](SportApi.md#playerslatest) | **GET** /{version}/{sport}/players/latest | Latest Updated |
| [**PlayersSearch**](SportApi.md#playerssearch) | **GET** /{version}/{sport}/players/search/{name} | Search |
| [**PredictionsAll**](SportApi.md#predictionsall) | **GET** /{version}/{sport}/predictions/probabilities | All |
| [**PredictionsAllValueBets**](SportApi.md#predictionsallvaluebets) | **GET** /{version}/{sport}/predictions/value-bets | All Value Bets |
| [**PredictionsByFixtureId**](SportApi.md#predictionsbyfixtureid) | **GET** /{version}/{sport}/predictions/probabilities/fixtures/{fixtureId} | By Fixture ID |
| [**PredictionsValueBetsByFixtureId**](SportApi.md#predictionsvaluebetsbyfixtureid) | **GET** /{version}/{sport}/predictions/value-bets/fixtures/{fixtureId} | Value Bets by Fixture ID |
| [**RefereeById**](SportApi.md#refereebyid) | **GET** /{version}/{sport}/referees/{refereeId} | By ID |
| [**RefereesAll**](SportApi.md#refereesall) | **GET** /{version}/{sport}/referees | All |
| [**RefereesByCountryId**](SportApi.md#refereesbycountryid) | **GET** /{version}/{sport}/referees/countries/{countryId} | By Country ID |
| [**RefereesBySeasonId**](SportApi.md#refereesbyseasonid) | **GET** /{version}/{sport}/referees/seasons/{seasonId} | By Season ID |
| [**RefereesSearch**](SportApi.md#refereessearch) | **GET** /{version}/{sport}/referees/search/{name} | Search |
| [**RivalsAll**](SportApi.md#rivalsall) | **GET** /{version}/{sport}/rivals | All |
| [**RivalsByTeamId**](SportApi.md#rivalsbyteamid) | **GET** /{version}/{sport}/rivals/teams/{teamId} | By Team ID |
| [**RoundById**](SportApi.md#roundbyid) | **GET** /{version}/{sport}/rounds/{roundId} | By ID |
| [**RoundsAll**](SportApi.md#roundsall) | **GET** /{version}/{sport}/rounds | All |
| [**RoundsBySeasonId**](SportApi.md#roundsbyseasonid) | **GET** /{version}/{sport}/rounds/seasons/{seasonId} | Season ID |
| [**RoundsSearch**](SportApi.md#roundssearch) | **GET** /{version}/{sport}/rounds/search/{name} | Search |
| [**SchedulesBySeasonId**](SportApi.md#schedulesbyseasonid) | **GET** /{version}/{sport}/schedules/seasons/{seasonId} | By Season ID |
| [**SchedulesByTeamAndSeasonId**](SportApi.md#schedulesbyteamandseasonid) | **GET** /{version}/{sport}/schedules/seasons/{seasonId}/teams/{teamId} | By Team and Season ID |
| [**SchedulesByTeamId**](SportApi.md#schedulesbyteamid) | **GET** /{version}/{sport}/schedules/teams/{teamId} | By Team ID |
| [**SeasonById**](SportApi.md#seasonbyid) | **GET** /{version}/{sport}/seasons/{seasonId} | By ID |
| [**SeasonsAll**](SportApi.md#seasonsall) | **GET** /{version}/{sport}/seasons | All |
| [**SeasonsByTeamId**](SportApi.md#seasonsbyteamid) | **GET** /{version}/{sport}/seasons/teams/{teamId} | By Team ID |
| [**SeasonsSearch**](SportApi.md#seasonssearch) | **GET** /{version}/{sport}/seasons/search/{name} | Search |
| [**SquadsBySeasonAndTeamId**](SportApi.md#squadsbyseasonandteamid) | **GET** /{version}/{sport}/squads/seasons/{seasonId}/teams/{teamId} | By Season and Team ID |
| [**SquadsByTeamId**](SportApi.md#squadsbyteamid) | **GET** /{version}/{sport}/squads/teams/{teamId} | By Team ID |
| [**StageById**](SportApi.md#stagebyid) | **GET** /{version}/{sport}/stages/{stageId} | By ID |
| [**StagesAll**](SportApi.md#stagesall) | **GET** /{version}/{sport}/stages | All |
| [**StagesBySeasonId**](SportApi.md#stagesbyseasonid) | **GET** /{version}/{sport}/stages/seasons/{seasonId} | By Season ID |
| [**StagesSearch**](SportApi.md#stagessearch) | **GET** /{version}/{sport}/stages/search/{name} | Search |
| [**StandingCorrectionsBySeasonId**](SportApi.md#standingcorrectionsbyseasonid) | **GET** /{version}/{sport}/standings/corrections/seasons/{seasonId} | Correction by Season ID |
| [**StandingsAll**](SportApi.md#standingsall) | **GET** /{version}/{sport}/standings | All |
| [**StandingsByRoundId**](SportApi.md#standingsbyroundid) | **GET** /{version}/{sport}/standings/rounds/{roundId} | By Round ID |
| [**StandingsBySeasonId**](SportApi.md#standingsbyseasonid) | **GET** /{version}/{sport}/standings/seasons/{seasonId} | By Season ID |
| [**StandingsLiveByLeagueId**](SportApi.md#standingslivebyleagueid) | **GET** /{version}/{sport}/standings/live/leagues/{leagueId} | By League ID |
| [**StateById**](SportApi.md#statebyid) | **GET** /{version}/{sport}/states/{stateId} | By ID |
| [**StatesBySport**](SportApi.md#statesbysport) | **GET** /{version}/{sport}/states | By Sport |
| [**TeamsAll**](SportApi.md#teamsall) | **GET** /{version}/{sport}/teams | All |
| [**TeamsByCountryId**](SportApi.md#teamsbycountryid) | **GET** /{version}/{sport}/teams/countries/{countryId} | By Country ID |
| [**TeamsById**](SportApi.md#teamsbyid) | **GET** /{version}/{sport}/teams/{teamId} | By ID |
| [**TeamsBySeasonId**](SportApi.md#teamsbyseasonid) | **GET** /{version}/{sport}/teams/seasons/{seasonId} | By Season ID |
| [**TeamsSearch**](SportApi.md#teamssearch) | **GET** /{version}/{sport}/teams/search/{name} | Search |
| [**TopScorersBySeasonId**](SportApi.md#topscorersbyseasonid) | **GET** /{version}/{sport}/topscorers/seasons/{seasonId} | By Season ID |
| [**TopScorersByStageId**](SportApi.md#topscorersbystageid) | **GET** /{version}/{sport}/topscorers/stages/{stageId} | By Stage ID |
| [**TranfersByDateRange**](SportApi.md#tranfersbydaterange) | **GET** /{version}/{sport}/transfers/between/{startDate}/{endDate} | By Date Range |
| [**TransferById**](SportApi.md#transferbyid) | **GET** /{version}/{sport}/transfers/{transferId} | By ID |
| [**TransfersAll**](SportApi.md#transfersall) | **GET** /{version}/{sport}/transfers | All |
| [**TransfersByPlayerId**](SportApi.md#transfersbyplayerid) | **GET** /{version}/{sport}/transfers/players/{playerId} | By Player ID |
| [**TransfersByTeamId**](SportApi.md#transfersbyteamid) | **GET** /{version}/{sport}/transfers/teams/{teamId} | By Team ID |
| [**TransfersLatest**](SportApi.md#transferslatest) | **GET** /{version}/{sport}/transfers/latest | Last Updated |
| [**TvStationById**](SportApi.md#tvstationbyid) | **GET** /{version}/{sport}/tv-stations/{tvStationId} | By ID |
| [**TvStationsAll**](SportApi.md#tvstationsall) | **GET** /{version}/{sport}/tv-stations | All |
| [**TvStationsByFixtureId**](SportApi.md#tvstationsbyfixtureid) | **GET** /{version}/{sport}/tv-stations/fixtures/{fixtureId} | By Fixture ID |
| [**VenueById**](SportApi.md#venuebyid) | **GET** /{version}/{sport}/venues/{venueId} | By ID |
| [**VenuesAll**](SportApi.md#venuesall) | **GET** /{version}/{sport}/venues | All |
| [**VenuesBySeasonId**](SportApi.md#venuesbyseasonid) | **GET** /{version}/{sport}/venues/seasons/{seasonId} | By Season ID |
| [**VenuesSearch**](SportApi.md#venuessearch) | **GET** /{version}/{sport}/venues/search/{name} | Search |

<a name="coachbyid"></a>
# **CoachById**
> SportCoachByIdResponse CoachById (string version, string sport, int coachId)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class CoachByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var coachId = 171906;  // int | The ID of the coach you want to retrieve.

            try
            {
                // By ID
                SportCoachByIdResponse result = apiInstance.CoachById(version, sport, coachId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.CoachById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the CoachByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<SportCoachByIdResponse> response = apiInstance.CoachByIdWithHttpInfo(version, sport, coachId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.CoachByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **coachId** | **int** | The ID of the coach you want to retrieve. |  |

### Return type

[**SportCoachByIdResponse**](SportCoachByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="coachesall"></a>
# **CoachesAll**
> SportCoachesAllResponse CoachesAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class CoachesAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportCoachesAllResponse result = apiInstance.CoachesAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.CoachesAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the CoachesAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportCoachesAllResponse> response = apiInstance.CoachesAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.CoachesAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportCoachesAllResponse**](SportCoachesAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="coachesbycountryid"></a>
# **CoachesByCountryId**
> SportCoachesByCountryIdResponse CoachesByCountryId (string version, string sport, int countryId)

By Country ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class CoachesByCountryIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var countryId = 320;  // int | The ID of the country you want to retrieve coaches from.

            try
            {
                // By Country ID
                SportCoachesByCountryIdResponse result = apiInstance.CoachesByCountryId(version, sport, countryId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.CoachesByCountryId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the CoachesByCountryIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Country ID
    ApiResponse<SportCoachesByCountryIdResponse> response = apiInstance.CoachesByCountryIdWithHttpInfo(version, sport, countryId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.CoachesByCountryIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **countryId** | **int** | The ID of the country you want to retrieve coaches from. |  |

### Return type

[**SportCoachesByCountryIdResponse**](SportCoachesByCountryIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="coacheslatest"></a>
# **CoachesLatest**
> SportCoachesLatestResponse CoachesLatest (string version, string sport)

Last updated

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class CoachesLatestExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // Last updated
                SportCoachesLatestResponse result = apiInstance.CoachesLatest(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.CoachesLatest: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the CoachesLatestWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Last updated
    ApiResponse<SportCoachesLatestResponse> response = apiInstance.CoachesLatestWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.CoachesLatestWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportCoachesLatestResponse**](SportCoachesLatestResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="coachessearch"></a>
# **CoachesSearch**
> SportCoachesSearchResponse CoachesSearch (string version, string sport, string name)

Search

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class CoachesSearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var name = John;  // string | The name you want to search on.

            try
            {
                // Search
                SportCoachesSearchResponse result = apiInstance.CoachesSearch(version, sport, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.CoachesSearch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the CoachesSearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<SportCoachesSearchResponse> response = apiInstance.CoachesSearchWithHttpInfo(version, sport, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.CoachesSearchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **name** | **string** | The name you want to search on. |  |

### Return type

[**SportCoachesSearchResponse**](SportCoachesSearchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="commentariesall"></a>
# **CommentariesAll**
> SportCommentariesAllResponse CommentariesAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class CommentariesAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportCommentariesAllResponse result = apiInstance.CommentariesAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.CommentariesAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the CommentariesAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportCommentariesAllResponse> response = apiInstance.CommentariesAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.CommentariesAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportCommentariesAllResponse**](SportCommentariesAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="commentariesbyfixtureid"></a>
# **CommentariesByFixtureId**
> SportCommentariesByFixtureIdResponse CommentariesByFixtureId (string version, string sport, int fixtureId)

By Fixture ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class CommentariesByFixtureIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var fixtureId = 16808591;  // int | The ID of the fixture you want to retrieve commentaries from.

            try
            {
                // By Fixture ID
                SportCommentariesByFixtureIdResponse result = apiInstance.CommentariesByFixtureId(version, sport, fixtureId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.CommentariesByFixtureId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the CommentariesByFixtureIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Fixture ID
    ApiResponse<SportCommentariesByFixtureIdResponse> response = apiInstance.CommentariesByFixtureIdWithHttpInfo(version, sport, fixtureId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.CommentariesByFixtureIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **fixtureId** | **int** | The ID of the fixture you want to retrieve commentaries from. |  |

### Return type

[**SportCommentariesByFixtureIdResponse**](SportCommentariesByFixtureIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="fixturebydaterangeforteam"></a>
# **FixtureByDateRangeForTeam**
> SportFixtureByDateRangeForTeamResponse FixtureByDateRangeForTeam (string version, string sport, string startDate, string endDate, string teamId)

By Date Range for Team

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class FixtureByDateRangeForTeamExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var startDate = maiores;  // string | 
            var endDate = voluptates;  // string | 
            var teamId = ut;  // string | 

            try
            {
                // By Date Range for Team
                SportFixtureByDateRangeForTeamResponse result = apiInstance.FixtureByDateRangeForTeam(version, sport, startDate, endDate, teamId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.FixtureByDateRangeForTeam: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the FixtureByDateRangeForTeamWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Date Range for Team
    ApiResponse<SportFixtureByDateRangeForTeamResponse> response = apiInstance.FixtureByDateRangeForTeamWithHttpInfo(version, sport, startDate, endDate, teamId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.FixtureByDateRangeForTeamWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **startDate** | **string** |  |  |
| **endDate** | **string** |  |  |
| **teamId** | **string** |  |  |

### Return type

[**SportFixtureByDateRangeForTeamResponse**](SportFixtureByDateRangeForTeamResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="fixturebyid"></a>
# **FixtureById**
> SportFixtureByIdResponse FixtureById (string version, string sport, int fixtureId)

Fixture ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class FixtureByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var fixtureId = 18528480;  // int | The ID of the fixture you want to retrieve.

            try
            {
                // Fixture ID
                SportFixtureByIdResponse result = apiInstance.FixtureById(version, sport, fixtureId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.FixtureById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the FixtureByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Fixture ID
    ApiResponse<SportFixtureByIdResponse> response = apiInstance.FixtureByIdWithHttpInfo(version, sport, fixtureId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.FixtureByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **fixtureId** | **int** | The ID of the fixture you want to retrieve. |  |

### Return type

[**SportFixtureByIdResponse**](SportFixtureByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="fixturesall"></a>
# **FixturesAll**
> SportFixturesAllResponse FixturesAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class FixturesAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportFixturesAllResponse result = apiInstance.FixturesAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.FixturesAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the FixturesAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportFixturesAllResponse> response = apiInstance.FixturesAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.FixturesAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportFixturesAllResponse**](SportFixturesAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="fixturesbydate"></a>
# **FixturesByDate**
> SportFixturesByDateResponse FixturesByDate (string version, string sport, string date)

By Date

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class FixturesByDateExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var date = 2022-07-24;  // string | The date you want to retrieve fixtures from.

            try
            {
                // By Date
                SportFixturesByDateResponse result = apiInstance.FixturesByDate(version, sport, date);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.FixturesByDate: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the FixturesByDateWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Date
    ApiResponse<SportFixturesByDateResponse> response = apiInstance.FixturesByDateWithHttpInfo(version, sport, date);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.FixturesByDateWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **date** | **string** | The date you want to retrieve fixtures from. |  |

### Return type

[**SportFixturesByDateResponse**](SportFixturesByDateResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="fixturesbydaterange"></a>
# **FixturesByDateRange**
> SportFixturesByDateRangeResponse FixturesByDateRange (string version, string sport, string startDate, string endDate)

By Date Range

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class FixturesByDateRangeExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var startDate = 2022-07-17;  // string | The start date you want to retrieve fixtures from.
            var endDate = 2022-07-25;  // string | The end date you want to retrieve fixtures from.

            try
            {
                // By Date Range
                SportFixturesByDateRangeResponse result = apiInstance.FixturesByDateRange(version, sport, startDate, endDate);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.FixturesByDateRange: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the FixturesByDateRangeWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Date Range
    ApiResponse<SportFixturesByDateRangeResponse> response = apiInstance.FixturesByDateRangeWithHttpInfo(version, sport, startDate, endDate);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.FixturesByDateRangeWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **startDate** | **string** | The start date you want to retrieve fixtures from. |  |
| **endDate** | **string** | The end date you want to retrieve fixtures from. |  |

### Return type

[**SportFixturesByDateRangeResponse**](SportFixturesByDateRangeResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="fixturesbyids"></a>
# **FixturesByIds**
> SportFixturesByIdsResponse FixturesByIds (string version, string sport, string fixtureIds)

By IDs

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class FixturesByIdsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var fixtureIds = 18528484%2C18531140;  // string | The IDs you want to retrieve.

            try
            {
                // By IDs
                SportFixturesByIdsResponse result = apiInstance.FixturesByIds(version, sport, fixtureIds);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.FixturesByIds: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the FixturesByIdsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By IDs
    ApiResponse<SportFixturesByIdsResponse> response = apiInstance.FixturesByIdsWithHttpInfo(version, sport, fixtureIds);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.FixturesByIdsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **fixtureIds** | **string** | The IDs you want to retrieve. |  |

### Return type

[**SportFixturesByIdsResponse**](SportFixturesByIdsResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="fixturesheadtohead"></a>
# **FixturesHeadToHead**
> SportFixturesHeadToHeadResponse FixturesHeadToHead (string version, string sport, int firstTeam, int secondTeam)

Head to Head

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class FixturesHeadToHeadExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var firstTeam = 2650;  // int | The ID of the first team retrieve fixtures from.
            var secondTeam = 86;  // int | The ID of the second team retrieve fixtures from.

            try
            {
                // Head to Head
                SportFixturesHeadToHeadResponse result = apiInstance.FixturesHeadToHead(version, sport, firstTeam, secondTeam);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.FixturesHeadToHead: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the FixturesHeadToHeadWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Head to Head
    ApiResponse<SportFixturesHeadToHeadResponse> response = apiInstance.FixturesHeadToHeadWithHttpInfo(version, sport, firstTeam, secondTeam);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.FixturesHeadToHeadWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **firstTeam** | **int** | The ID of the first team retrieve fixtures from. |  |
| **secondTeam** | **int** | The ID of the second team retrieve fixtures from. |  |

### Return type

[**SportFixturesHeadToHeadResponse**](SportFixturesHeadToHeadResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="fixtureslatest"></a>
# **FixturesLatest**
> string FixturesLatest (string version, string sport)

Last Updated

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class FixturesLatestExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // Last Updated
                string result = apiInstance.FixturesLatest(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.FixturesLatest: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the FixturesLatestWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Last Updated
    ApiResponse<string> response = apiInstance.FixturesLatestWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.FixturesLatestWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

**string**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="fixturessearch"></a>
# **FixturesSearch**
> SportFixturesSearchResponse FixturesSearch (string version, string sport, string name)

Search

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class FixturesSearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var name = havn;  // string | The name you want search on.

            try
            {
                // Search
                SportFixturesSearchResponse result = apiInstance.FixturesSearch(version, sport, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.FixturesSearch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the FixturesSearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<SportFixturesSearchResponse> response = apiInstance.FixturesSearchWithHttpInfo(version, sport, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.FixturesSearchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **name** | **string** | The name you want search on. |  |

### Return type

[**SportFixturesSearchResponse**](SportFixturesSearchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="leaguebyid"></a>
# **LeagueById**
> SportLeagueByIdResponse LeagueById (string version, string sport, int leagueId)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LeagueByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var leagueId = 271;  // int | The ID of the league you want to retrieve.

            try
            {
                // By ID
                SportLeagueByIdResponse result = apiInstance.LeagueById(version, sport, leagueId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LeagueById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LeagueByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<SportLeagueByIdResponse> response = apiInstance.LeagueByIdWithHttpInfo(version, sport, leagueId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LeagueByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **leagueId** | **int** | The ID of the league you want to retrieve. |  |

### Return type

[**SportLeagueByIdResponse**](SportLeagueByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="leagueenrichments"></a>
# **LeagueEnrichments**
> Object LeagueEnrichments (string version, string sport, int leagueId)

Enrichments

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LeagueEnrichmentsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var leagueId = 271;  // int | The ID of the league you want to retrieve enrichments from.

            try
            {
                // Enrichments
                Object result = apiInstance.LeagueEnrichments(version, sport, leagueId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LeagueEnrichments: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LeagueEnrichmentsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Enrichments
    ApiResponse<Object> response = apiInstance.LeagueEnrichmentsWithHttpInfo(version, sport, leagueId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LeagueEnrichmentsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **leagueId** | **int** | The ID of the league you want to retrieve enrichments from. |  |

### Return type

**Object**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="leagueshirts"></a>
# **LeagueShirts**
> Object LeagueShirts (string version, string sport, int leagueId)

Shirts By League ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LeagueShirtsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var leagueId = 271;  // int | The ID of the league you want to retrieve.

            try
            {
                // Shirts By League ID
                Object result = apiInstance.LeagueShirts(version, sport, leagueId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LeagueShirts: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LeagueShirtsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Shirts By League ID
    ApiResponse<Object> response = apiInstance.LeagueShirtsWithHttpInfo(version, sport, leagueId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LeagueShirtsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **leagueId** | **int** | The ID of the league you want to retrieve. |  |

### Return type

**Object**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="leaguesall"></a>
# **LeaguesAll**
> SportLeaguesAllResponse LeaguesAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LeaguesAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportLeaguesAllResponse result = apiInstance.LeaguesAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LeaguesAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LeaguesAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportLeaguesAllResponse> response = apiInstance.LeaguesAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LeaguesAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportLeaguesAllResponse**](SportLeaguesAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="leaguesbycountryid"></a>
# **LeaguesByCountryId**
> SportLeaguesByCountryIdResponse LeaguesByCountryId (string version, string sport, int countryId)

By Country ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LeaguesByCountryIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var countryId = 320;  // int | The ID of the country you want to retrieve leagues from.

            try
            {
                // By Country ID
                SportLeaguesByCountryIdResponse result = apiInstance.LeaguesByCountryId(version, sport, countryId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LeaguesByCountryId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LeaguesByCountryIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Country ID
    ApiResponse<SportLeaguesByCountryIdResponse> response = apiInstance.LeaguesByCountryIdWithHttpInfo(version, sport, countryId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LeaguesByCountryIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **countryId** | **int** | The ID of the country you want to retrieve leagues from. |  |

### Return type

[**SportLeaguesByCountryIdResponse**](SportLeaguesByCountryIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="leaguesbydate"></a>
# **LeaguesByDate**
> SportLeaguesByDateResponse LeaguesByDate (string version, string sport, string date)

By Date

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LeaguesByDateExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var date = 2022-07-15;  // string | The date of fixtures you want to retrieve leagues from.

            try
            {
                // By Date
                SportLeaguesByDateResponse result = apiInstance.LeaguesByDate(version, sport, date);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LeaguesByDate: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LeaguesByDateWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Date
    ApiResponse<SportLeaguesByDateResponse> response = apiInstance.LeaguesByDateWithHttpInfo(version, sport, date);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LeaguesByDateWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **date** | **string** | The date of fixtures you want to retrieve leagues from. |  |

### Return type

[**SportLeaguesByDateResponse**](SportLeaguesByDateResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="leaguesbyteamid"></a>
# **LeaguesByTeamId**
> Object LeaguesByTeamId (string version, string sport, int teamId)

Leagues By Team ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LeaguesByTeamIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var teamId = 180;  // int | The ID of the team you want to retrieve leagues from.

            try
            {
                // Leagues By Team ID
                Object result = apiInstance.LeaguesByTeamId(version, sport, teamId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LeaguesByTeamId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LeaguesByTeamIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Leagues By Team ID
    ApiResponse<Object> response = apiInstance.LeaguesByTeamIdWithHttpInfo(version, sport, teamId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LeaguesByTeamIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **teamId** | **int** | The ID of the team you want to retrieve leagues from. |  |

### Return type

**Object**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="leaguescurrentbyteamid"></a>
# **LeaguesCurrentByTeamId**
> Object LeaguesCurrentByTeamId (string version, string sport, int teamId)

Current Leagues By Team ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LeaguesCurrentByTeamIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var teamId = 180;  // int | The ID of the team you want to retrieve current leagues from.

            try
            {
                // Current Leagues By Team ID
                Object result = apiInstance.LeaguesCurrentByTeamId(version, sport, teamId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LeaguesCurrentByTeamId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LeaguesCurrentByTeamIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Current Leagues By Team ID
    ApiResponse<Object> response = apiInstance.LeaguesCurrentByTeamIdWithHttpInfo(version, sport, teamId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LeaguesCurrentByTeamIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **teamId** | **int** | The ID of the team you want to retrieve current leagues from. |  |

### Return type

**Object**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="leagueslive"></a>
# **LeaguesLive**
> SportLeaguesLiveResponse LeaguesLive (string version, string sport)

Live

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LeaguesLiveExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // Live
                SportLeaguesLiveResponse result = apiInstance.LeaguesLive(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LeaguesLive: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LeaguesLiveWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Live
    ApiResponse<SportLeaguesLiveResponse> response = apiInstance.LeaguesLiveWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LeaguesLiveWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportLeaguesLiveResponse**](SportLeaguesLiveResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="leaguessearch"></a>
# **LeaguesSearch**
> SportLeaguesSearchResponse LeaguesSearch (string version, string sport, string name)

Search

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LeaguesSearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var name = Super;  // string | The name you want to search on.

            try
            {
                // Search
                SportLeaguesSearchResponse result = apiInstance.LeaguesSearch(version, sport, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LeaguesSearch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LeaguesSearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<SportLeaguesSearchResponse> response = apiInstance.LeaguesSearchWithHttpInfo(version, sport, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LeaguesSearchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **name** | **string** | The name you want to search on. |  |

### Return type

[**SportLeaguesSearchResponse**](SportLeaguesSearchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="livescoresall"></a>
# **LivescoresAll**
> SportLivescoresAllResponse LivescoresAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LivescoresAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportLivescoresAllResponse result = apiInstance.LivescoresAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LivescoresAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LivescoresAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportLivescoresAllResponse> response = apiInstance.LivescoresAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LivescoresAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportLivescoresAllResponse**](SportLivescoresAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="livescoresallinplay"></a>
# **LivescoresAllInPlay**
> SportLivescoresAllInPlayResponse LivescoresAllInPlay (string version, string sport)

All In-play

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LivescoresAllInPlayExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All In-play
                SportLivescoresAllInPlayResponse result = apiInstance.LivescoresAllInPlay(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LivescoresAllInPlay: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LivescoresAllInPlayWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All In-play
    ApiResponse<SportLivescoresAllInPlayResponse> response = apiInstance.LivescoresAllInPlayWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LivescoresAllInPlayWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportLivescoresAllInPlayResponse**](SportLivescoresAllInPlayResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="livescoreslatest"></a>
# **LivescoresLatest**
> SportLivescoresLatestResponse LivescoresLatest (string version, string sport)

Last Updated In-play

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class LivescoresLatestExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // Last Updated In-play
                SportLivescoresLatestResponse result = apiInstance.LivescoresLatest(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.LivescoresLatest: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the LivescoresLatestWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Last Updated In-play
    ApiResponse<SportLivescoresLatestResponse> response = apiInstance.LivescoresLatestWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.LivescoresLatestWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportLivescoresLatestResponse**](SportLivescoresLatestResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="newsallpostmatch"></a>
# **NewsAllPostMatch**
> string NewsAllPostMatch (string version, string sport)

All Post Match

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class NewsAllPostMatchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All Post Match
                string result = apiInstance.NewsAllPostMatch(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.NewsAllPostMatch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the NewsAllPostMatchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All Post Match
    ApiResponse<string> response = apiInstance.NewsAllPostMatchWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.NewsAllPostMatchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

**string**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="newsallprematch"></a>
# **NewsAllPreMatch**
> SportNewsAllPreMatchResponse NewsAllPreMatch (string version, string sport)

All Pre-match

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class NewsAllPreMatchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All Pre-match
                SportNewsAllPreMatchResponse result = apiInstance.NewsAllPreMatch(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.NewsAllPreMatch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the NewsAllPreMatchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All Pre-match
    ApiResponse<SportNewsAllPreMatchResponse> response = apiInstance.NewsAllPreMatchWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.NewsAllPreMatchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportNewsAllPreMatchResponse**](SportNewsAllPreMatchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="newspostmatchbyseasonid"></a>
# **NewsPostMatchBySeasonId**
> string NewsPostMatchBySeasonId (string version, string sport, int seasonId)

Post Match by Season ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class NewsPostMatchBySeasonIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | The ID of the season you want to retrieve post-match news from.

            try
            {
                // Post Match by Season ID
                string result = apiInstance.NewsPostMatchBySeasonId(version, sport, seasonId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.NewsPostMatchBySeasonId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the NewsPostMatchBySeasonIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Post Match by Season ID
    ApiResponse<string> response = apiInstance.NewsPostMatchBySeasonIdWithHttpInfo(version, sport, seasonId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.NewsPostMatchBySeasonIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve post-match news from. |  |

### Return type

**string**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="newsprematchbyseasonid"></a>
# **NewsPreMatchBySeasonId**
> SportNewsPreMatchBySeasonIdResponse NewsPreMatchBySeasonId (string version, string sport, int seasonId)

Pre-match By Season ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class NewsPreMatchBySeasonIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19734;  // int | The ID of the season you want to retrieve post-match news from.

            try
            {
                // Pre-match By Season ID
                SportNewsPreMatchBySeasonIdResponse result = apiInstance.NewsPreMatchBySeasonId(version, sport, seasonId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.NewsPreMatchBySeasonId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the NewsPreMatchBySeasonIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Pre-match By Season ID
    ApiResponse<SportNewsPreMatchBySeasonIdResponse> response = apiInstance.NewsPreMatchBySeasonIdWithHttpInfo(version, sport, seasonId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.NewsPreMatchBySeasonIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve post-match news from. |  |

### Return type

[**SportNewsPreMatchBySeasonIdResponse**](SportNewsPreMatchBySeasonIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="newsupcomingpostmatch"></a>
# **NewsUpcomingPostMatch**
> string NewsUpcomingPostMatch (string version, string sport)

Upcoming Post Match

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class NewsUpcomingPostMatchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // Upcoming Post Match
                string result = apiInstance.NewsUpcomingPostMatch(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.NewsUpcomingPostMatch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the NewsUpcomingPostMatchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Upcoming Post Match
    ApiResponse<string> response = apiInstance.NewsUpcomingPostMatchWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.NewsUpcomingPostMatchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

**string**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="newsupcomingprematch"></a>
# **NewsUpcomingPreMatch**
> SportNewsUpcomingPreMatchResponse NewsUpcomingPreMatch (string version, string sport)

Upcoming Pre-match

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class NewsUpcomingPreMatchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // Upcoming Pre-match
                SportNewsUpcomingPreMatchResponse result = apiInstance.NewsUpcomingPreMatch(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.NewsUpcomingPreMatch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the NewsUpcomingPreMatchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Upcoming Pre-match
    ApiResponse<SportNewsUpcomingPreMatchResponse> response = apiInstance.NewsUpcomingPreMatchWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.NewsUpcomingPreMatchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportNewsUpcomingPreMatchResponse**](SportNewsUpcomingPreMatchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="oddsallinplay"></a>
# **OddsAllInPlay**
> SportOddsAllInPlayResponse OddsAllInPlay (string version, string sport)

All In-play

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class OddsAllInPlayExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All In-play
                SportOddsAllInPlayResponse result = apiInstance.OddsAllInPlay(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.OddsAllInPlay: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the OddsAllInPlayWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All In-play
    ApiResponse<SportOddsAllInPlayResponse> response = apiInstance.OddsAllInPlayWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.OddsAllInPlayWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportOddsAllInPlayResponse**](SportOddsAllInPlayResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="oddsallprematch"></a>
# **OddsAllPreMatch**
> SportOddsAllPreMatchResponse OddsAllPreMatch (string version, string sport)

All Pre-match

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class OddsAllPreMatchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All Pre-match
                SportOddsAllPreMatchResponse result = apiInstance.OddsAllPreMatch(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.OddsAllPreMatch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the OddsAllPreMatchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All Pre-match
    ApiResponse<SportOddsAllPreMatchResponse> response = apiInstance.OddsAllPreMatchWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.OddsAllPreMatchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportOddsAllPreMatchResponse**](SportOddsAllPreMatchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="oddsinplaybyfixtureandbookmakerid"></a>
# **OddsInPlayByFixtureAndBookmakerId**
> Object OddsInPlayByFixtureAndBookmakerId (string version, string sport, int fixtureId, int bookmakerId)

In-play by Fixture and Bookmaker ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class OddsInPlayByFixtureAndBookmakerIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var fixtureId = 18535046;  // int | The ID of the fixture you want to retrieve in-play odds from.
            var bookmakerId = 6;  // int | The ID of the bookmaker you want to retrieve in-play odds from.

            try
            {
                // In-play by Fixture and Bookmaker ID
                Object result = apiInstance.OddsInPlayByFixtureAndBookmakerId(version, sport, fixtureId, bookmakerId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.OddsInPlayByFixtureAndBookmakerId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the OddsInPlayByFixtureAndBookmakerIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // In-play by Fixture and Bookmaker ID
    ApiResponse<Object> response = apiInstance.OddsInPlayByFixtureAndBookmakerIdWithHttpInfo(version, sport, fixtureId, bookmakerId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.OddsInPlayByFixtureAndBookmakerIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **fixtureId** | **int** | The ID of the fixture you want to retrieve in-play odds from. |  |
| **bookmakerId** | **int** | The ID of the bookmaker you want to retrieve in-play odds from. |  |

### Return type

**Object**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="oddsinplaybyfixtureandmarketid"></a>
# **OddsInPlayByFixtureAndMarketId**
> Object OddsInPlayByFixtureAndMarketId (string version, string sport, int fixtureId, int marketId)

In-play by Fixture and Market ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class OddsInPlayByFixtureAndMarketIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var fixtureId = 233366;  // int | The ID of the fixture you want to retrieve in-play odds from.
            var marketId = 56;  // int | The ID of the market you want to retrieve in-play odds from.

            try
            {
                // In-play by Fixture and Market ID
                Object result = apiInstance.OddsInPlayByFixtureAndMarketId(version, sport, fixtureId, marketId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.OddsInPlayByFixtureAndMarketId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the OddsInPlayByFixtureAndMarketIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // In-play by Fixture and Market ID
    ApiResponse<Object> response = apiInstance.OddsInPlayByFixtureAndMarketIdWithHttpInfo(version, sport, fixtureId, marketId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.OddsInPlayByFixtureAndMarketIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **fixtureId** | **int** | The ID of the fixture you want to retrieve in-play odds from. |  |
| **marketId** | **int** | The ID of the market you want to retrieve in-play odds from. |  |

### Return type

**Object**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="oddsinplaybyfixtureid"></a>
# **OddsInPlayByFixtureId**
> SportOddsInPlayByFixtureIdResponse OddsInPlayByFixtureId (string version, string sport, int fixtureId)

In-play by Fixture ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class OddsInPlayByFixtureIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var fixtureId = 18535046;  // int | The ID of the fixture you want to retrieve in-play odds from.

            try
            {
                // In-play by Fixture ID
                SportOddsInPlayByFixtureIdResponse result = apiInstance.OddsInPlayByFixtureId(version, sport, fixtureId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.OddsInPlayByFixtureId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the OddsInPlayByFixtureIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // In-play by Fixture ID
    ApiResponse<SportOddsInPlayByFixtureIdResponse> response = apiInstance.OddsInPlayByFixtureIdWithHttpInfo(version, sport, fixtureId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.OddsInPlayByFixtureIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **fixtureId** | **int** | The ID of the fixture you want to retrieve in-play odds from. |  |

### Return type

[**SportOddsInPlayByFixtureIdResponse**](SportOddsInPlayByFixtureIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="oddslatestinplay"></a>
# **OddsLatestInPlay**
> Object OddsLatestInPlay (string version, string sport)

Latest In-play

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class OddsLatestInPlayExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // Latest In-play
                Object result = apiInstance.OddsLatestInPlay(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.OddsLatestInPlay: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the OddsLatestInPlayWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Latest In-play
    ApiResponse<Object> response = apiInstance.OddsLatestInPlayWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.OddsLatestInPlayWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

**Object**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="oddslatestprematch"></a>
# **OddsLatestPreMatch**
> Object OddsLatestPreMatch (string version, string sport)

Last Updated Pre-match

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class OddsLatestPreMatchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // Last Updated Pre-match
                Object result = apiInstance.OddsLatestPreMatch(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.OddsLatestPreMatch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the OddsLatestPreMatchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Last Updated Pre-match
    ApiResponse<Object> response = apiInstance.OddsLatestPreMatchWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.OddsLatestPreMatchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

**Object**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="oddsprematchbyfixtureandbookmakerid"></a>
# **OddsPreMatchByFixtureAndBookmakerId**
> SportOddsPreMatchByFixtureAndBookmakerIdResponse OddsPreMatchByFixtureAndBookmakerId (string version, string sport, int fixtureId, int bookmakerId)

Pre-match by Fixture and Bookmaker ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class OddsPreMatchByFixtureAndBookmakerIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var fixtureId = 233366;  // int | The ID of the fixture you want to retrieve pre-match odds from.
            var bookmakerId = 6;  // int | The ID of the bookmaker you want to retrieve pre-match odds from.

            try
            {
                // Pre-match by Fixture and Bookmaker ID
                SportOddsPreMatchByFixtureAndBookmakerIdResponse result = apiInstance.OddsPreMatchByFixtureAndBookmakerId(version, sport, fixtureId, bookmakerId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.OddsPreMatchByFixtureAndBookmakerId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the OddsPreMatchByFixtureAndBookmakerIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Pre-match by Fixture and Bookmaker ID
    ApiResponse<SportOddsPreMatchByFixtureAndBookmakerIdResponse> response = apiInstance.OddsPreMatchByFixtureAndBookmakerIdWithHttpInfo(version, sport, fixtureId, bookmakerId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.OddsPreMatchByFixtureAndBookmakerIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **fixtureId** | **int** | The ID of the fixture you want to retrieve pre-match odds from. |  |
| **bookmakerId** | **int** | The ID of the bookmaker you want to retrieve pre-match odds from. |  |

### Return type

[**SportOddsPreMatchByFixtureAndBookmakerIdResponse**](SportOddsPreMatchByFixtureAndBookmakerIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="oddsprematchbyfixtureandmarketid"></a>
# **OddsPreMatchByFixtureAndMarketId**
> SportOddsPreMatchByFixtureAndMarketIdResponse OddsPreMatchByFixtureAndMarketId (string version, string sport, int fixtureId, int marketId)

Pre-match by Fixture and Market ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class OddsPreMatchByFixtureAndMarketIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var fixtureId = 233366;  // int | The ID of the fixture you want to retrieve pre-match odds from.
            var marketId = 56;  // int | The ID of the market you want to retrieve pre-match odds from.

            try
            {
                // Pre-match by Fixture and Market ID
                SportOddsPreMatchByFixtureAndMarketIdResponse result = apiInstance.OddsPreMatchByFixtureAndMarketId(version, sport, fixtureId, marketId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.OddsPreMatchByFixtureAndMarketId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the OddsPreMatchByFixtureAndMarketIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Pre-match by Fixture and Market ID
    ApiResponse<SportOddsPreMatchByFixtureAndMarketIdResponse> response = apiInstance.OddsPreMatchByFixtureAndMarketIdWithHttpInfo(version, sport, fixtureId, marketId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.OddsPreMatchByFixtureAndMarketIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **fixtureId** | **int** | The ID of the fixture you want to retrieve pre-match odds from. |  |
| **marketId** | **int** | The ID of the market you want to retrieve pre-match odds from. |  |

### Return type

[**SportOddsPreMatchByFixtureAndMarketIdResponse**](SportOddsPreMatchByFixtureAndMarketIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="oddsprematchbyfixtureid"></a>
# **OddsPreMatchByFixtureId**
> SportOddsPreMatchByFixtureIdResponse OddsPreMatchByFixtureId (string version, string sport, int fixtureId)

Pre-match by Fixture ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class OddsPreMatchByFixtureIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var fixtureId = 233366;  // int | The ID of the fixture you want to retrieve pre-match odds from.

            try
            {
                // Pre-match by Fixture ID
                SportOddsPreMatchByFixtureIdResponse result = apiInstance.OddsPreMatchByFixtureId(version, sport, fixtureId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.OddsPreMatchByFixtureId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the OddsPreMatchByFixtureIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Pre-match by Fixture ID
    ApiResponse<SportOddsPreMatchByFixtureIdResponse> response = apiInstance.OddsPreMatchByFixtureIdWithHttpInfo(version, sport, fixtureId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.OddsPreMatchByFixtureIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **fixtureId** | **int** | The ID of the fixture you want to retrieve pre-match odds from. |  |

### Return type

[**SportOddsPreMatchByFixtureIdResponse**](SportOddsPreMatchByFixtureIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="playerbyid"></a>
# **PlayerById**
> SportPlayerByIdResponse PlayerById (string version, string sport, int playerId)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class PlayerByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var playerId = 14;  // int | The ID of the player you want to retrieve.

            try
            {
                // By ID
                SportPlayerByIdResponse result = apiInstance.PlayerById(version, sport, playerId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.PlayerById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the PlayerByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<SportPlayerByIdResponse> response = apiInstance.PlayerByIdWithHttpInfo(version, sport, playerId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.PlayerByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **playerId** | **int** | The ID of the player you want to retrieve. |  |

### Return type

[**SportPlayerByIdResponse**](SportPlayerByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="playersall"></a>
# **PlayersAll**
> SportPlayersAllResponse PlayersAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class PlayersAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportPlayersAllResponse result = apiInstance.PlayersAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.PlayersAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the PlayersAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportPlayersAllResponse> response = apiInstance.PlayersAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.PlayersAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportPlayersAllResponse**](SportPlayersAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="playersbycountryid"></a>
# **PlayersByCountryId**
> SportPlayersByCountryIdResponse PlayersByCountryId (string version, string sport, int countryId)

By Country ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class PlayersByCountryIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var countryId = 320;  // int | The ID of the country you want to retrieve players from.

            try
            {
                // By Country ID
                SportPlayersByCountryIdResponse result = apiInstance.PlayersByCountryId(version, sport, countryId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.PlayersByCountryId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the PlayersByCountryIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Country ID
    ApiResponse<SportPlayersByCountryIdResponse> response = apiInstance.PlayersByCountryIdWithHttpInfo(version, sport, countryId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.PlayersByCountryIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **countryId** | **int** | The ID of the country you want to retrieve players from. |  |

### Return type

[**SportPlayersByCountryIdResponse**](SportPlayersByCountryIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="playerslatest"></a>
# **PlayersLatest**
> SportPlayersLatestResponse PlayersLatest (string version, string sport)

Latest Updated

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class PlayersLatestExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // Latest Updated
                SportPlayersLatestResponse result = apiInstance.PlayersLatest(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.PlayersLatest: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the PlayersLatestWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Latest Updated
    ApiResponse<SportPlayersLatestResponse> response = apiInstance.PlayersLatestWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.PlayersLatestWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportPlayersLatestResponse**](SportPlayersLatestResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="playerssearch"></a>
# **PlayersSearch**
> SportPlayersSearchResponse PlayersSearch (string version, string sport, string name)

Search

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class PlayersSearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var name = Agg;  // string | The name you want to search on.

            try
            {
                // Search
                SportPlayersSearchResponse result = apiInstance.PlayersSearch(version, sport, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.PlayersSearch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the PlayersSearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<SportPlayersSearchResponse> response = apiInstance.PlayersSearchWithHttpInfo(version, sport, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.PlayersSearchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **name** | **string** | The name you want to search on. |  |

### Return type

[**SportPlayersSearchResponse**](SportPlayersSearchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="predictionsall"></a>
# **PredictionsAll**
> SportPredictionsAllResponse PredictionsAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class PredictionsAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportPredictionsAllResponse result = apiInstance.PredictionsAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.PredictionsAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the PredictionsAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportPredictionsAllResponse> response = apiInstance.PredictionsAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.PredictionsAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportPredictionsAllResponse**](SportPredictionsAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="predictionsallvaluebets"></a>
# **PredictionsAllValueBets**
> SportPredictionsAllValueBetsResponse PredictionsAllValueBets (string version, string sport)

All Value Bets

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class PredictionsAllValueBetsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All Value Bets
                SportPredictionsAllValueBetsResponse result = apiInstance.PredictionsAllValueBets(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.PredictionsAllValueBets: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the PredictionsAllValueBetsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All Value Bets
    ApiResponse<SportPredictionsAllValueBetsResponse> response = apiInstance.PredictionsAllValueBetsWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.PredictionsAllValueBetsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportPredictionsAllValueBetsResponse**](SportPredictionsAllValueBetsResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="predictionsbyfixtureid"></a>
# **PredictionsByFixtureId**
> SportPredictionsByFixtureIdResponse PredictionsByFixtureId (string version, string sport, int fixtureId)

By Fixture ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class PredictionsByFixtureIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var fixtureId = 16774022;  // int | The ID of the fixture you want to retrieve predictions from.

            try
            {
                // By Fixture ID
                SportPredictionsByFixtureIdResponse result = apiInstance.PredictionsByFixtureId(version, sport, fixtureId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.PredictionsByFixtureId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the PredictionsByFixtureIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Fixture ID
    ApiResponse<SportPredictionsByFixtureIdResponse> response = apiInstance.PredictionsByFixtureIdWithHttpInfo(version, sport, fixtureId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.PredictionsByFixtureIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **fixtureId** | **int** | The ID of the fixture you want to retrieve predictions from. |  |

### Return type

[**SportPredictionsByFixtureIdResponse**](SportPredictionsByFixtureIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="predictionsvaluebetsbyfixtureid"></a>
# **PredictionsValueBetsByFixtureId**
> Object PredictionsValueBetsByFixtureId (string version, string sport, int fixtureId)

Value Bets by Fixture ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class PredictionsValueBetsByFixtureIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var fixtureId = 18535050;  // int | The ID of the fixture you want to retrieve value bets from.

            try
            {
                // Value Bets by Fixture ID
                Object result = apiInstance.PredictionsValueBetsByFixtureId(version, sport, fixtureId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.PredictionsValueBetsByFixtureId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the PredictionsValueBetsByFixtureIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Value Bets by Fixture ID
    ApiResponse<Object> response = apiInstance.PredictionsValueBetsByFixtureIdWithHttpInfo(version, sport, fixtureId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.PredictionsValueBetsByFixtureIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **fixtureId** | **int** | The ID of the fixture you want to retrieve value bets from. |  |

### Return type

**Object**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="refereebyid"></a>
# **RefereeById**
> SportRefereeByIdResponse RefereeById (string version, string sport, int refereeId)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class RefereeByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var refereeId = 11698;  // int | The ID of the referee you want to retrieve.

            try
            {
                // By ID
                SportRefereeByIdResponse result = apiInstance.RefereeById(version, sport, refereeId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.RefereeById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the RefereeByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<SportRefereeByIdResponse> response = apiInstance.RefereeByIdWithHttpInfo(version, sport, refereeId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.RefereeByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **refereeId** | **int** | The ID of the referee you want to retrieve. |  |

### Return type

[**SportRefereeByIdResponse**](SportRefereeByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="refereesall"></a>
# **RefereesAll**
> SportRefereesAllResponse RefereesAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class RefereesAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportRefereesAllResponse result = apiInstance.RefereesAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.RefereesAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the RefereesAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportRefereesAllResponse> response = apiInstance.RefereesAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.RefereesAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportRefereesAllResponse**](SportRefereesAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="refereesbycountryid"></a>
# **RefereesByCountryId**
> SportRefereesByCountryIdResponse RefereesByCountryId (string version, string sport, int countryId)

By Country ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class RefereesByCountryIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var countryId = 320;  // int | The ID of the country you want to retrieve referees from.

            try
            {
                // By Country ID
                SportRefereesByCountryIdResponse result = apiInstance.RefereesByCountryId(version, sport, countryId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.RefereesByCountryId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the RefereesByCountryIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Country ID
    ApiResponse<SportRefereesByCountryIdResponse> response = apiInstance.RefereesByCountryIdWithHttpInfo(version, sport, countryId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.RefereesByCountryIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **countryId** | **int** | The ID of the country you want to retrieve referees from. |  |

### Return type

[**SportRefereesByCountryIdResponse**](SportRefereesByCountryIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="refereesbyseasonid"></a>
# **RefereesBySeasonId**
> SportRefereesBySeasonIdResponse RefereesBySeasonId (string version, string sport, int seasonId)

By Season ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class RefereesBySeasonIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | The ID of the season you want to retrieve referees from.

            try
            {
                // By Season ID
                SportRefereesBySeasonIdResponse result = apiInstance.RefereesBySeasonId(version, sport, seasonId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.RefereesBySeasonId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the RefereesBySeasonIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Season ID
    ApiResponse<SportRefereesBySeasonIdResponse> response = apiInstance.RefereesBySeasonIdWithHttpInfo(version, sport, seasonId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.RefereesBySeasonIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve referees from. |  |

### Return type

[**SportRefereesBySeasonIdResponse**](SportRefereesBySeasonIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="refereessearch"></a>
# **RefereesSearch**
> SportRefereesSearchResponse RefereesSearch (string version, string sport, string name)

Search

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class RefereesSearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var name = Munch;  // string | The name you want to search on.

            try
            {
                // Search
                SportRefereesSearchResponse result = apiInstance.RefereesSearch(version, sport, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.RefereesSearch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the RefereesSearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<SportRefereesSearchResponse> response = apiInstance.RefereesSearchWithHttpInfo(version, sport, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.RefereesSearchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **name** | **string** | The name you want to search on. |  |

### Return type

[**SportRefereesSearchResponse**](SportRefereesSearchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="rivalsall"></a>
# **RivalsAll**
> SportRivalsAllResponse RivalsAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class RivalsAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportRivalsAllResponse result = apiInstance.RivalsAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.RivalsAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the RivalsAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportRivalsAllResponse> response = apiInstance.RivalsAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.RivalsAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportRivalsAllResponse**](SportRivalsAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="rivalsbyteamid"></a>
# **RivalsByTeamId**
> SportRivalsByTeamIdResponse RivalsByTeamId (string version, string sport, int teamId)

By Team ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class RivalsByTeamIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var teamId = 53;  // int | The ID of the team you want to retrieve rivals from.

            try
            {
                // By Team ID
                SportRivalsByTeamIdResponse result = apiInstance.RivalsByTeamId(version, sport, teamId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.RivalsByTeamId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the RivalsByTeamIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Team ID
    ApiResponse<SportRivalsByTeamIdResponse> response = apiInstance.RivalsByTeamIdWithHttpInfo(version, sport, teamId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.RivalsByTeamIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **teamId** | **int** | The ID of the team you want to retrieve rivals from. |  |

### Return type

[**SportRivalsByTeamIdResponse**](SportRivalsByTeamIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="roundbyid"></a>
# **RoundById**
> SportRoundByIdResponse RoundById (string version, string sport, int roundId)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class RoundByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var roundId = 23317;  // int | The ID of the round you want to retrieve.

            try
            {
                // By ID
                SportRoundByIdResponse result = apiInstance.RoundById(version, sport, roundId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.RoundById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the RoundByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<SportRoundByIdResponse> response = apiInstance.RoundByIdWithHttpInfo(version, sport, roundId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.RoundByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **roundId** | **int** | The ID of the round you want to retrieve. |  |

### Return type

[**SportRoundByIdResponse**](SportRoundByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="roundsall"></a>
# **RoundsAll**
> SportRoundsAllResponse RoundsAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class RoundsAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportRoundsAllResponse result = apiInstance.RoundsAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.RoundsAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the RoundsAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportRoundsAllResponse> response = apiInstance.RoundsAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.RoundsAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportRoundsAllResponse**](SportRoundsAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="roundsbyseasonid"></a>
# **RoundsBySeasonId**
> SportRoundsBySeasonIdResponse RoundsBySeasonId (string version, string sport, int seasonId)

Season ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class RoundsBySeasonIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | The ID of the season you want to retrieve rounds from.

            try
            {
                // Season ID
                SportRoundsBySeasonIdResponse result = apiInstance.RoundsBySeasonId(version, sport, seasonId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.RoundsBySeasonId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the RoundsBySeasonIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Season ID
    ApiResponse<SportRoundsBySeasonIdResponse> response = apiInstance.RoundsBySeasonIdWithHttpInfo(version, sport, seasonId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.RoundsBySeasonIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve rounds from. |  |

### Return type

[**SportRoundsBySeasonIdResponse**](SportRoundsBySeasonIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="roundssearch"></a>
# **RoundsSearch**
> SportRoundsSearchResponse RoundsSearch (string version, string sport, int name)

Search

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class RoundsSearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var name = 2;  // int | The name you want to search on.

            try
            {
                // Search
                SportRoundsSearchResponse result = apiInstance.RoundsSearch(version, sport, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.RoundsSearch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the RoundsSearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<SportRoundsSearchResponse> response = apiInstance.RoundsSearchWithHttpInfo(version, sport, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.RoundsSearchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **name** | **int** | The name you want to search on. |  |

### Return type

[**SportRoundsSearchResponse**](SportRoundsSearchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="schedulesbyseasonid"></a>
# **SchedulesBySeasonId**
> SportSchedulesBySeasonIdResponse SchedulesBySeasonId (string version, string sport, int seasonId)

By Season ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class SchedulesBySeasonIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | 

            try
            {
                // By Season ID
                SportSchedulesBySeasonIdResponse result = apiInstance.SchedulesBySeasonId(version, sport, seasonId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.SchedulesBySeasonId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the SchedulesBySeasonIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Season ID
    ApiResponse<SportSchedulesBySeasonIdResponse> response = apiInstance.SchedulesBySeasonIdWithHttpInfo(version, sport, seasonId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.SchedulesBySeasonIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** |  |  |

### Return type

[**SportSchedulesBySeasonIdResponse**](SportSchedulesBySeasonIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="schedulesbyteamandseasonid"></a>
# **SchedulesByTeamAndSeasonId**
> SportSchedulesByTeamAndSeasonIdResponse SchedulesByTeamAndSeasonId (string version, string sport, int seasonId, int teamId)

By Team and Season ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class SchedulesByTeamAndSeasonIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | The ID of the season you want to retrieve schedule from.
            var teamId = 282;  // int | The ID of the team you want to retrieve schedule from.

            try
            {
                // By Team and Season ID
                SportSchedulesByTeamAndSeasonIdResponse result = apiInstance.SchedulesByTeamAndSeasonId(version, sport, seasonId, teamId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.SchedulesByTeamAndSeasonId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the SchedulesByTeamAndSeasonIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Team and Season ID
    ApiResponse<SportSchedulesByTeamAndSeasonIdResponse> response = apiInstance.SchedulesByTeamAndSeasonIdWithHttpInfo(version, sport, seasonId, teamId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.SchedulesByTeamAndSeasonIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve schedule from. |  |
| **teamId** | **int** | The ID of the team you want to retrieve schedule from. |  |

### Return type

[**SportSchedulesByTeamAndSeasonIdResponse**](SportSchedulesByTeamAndSeasonIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="schedulesbyteamid"></a>
# **SchedulesByTeamId**
> SportSchedulesByTeamIdResponse SchedulesByTeamId (string version, string sport, int teamId)

By Team ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class SchedulesByTeamIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var teamId = 282;  // int | The ID of the team you want to retrieve schedule from.

            try
            {
                // By Team ID
                SportSchedulesByTeamIdResponse result = apiInstance.SchedulesByTeamId(version, sport, teamId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.SchedulesByTeamId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the SchedulesByTeamIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Team ID
    ApiResponse<SportSchedulesByTeamIdResponse> response = apiInstance.SchedulesByTeamIdWithHttpInfo(version, sport, teamId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.SchedulesByTeamIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **teamId** | **int** | The ID of the team you want to retrieve schedule from. |  |

### Return type

[**SportSchedulesByTeamIdResponse**](SportSchedulesByTeamIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="seasonbyid"></a>
# **SeasonById**
> SportSeasonByIdResponse SeasonById (string version, string sport, int seasonId)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class SeasonByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | The ID of the season you want to retrieve.

            try
            {
                // By ID
                SportSeasonByIdResponse result = apiInstance.SeasonById(version, sport, seasonId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.SeasonById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the SeasonByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<SportSeasonByIdResponse> response = apiInstance.SeasonByIdWithHttpInfo(version, sport, seasonId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.SeasonByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve. |  |

### Return type

[**SportSeasonByIdResponse**](SportSeasonByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="seasonsall"></a>
# **SeasonsAll**
> SportSeasonsAllResponse SeasonsAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class SeasonsAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportSeasonsAllResponse result = apiInstance.SeasonsAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.SeasonsAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the SeasonsAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportSeasonsAllResponse> response = apiInstance.SeasonsAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.SeasonsAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportSeasonsAllResponse**](SportSeasonsAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="seasonsbyteamid"></a>
# **SeasonsByTeamId**
> Object SeasonsByTeamId (string version, string sport, int teamId)

By Team ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class SeasonsByTeamIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var teamId = 282;  // int | The ID of the team you want to retrieve seasons from.

            try
            {
                // By Team ID
                Object result = apiInstance.SeasonsByTeamId(version, sport, teamId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.SeasonsByTeamId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the SeasonsByTeamIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Team ID
    ApiResponse<Object> response = apiInstance.SeasonsByTeamIdWithHttpInfo(version, sport, teamId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.SeasonsByTeamIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **teamId** | **int** | The ID of the team you want to retrieve seasons from. |  |

### Return type

**Object**

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="seasonssearch"></a>
# **SeasonsSearch**
> SportSeasonsSearchResponse SeasonsSearch (string version, string sport, int name)

Search

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class SeasonsSearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var name = 2022;  // int | The name you want to search on.

            try
            {
                // Search
                SportSeasonsSearchResponse result = apiInstance.SeasonsSearch(version, sport, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.SeasonsSearch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the SeasonsSearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<SportSeasonsSearchResponse> response = apiInstance.SeasonsSearchWithHttpInfo(version, sport, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.SeasonsSearchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **name** | **int** | The name you want to search on. |  |

### Return type

[**SportSeasonsSearchResponse**](SportSeasonsSearchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="squadsbyseasonandteamid"></a>
# **SquadsBySeasonAndTeamId**
> SportSquadsBySeasonAndTeamIdResponse SquadsBySeasonAndTeamId (string version, string sport, int seasonId, int teamId)

By Season and Team ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class SquadsBySeasonAndTeamIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | The ID of the season you want to retrieve squads from.
            var teamId = 282;  // int | The ID of the team you want to retrieve squads from.

            try
            {
                // By Season and Team ID
                SportSquadsBySeasonAndTeamIdResponse result = apiInstance.SquadsBySeasonAndTeamId(version, sport, seasonId, teamId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.SquadsBySeasonAndTeamId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the SquadsBySeasonAndTeamIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Season and Team ID
    ApiResponse<SportSquadsBySeasonAndTeamIdResponse> response = apiInstance.SquadsBySeasonAndTeamIdWithHttpInfo(version, sport, seasonId, teamId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.SquadsBySeasonAndTeamIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve squads from. |  |
| **teamId** | **int** | The ID of the team you want to retrieve squads from. |  |

### Return type

[**SportSquadsBySeasonAndTeamIdResponse**](SportSquadsBySeasonAndTeamIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="squadsbyteamid"></a>
# **SquadsByTeamId**
> SportSquadsByTeamIdResponse SquadsByTeamId (string version, string sport, int teamId)

By Team ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class SquadsByTeamIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var teamId = 282;  // int | The ID of the team you want to retrieve squads from.

            try
            {
                // By Team ID
                SportSquadsByTeamIdResponse result = apiInstance.SquadsByTeamId(version, sport, teamId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.SquadsByTeamId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the SquadsByTeamIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Team ID
    ApiResponse<SportSquadsByTeamIdResponse> response = apiInstance.SquadsByTeamIdWithHttpInfo(version, sport, teamId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.SquadsByTeamIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **teamId** | **int** | The ID of the team you want to retrieve squads from. |  |

### Return type

[**SportSquadsByTeamIdResponse**](SportSquadsByTeamIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="stagebyid"></a>
# **StageById**
> SportStageByIdResponse StageById (string version, string sport, int stageId)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class StageByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var stageId = 1100;  // int | The ID of the stage you want to retrieve.

            try
            {
                // By ID
                SportStageByIdResponse result = apiInstance.StageById(version, sport, stageId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.StageById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the StageByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<SportStageByIdResponse> response = apiInstance.StageByIdWithHttpInfo(version, sport, stageId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.StageByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **stageId** | **int** | The ID of the stage you want to retrieve. |  |

### Return type

[**SportStageByIdResponse**](SportStageByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="stagesall"></a>
# **StagesAll**
> SportStagesAllResponse StagesAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class StagesAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportStagesAllResponse result = apiInstance.StagesAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.StagesAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the StagesAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportStagesAllResponse> response = apiInstance.StagesAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.StagesAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportStagesAllResponse**](SportStagesAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="stagesbyseasonid"></a>
# **StagesBySeasonId**
> SportStagesBySeasonIdResponse StagesBySeasonId (string version, string sport, int seasonId)

By Season ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class StagesBySeasonIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | The ID of the season you want to retrieve stages from.

            try
            {
                // By Season ID
                SportStagesBySeasonIdResponse result = apiInstance.StagesBySeasonId(version, sport, seasonId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.StagesBySeasonId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the StagesBySeasonIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Season ID
    ApiResponse<SportStagesBySeasonIdResponse> response = apiInstance.StagesBySeasonIdWithHttpInfo(version, sport, seasonId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.StagesBySeasonIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve stages from. |  |

### Return type

[**SportStagesBySeasonIdResponse**](SportStagesBySeasonIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="stagessearch"></a>
# **StagesSearch**
> SportStagesSearchResponse StagesSearch (string version, string sport, string name)

Search

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class StagesSearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var name = Championship;  // string | The name you want to search on.

            try
            {
                // Search
                SportStagesSearchResponse result = apiInstance.StagesSearch(version, sport, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.StagesSearch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the StagesSearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<SportStagesSearchResponse> response = apiInstance.StagesSearchWithHttpInfo(version, sport, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.StagesSearchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **name** | **string** | The name you want to search on. |  |

### Return type

[**SportStagesSearchResponse**](SportStagesSearchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="standingcorrectionsbyseasonid"></a>
# **StandingCorrectionsBySeasonId**
> SportStandingCorrectionsBySeasonIdResponse StandingCorrectionsBySeasonId (string version, string sport, int seasonId)

Correction by Season ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class StandingCorrectionsBySeasonIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | The ID of the season you want to retrieve standing corrections from.

            try
            {
                // Correction by Season ID
                SportStandingCorrectionsBySeasonIdResponse result = apiInstance.StandingCorrectionsBySeasonId(version, sport, seasonId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.StandingCorrectionsBySeasonId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the StandingCorrectionsBySeasonIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Correction by Season ID
    ApiResponse<SportStandingCorrectionsBySeasonIdResponse> response = apiInstance.StandingCorrectionsBySeasonIdWithHttpInfo(version, sport, seasonId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.StandingCorrectionsBySeasonIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve standing corrections from. |  |

### Return type

[**SportStandingCorrectionsBySeasonIdResponse**](SportStandingCorrectionsBySeasonIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="standingsall"></a>
# **StandingsAll**
> SportStandingsAllResponse StandingsAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class StandingsAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportStandingsAllResponse result = apiInstance.StandingsAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.StandingsAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the StandingsAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportStandingsAllResponse> response = apiInstance.StandingsAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.StandingsAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportStandingsAllResponse**](SportStandingsAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="standingsbyroundid"></a>
# **StandingsByRoundId**
> SportStandingsByRoundIdResponse StandingsByRoundId (string version, string sport, int roundId)

By Round ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class StandingsByRoundIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var roundId = 23318;  // int | The ID of the round you want to retrieve standing from.

            try
            {
                // By Round ID
                SportStandingsByRoundIdResponse result = apiInstance.StandingsByRoundId(version, sport, roundId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.StandingsByRoundId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the StandingsByRoundIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Round ID
    ApiResponse<SportStandingsByRoundIdResponse> response = apiInstance.StandingsByRoundIdWithHttpInfo(version, sport, roundId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.StandingsByRoundIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **roundId** | **int** | The ID of the round you want to retrieve standing from. |  |

### Return type

[**SportStandingsByRoundIdResponse**](SportStandingsByRoundIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="standingsbyseasonid"></a>
# **StandingsBySeasonId**
> SportStandingsBySeasonIdResponse StandingsBySeasonId (string version, string sport, int seasonId)

By Season ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class StandingsBySeasonIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | The ID of the season you want to retrieve standing from.

            try
            {
                // By Season ID
                SportStandingsBySeasonIdResponse result = apiInstance.StandingsBySeasonId(version, sport, seasonId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.StandingsBySeasonId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the StandingsBySeasonIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Season ID
    ApiResponse<SportStandingsBySeasonIdResponse> response = apiInstance.StandingsBySeasonIdWithHttpInfo(version, sport, seasonId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.StandingsBySeasonIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve standing from. |  |

### Return type

[**SportStandingsBySeasonIdResponse**](SportStandingsBySeasonIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="standingslivebyleagueid"></a>
# **StandingsLiveByLeagueId**
> SportStandingsLiveByLeagueIdResponse StandingsLiveByLeagueId (string version, string sport, int leagueId)

By League ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class StandingsLiveByLeagueIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var leagueId = 271;  // int | The ID of the league you want to retrieve standings from.

            try
            {
                // By League ID
                SportStandingsLiveByLeagueIdResponse result = apiInstance.StandingsLiveByLeagueId(version, sport, leagueId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.StandingsLiveByLeagueId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the StandingsLiveByLeagueIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By League ID
    ApiResponse<SportStandingsLiveByLeagueIdResponse> response = apiInstance.StandingsLiveByLeagueIdWithHttpInfo(version, sport, leagueId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.StandingsLiveByLeagueIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **leagueId** | **int** | The ID of the league you want to retrieve standings from. |  |

### Return type

[**SportStandingsLiveByLeagueIdResponse**](SportStandingsLiveByLeagueIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="statebyid"></a>
# **StateById**
> SportStateByIdResponse StateById (string version, string sport, int stateId)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class StateByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var stateId = 1;  // int | The ID of the state you want to retrieve.

            try
            {
                // By ID
                SportStateByIdResponse result = apiInstance.StateById(version, sport, stateId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.StateById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the StateByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<SportStateByIdResponse> response = apiInstance.StateByIdWithHttpInfo(version, sport, stateId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.StateByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **stateId** | **int** | The ID of the state you want to retrieve. |  |

### Return type

[**SportStateByIdResponse**](SportStateByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="statesbysport"></a>
# **StatesBySport**
> SportStatesBySportResponse StatesBySport (string version, string sport)

By Sport

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class StatesBySportExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // By Sport
                SportStatesBySportResponse result = apiInstance.StatesBySport(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.StatesBySport: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the StatesBySportWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Sport
    ApiResponse<SportStatesBySportResponse> response = apiInstance.StatesBySportWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.StatesBySportWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportStatesBySportResponse**](SportStatesBySportResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="teamsall"></a>
# **TeamsAll**
> SportTeamsAllResponse TeamsAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TeamsAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportTeamsAllResponse result = apiInstance.TeamsAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TeamsAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TeamsAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportTeamsAllResponse> response = apiInstance.TeamsAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TeamsAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportTeamsAllResponse**](SportTeamsAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="teamsbycountryid"></a>
# **TeamsByCountryId**
> SportTeamsByCountryIdResponse TeamsByCountryId (string version, string sport, int countryId)

By Country ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TeamsByCountryIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var countryId = 320;  // int | The ID of the country you want to retrieve teams from.

            try
            {
                // By Country ID
                SportTeamsByCountryIdResponse result = apiInstance.TeamsByCountryId(version, sport, countryId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TeamsByCountryId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TeamsByCountryIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Country ID
    ApiResponse<SportTeamsByCountryIdResponse> response = apiInstance.TeamsByCountryIdWithHttpInfo(version, sport, countryId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TeamsByCountryIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **countryId** | **int** | The ID of the country you want to retrieve teams from. |  |

### Return type

[**SportTeamsByCountryIdResponse**](SportTeamsByCountryIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="teamsbyid"></a>
# **TeamsById**
> SportTeamsByIdResponse TeamsById (string version, string sport, int teamId)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TeamsByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var teamId = 180;  // int | The ID of the team you want to retrieve.

            try
            {
                // By ID
                SportTeamsByIdResponse result = apiInstance.TeamsById(version, sport, teamId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TeamsById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TeamsByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<SportTeamsByIdResponse> response = apiInstance.TeamsByIdWithHttpInfo(version, sport, teamId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TeamsByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **teamId** | **int** | The ID of the team you want to retrieve. |  |

### Return type

[**SportTeamsByIdResponse**](SportTeamsByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="teamsbyseasonid"></a>
# **TeamsBySeasonId**
> SportTeamsBySeasonIdResponse TeamsBySeasonId (string version, string sport, int seasonId)

By Season ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TeamsBySeasonIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | The ID of the season you want to retrieve teams from.

            try
            {
                // By Season ID
                SportTeamsBySeasonIdResponse result = apiInstance.TeamsBySeasonId(version, sport, seasonId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TeamsBySeasonId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TeamsBySeasonIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Season ID
    ApiResponse<SportTeamsBySeasonIdResponse> response = apiInstance.TeamsBySeasonIdWithHttpInfo(version, sport, seasonId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TeamsBySeasonIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve teams from. |  |

### Return type

[**SportTeamsBySeasonIdResponse**](SportTeamsBySeasonIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="teamssearch"></a>
# **TeamsSearch**
> SportTeamsSearchResponse TeamsSearch (string version, string sport, string name)

Search

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TeamsSearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var name = Hors;  // string | The name you want to search on.

            try
            {
                // Search
                SportTeamsSearchResponse result = apiInstance.TeamsSearch(version, sport, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TeamsSearch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TeamsSearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<SportTeamsSearchResponse> response = apiInstance.TeamsSearchWithHttpInfo(version, sport, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TeamsSearchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **name** | **string** | The name you want to search on. |  |

### Return type

[**SportTeamsSearchResponse**](SportTeamsSearchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="topscorersbyseasonid"></a>
# **TopScorersBySeasonId**
> SportTopScorersBySeasonIdResponse TopScorersBySeasonId (string version, string sport, int seasonId)

By Season ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TopScorersBySeasonIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | The ID of the season you want to retrieve topscorers from.

            try
            {
                // By Season ID
                SportTopScorersBySeasonIdResponse result = apiInstance.TopScorersBySeasonId(version, sport, seasonId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TopScorersBySeasonId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TopScorersBySeasonIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Season ID
    ApiResponse<SportTopScorersBySeasonIdResponse> response = apiInstance.TopScorersBySeasonIdWithHttpInfo(version, sport, seasonId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TopScorersBySeasonIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve topscorers from. |  |

### Return type

[**SportTopScorersBySeasonIdResponse**](SportTopScorersBySeasonIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="topscorersbystageid"></a>
# **TopScorersByStageId**
> SportTopScorersByStageIdResponse TopScorersByStageId (string version, string sport, int stageId)

By Stage ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TopScorersByStageIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var stageId = 1100;  // int | The ID of the stage you want to retrieve topscorers from.

            try
            {
                // By Stage ID
                SportTopScorersByStageIdResponse result = apiInstance.TopScorersByStageId(version, sport, stageId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TopScorersByStageId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TopScorersByStageIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Stage ID
    ApiResponse<SportTopScorersByStageIdResponse> response = apiInstance.TopScorersByStageIdWithHttpInfo(version, sport, stageId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TopScorersByStageIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **stageId** | **int** | The ID of the stage you want to retrieve topscorers from. |  |

### Return type

[**SportTopScorersByStageIdResponse**](SportTopScorersByStageIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="tranfersbydaterange"></a>
# **TranfersByDateRange**
> SportTranfersByDateRangeResponse TranfersByDateRange (string version, string sport, string startDate, string endDate)

By Date Range

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TranfersByDateRangeExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var startDate = 2021-12-27;  // string | The start date you want to retrieve transfers from.
            var endDate = 2021-12-30;  // string | The end date you want to retrieve transfers from.

            try
            {
                // By Date Range
                SportTranfersByDateRangeResponse result = apiInstance.TranfersByDateRange(version, sport, startDate, endDate);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TranfersByDateRange: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TranfersByDateRangeWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Date Range
    ApiResponse<SportTranfersByDateRangeResponse> response = apiInstance.TranfersByDateRangeWithHttpInfo(version, sport, startDate, endDate);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TranfersByDateRangeWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **startDate** | **string** | The start date you want to retrieve transfers from. |  |
| **endDate** | **string** | The end date you want to retrieve transfers from. |  |

### Return type

[**SportTranfersByDateRangeResponse**](SportTranfersByDateRangeResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="transferbyid"></a>
# **TransferById**
> SportTransferByIdResponse TransferById (string version, string sport, int transferId)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TransferByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var transferId = 1;  // int | 

            try
            {
                // By ID
                SportTransferByIdResponse result = apiInstance.TransferById(version, sport, transferId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TransferById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TransferByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<SportTransferByIdResponse> response = apiInstance.TransferByIdWithHttpInfo(version, sport, transferId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TransferByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **transferId** | **int** |  |  |

### Return type

[**SportTransferByIdResponse**](SportTransferByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="transfersall"></a>
# **TransfersAll**
> SportTransfersAllResponse TransfersAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TransfersAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportTransfersAllResponse result = apiInstance.TransfersAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TransfersAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TransfersAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportTransfersAllResponse> response = apiInstance.TransfersAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TransfersAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportTransfersAllResponse**](SportTransfersAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="transfersbyplayerid"></a>
# **TransfersByPlayerId**
> SportTransfersByPlayerIdResponse TransfersByPlayerId (string version, string sport, int playerId)

By Player ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TransfersByPlayerIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var playerId = 35659846;  // int | The ID of the player you want to retrieve transfers from.

            try
            {
                // By Player ID
                SportTransfersByPlayerIdResponse result = apiInstance.TransfersByPlayerId(version, sport, playerId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TransfersByPlayerId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TransfersByPlayerIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Player ID
    ApiResponse<SportTransfersByPlayerIdResponse> response = apiInstance.TransfersByPlayerIdWithHttpInfo(version, sport, playerId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TransfersByPlayerIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **playerId** | **int** | The ID of the player you want to retrieve transfers from. |  |

### Return type

[**SportTransfersByPlayerIdResponse**](SportTransfersByPlayerIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="transfersbyteamid"></a>
# **TransfersByTeamId**
> SportTransfersByTeamIdResponse TransfersByTeamId (string version, string sport, int teamId)

By Team ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TransfersByTeamIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var teamId = 3736;  // int | The ID of the team you want to retrieve transfers from.

            try
            {
                // By Team ID
                SportTransfersByTeamIdResponse result = apiInstance.TransfersByTeamId(version, sport, teamId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TransfersByTeamId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TransfersByTeamIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Team ID
    ApiResponse<SportTransfersByTeamIdResponse> response = apiInstance.TransfersByTeamIdWithHttpInfo(version, sport, teamId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TransfersByTeamIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **teamId** | **int** | The ID of the team you want to retrieve transfers from. |  |

### Return type

[**SportTransfersByTeamIdResponse**](SportTransfersByTeamIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="transferslatest"></a>
# **TransfersLatest**
> SportTransfersLatestResponse TransfersLatest (string version, string sport)

Last Updated

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TransfersLatestExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // Last Updated
                SportTransfersLatestResponse result = apiInstance.TransfersLatest(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TransfersLatest: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TransfersLatestWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Last Updated
    ApiResponse<SportTransfersLatestResponse> response = apiInstance.TransfersLatestWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TransfersLatestWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportTransfersLatestResponse**](SportTransfersLatestResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="tvstationbyid"></a>
# **TvStationById**
> SportTvStationByIdResponse TvStationById (string version, string sport, int tvStationId)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TvStationByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var tvStationId = 33;  // int | The ID of the tv station you want to retrieve.

            try
            {
                // By ID
                SportTvStationByIdResponse result = apiInstance.TvStationById(version, sport, tvStationId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TvStationById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TvStationByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<SportTvStationByIdResponse> response = apiInstance.TvStationByIdWithHttpInfo(version, sport, tvStationId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TvStationByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **tvStationId** | **int** | The ID of the tv station you want to retrieve. |  |

### Return type

[**SportTvStationByIdResponse**](SportTvStationByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="tvstationsall"></a>
# **TvStationsAll**
> SportTvStationsAllResponse TvStationsAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TvStationsAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportTvStationsAllResponse result = apiInstance.TvStationsAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TvStationsAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TvStationsAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportTvStationsAllResponse> response = apiInstance.TvStationsAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TvStationsAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportTvStationsAllResponse**](SportTvStationsAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="tvstationsbyfixtureid"></a>
# **TvStationsByFixtureId**
> SportTvStationsByFixtureIdResponse TvStationsByFixtureId (string version, string sport, int fixtureId)

By Fixture ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class TvStationsByFixtureIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var fixtureId = 16808591;  // int | The ID of the fixture you want to retrieve tv-stations from.

            try
            {
                // By Fixture ID
                SportTvStationsByFixtureIdResponse result = apiInstance.TvStationsByFixtureId(version, sport, fixtureId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.TvStationsByFixtureId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the TvStationsByFixtureIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Fixture ID
    ApiResponse<SportTvStationsByFixtureIdResponse> response = apiInstance.TvStationsByFixtureIdWithHttpInfo(version, sport, fixtureId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.TvStationsByFixtureIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **fixtureId** | **int** | The ID of the fixture you want to retrieve tv-stations from. |  |

### Return type

[**SportTvStationsByFixtureIdResponse**](SportTvStationsByFixtureIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="venuebyid"></a>
# **VenueById**
> SportVenueByIdResponse VenueById (string version, string sport, int venueId)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class VenueByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var venueId = 219;  // int | The ID of the venue you want to retrieve.

            try
            {
                // By ID
                SportVenueByIdResponse result = apiInstance.VenueById(version, sport, venueId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.VenueById: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the VenueByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<SportVenueByIdResponse> response = apiInstance.VenueByIdWithHttpInfo(version, sport, venueId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.VenueByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **venueId** | **int** | The ID of the venue you want to retrieve. |  |

### Return type

[**SportVenueByIdResponse**](SportVenueByIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="venuesall"></a>
# **VenuesAll**
> SportVenuesAllResponse VenuesAll (string version, string sport)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class VenuesAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.

            try
            {
                // All
                SportVenuesAllResponse result = apiInstance.VenuesAll(version, sport);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.VenuesAll: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the VenuesAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<SportVenuesAllResponse> response = apiInstance.VenuesAllWithHttpInfo(version, sport);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.VenuesAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |

### Return type

[**SportVenuesAllResponse**](SportVenuesAllResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="venuesbyseasonid"></a>
# **VenuesBySeasonId**
> SportVenuesBySeasonIdResponse VenuesBySeasonId (string version, string sport, int seasonId)

By Season ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class VenuesBySeasonIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var seasonId = 19686;  // int | The ID of the season you want to retrieve venues from.

            try
            {
                // By Season ID
                SportVenuesBySeasonIdResponse result = apiInstance.VenuesBySeasonId(version, sport, seasonId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.VenuesBySeasonId: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the VenuesBySeasonIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Season ID
    ApiResponse<SportVenuesBySeasonIdResponse> response = apiInstance.VenuesBySeasonIdWithHttpInfo(version, sport, seasonId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.VenuesBySeasonIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **seasonId** | **int** | The ID of the season you want to retrieve venues from. |  |

### Return type

[**SportVenuesBySeasonIdResponse**](SportVenuesBySeasonIdResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a name="venuessearch"></a>
# **VenuesSearch**
> SportVenuesSearchResponse VenuesSearch (string version, string sport, string name)

Search

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Api;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class VenuesSearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new SportApi(config);
            var version = v3;  // string | The version of the API.
            var sport = football;  // string | The sport you want retrieve entities from.
            var name = Park;  // string | The name you want to search on.

            try
            {
                // Search
                SportVenuesSearchResponse result = apiInstance.VenuesSearch(version, sport, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling SportApi.VenuesSearch: " + e.Message);
                Console.WriteLine("Status Code: "+ e.ErrorCode);
                Console.WriteLine(e.StackTrace);
            }
            catch (ClientException e)
            {
                Console.WriteLine(e.Response.StatusCode);
                Console.WriteLine(e.Response.RawContent);
                Console.WriteLine(e.InnerException);
            }
        }
    }
}
```

#### Using the VenuesSearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<SportVenuesSearchResponse> response = apiInstance.VenuesSearchWithHttpInfo(version, sport, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling SportApi.VenuesSearchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **sport** | **string** | The sport you want retrieve entities from. |  |
| **name** | **string** | The name you want to search on. |  |

### Return type

[**SportVenuesSearchResponse**](SportVenuesSearchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

