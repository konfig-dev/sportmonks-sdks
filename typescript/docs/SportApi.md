# SportApi

All URIs are relative to *https://api.sportmonks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**coachById**](SportApi.md#coachById) | **GET** /{version}/{sport}/coaches/{coachId} | By ID
[**coachesAll**](SportApi.md#coachesAll) | **GET** /{version}/{sport}/coaches | All
[**coachesByCountryId**](SportApi.md#coachesByCountryId) | **GET** /{version}/{sport}/coaches/countries/{countryId} | By Country ID
[**coachesLatest**](SportApi.md#coachesLatest) | **GET** /{version}/{sport}/coaches/latest | Last updated
[**coachesSearch**](SportApi.md#coachesSearch) | **GET** /{version}/{sport}/coaches/search/{name} | Search
[**commentariesAll**](SportApi.md#commentariesAll) | **GET** /{version}/{sport}/commentaries | All
[**commentariesByFixtureId**](SportApi.md#commentariesByFixtureId) | **GET** /{version}/{sport}/commentaries/fixtures/{fixtureId} | By Fixture ID
[**fixtureByDateRangeForTeam**](SportApi.md#fixtureByDateRangeForTeam) | **GET** /{version}/{sport}/fixtures/between/{startDate}/{endDate}/{teamId} | By Date Range for Team
[**fixtureById**](SportApi.md#fixtureById) | **GET** /{version}/{sport}/fixtures/{fixtureId} | Fixture ID
[**fixturesAll**](SportApi.md#fixturesAll) | **GET** /{version}/{sport}/fixtures | All
[**fixturesByDate**](SportApi.md#fixturesByDate) | **GET** /{version}/{sport}/fixtures/date/{date} | By Date
[**fixturesByDateRange**](SportApi.md#fixturesByDateRange) | **GET** /{version}/{sport}/fixtures/between/{startDate}/{endDate} | By Date Range
[**fixturesByIds**](SportApi.md#fixturesByIds) | **GET** /{version}/{sport}/fixtures/multi/{fixtureIds} | By IDs
[**fixturesHeadToHead**](SportApi.md#fixturesHeadToHead) | **GET** /{version}/{sport}/fixtures/head-to-head/{firstTeam}/{secondTeam} | Head to Head
[**fixturesLatest**](SportApi.md#fixturesLatest) | **GET** /{version}/{sport}/fixtures/latest | Last Updated
[**fixturesSearch**](SportApi.md#fixturesSearch) | **GET** /{version}/{sport}/fixtures/search/{name} | Search
[**leagueById**](SportApi.md#leagueById) | **GET** /{version}/{sport}/leagues/{leagueId} | By ID
[**leagueEnrichments**](SportApi.md#leagueEnrichments) | **GET** /{version}/{sport}/leagues/{leagueId}/includes | Enrichments
[**leagueShirts**](SportApi.md#leagueShirts) | **GET** /{version}/{sport}/leagues/{leagueId}/jerseys | Shirts By League ID
[**leaguesAll**](SportApi.md#leaguesAll) | **GET** /{version}/{sport}/leagues | All
[**leaguesByCountryId**](SportApi.md#leaguesByCountryId) | **GET** /{version}/{sport}/leagues/countries/{countryId} | By Country ID
[**leaguesByDate**](SportApi.md#leaguesByDate) | **GET** /{version}/{sport}/leagues/date/{date} | By Date
[**leaguesByTeamId**](SportApi.md#leaguesByTeamId) | **GET** /{version}/{sport}/teams/{teamId}/leagues | Leagues By Team ID
[**leaguesCurrentByTeamId**](SportApi.md#leaguesCurrentByTeamId) | **GET** /{version}/{sport}/teams/{teamId}/leagues/current | Current Leagues By Team ID
[**leaguesLive**](SportApi.md#leaguesLive) | **GET** /{version}/{sport}/leagues/live | Live
[**leaguesSearch**](SportApi.md#leaguesSearch) | **GET** /{version}/{sport}/leagues/search/{name} | Search
[**livescoresAll**](SportApi.md#livescoresAll) | **GET** /{version}/{sport}/livescores | All
[**livescoresAllInPlay**](SportApi.md#livescoresAllInPlay) | **GET** /{version}/{sport}/livescores/inplay | All In-play
[**livescoresLatest**](SportApi.md#livescoresLatest) | **GET** /{version}/{sport}/livescores/latest | Last Updated In-play
[**newsAllPostMatch**](SportApi.md#newsAllPostMatch) | **GET** /{version}/{sport}/news/post-match | All Post Match
[**newsAllPreMatch**](SportApi.md#newsAllPreMatch) | **GET** /{version}/{sport}/news/pre-match | All Pre-match
[**newsPostMatchBySeasonId**](SportApi.md#newsPostMatchBySeasonId) | **GET** /{version}/{sport}/news/post-match/seasons/{seasonId} | Post Match by Season ID
[**newsPreMatchBySeasonId**](SportApi.md#newsPreMatchBySeasonId) | **GET** /{version}/{sport}/news/pre-match/seasons/{seasonId} | Pre-match By Season ID
[**newsUpcomingPostMatch**](SportApi.md#newsUpcomingPostMatch) | **GET** /{version}/{sport}/news/post-match/upcoming | Upcoming Post Match
[**newsUpcomingPreMatch**](SportApi.md#newsUpcomingPreMatch) | **GET** /{version}/{sport}/news/pre-match/upcoming | Upcoming Pre-match
[**oddsAllInPlay**](SportApi.md#oddsAllInPlay) | **GET** /{version}/{sport}/odds/inplay | All In-play
[**oddsAllPreMatch**](SportApi.md#oddsAllPreMatch) | **GET** /{version}/{sport}/odds/pre-match | All Pre-match
[**oddsInPlayByFixtureAndBookmakerId**](SportApi.md#oddsInPlayByFixtureAndBookmakerId) | **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}/bookmakers/{bookmakerId} | In-play by Fixture and Bookmaker ID
[**oddsInPlayByFixtureAndMarketId**](SportApi.md#oddsInPlayByFixtureAndMarketId) | **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}/markets/{marketId} | In-play by Fixture and Market ID
[**oddsInPlayByFixtureId**](SportApi.md#oddsInPlayByFixtureId) | **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId} | In-play by Fixture ID
[**oddsLatestInPlay**](SportApi.md#oddsLatestInPlay) | **GET** /{version}/{sport}/odds/inplay/latest | Latest In-play
[**oddsLatestPreMatch**](SportApi.md#oddsLatestPreMatch) | **GET** /{version}/{sport}/odds/pre-match/latest | Last Updated Pre-match
[**oddsPreMatchByFixtureAndBookmakerId**](SportApi.md#oddsPreMatchByFixtureAndBookmakerId) | **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}/bookmakers/{bookmakerId} | Pre-match by Fixture and Bookmaker ID
[**oddsPreMatchByFixtureAndMarketId**](SportApi.md#oddsPreMatchByFixtureAndMarketId) | **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}/markets/{marketId} | Pre-match by Fixture and Market ID
[**oddsPreMatchByFixtureId**](SportApi.md#oddsPreMatchByFixtureId) | **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId} | Pre-match by Fixture ID
[**playerById**](SportApi.md#playerById) | **GET** /{version}/{sport}/players/{playerId} | By ID
[**playersAll**](SportApi.md#playersAll) | **GET** /{version}/{sport}/players | All
[**playersByCountryId**](SportApi.md#playersByCountryId) | **GET** /{version}/{sport}/players/countries/{countryId} | By Country ID
[**playersLatest**](SportApi.md#playersLatest) | **GET** /{version}/{sport}/players/latest | Latest Updated
[**playersSearch**](SportApi.md#playersSearch) | **GET** /{version}/{sport}/players/search/{name} | Search
[**predictionsAll**](SportApi.md#predictionsAll) | **GET** /{version}/{sport}/predictions/probabilities | All
[**predictionsAllValueBets**](SportApi.md#predictionsAllValueBets) | **GET** /{version}/{sport}/predictions/value-bets | All Value Bets
[**predictionsByFixtureId**](SportApi.md#predictionsByFixtureId) | **GET** /{version}/{sport}/predictions/probabilities/fixtures/{fixtureId} | By Fixture ID
[**predictionsValueBetsByFixtureId**](SportApi.md#predictionsValueBetsByFixtureId) | **GET** /{version}/{sport}/predictions/value-bets/fixtures/{fixtureId} | Value Bets by Fixture ID
[**refereeById**](SportApi.md#refereeById) | **GET** /{version}/{sport}/referees/{refereeId} | By ID
[**refereesAll**](SportApi.md#refereesAll) | **GET** /{version}/{sport}/referees | All
[**refereesByCountryId**](SportApi.md#refereesByCountryId) | **GET** /{version}/{sport}/referees/countries/{countryId} | By Country ID
[**refereesBySeasonId**](SportApi.md#refereesBySeasonId) | **GET** /{version}/{sport}/referees/seasons/{seasonId} | By Season ID
[**refereesSearch**](SportApi.md#refereesSearch) | **GET** /{version}/{sport}/referees/search/{name} | Search
[**rivalsAll**](SportApi.md#rivalsAll) | **GET** /{version}/{sport}/rivals | All
[**rivalsByTeamId**](SportApi.md#rivalsByTeamId) | **GET** /{version}/{sport}/rivals/teams/{teamId} | By Team ID
[**roundById**](SportApi.md#roundById) | **GET** /{version}/{sport}/rounds/{roundId} | By ID
[**roundsAll**](SportApi.md#roundsAll) | **GET** /{version}/{sport}/rounds | All
[**roundsBySeasonId**](SportApi.md#roundsBySeasonId) | **GET** /{version}/{sport}/rounds/seasons/{seasonId} | Season ID
[**roundsSearch**](SportApi.md#roundsSearch) | **GET** /{version}/{sport}/rounds/search/{name} | Search
[**schedulesBySeasonId**](SportApi.md#schedulesBySeasonId) | **GET** /{version}/{sport}/schedules/seasons/{seasonId} | By Season ID
[**schedulesByTeamAndSeasonId**](SportApi.md#schedulesByTeamAndSeasonId) | **GET** /{version}/{sport}/schedules/seasons/{seasonId}/teams/{teamId} | By Team and Season ID
[**schedulesByTeamId**](SportApi.md#schedulesByTeamId) | **GET** /{version}/{sport}/schedules/teams/{teamId} | By Team ID
[**seasonById**](SportApi.md#seasonById) | **GET** /{version}/{sport}/seasons/{seasonId} | By ID
[**seasonsAll**](SportApi.md#seasonsAll) | **GET** /{version}/{sport}/seasons | All
[**seasonsByTeamId**](SportApi.md#seasonsByTeamId) | **GET** /{version}/{sport}/seasons/teams/{teamId} | By Team ID
[**seasonsSearch**](SportApi.md#seasonsSearch) | **GET** /{version}/{sport}/seasons/search/{name} | Search
[**squadsBySeasonAndTeamId**](SportApi.md#squadsBySeasonAndTeamId) | **GET** /{version}/{sport}/squads/seasons/{seasonId}/teams/{teamId} | By Season and Team ID
[**squadsByTeamId**](SportApi.md#squadsByTeamId) | **GET** /{version}/{sport}/squads/teams/{teamId} | By Team ID
[**stageById**](SportApi.md#stageById) | **GET** /{version}/{sport}/stages/{stageId} | By ID
[**stagesAll**](SportApi.md#stagesAll) | **GET** /{version}/{sport}/stages | All
[**stagesBySeasonId**](SportApi.md#stagesBySeasonId) | **GET** /{version}/{sport}/stages/seasons/{seasonId} | By Season ID
[**stagesSearch**](SportApi.md#stagesSearch) | **GET** /{version}/{sport}/stages/search/{name} | Search
[**standingCorrectionsBySeasonId**](SportApi.md#standingCorrectionsBySeasonId) | **GET** /{version}/{sport}/standings/corrections/seasons/{seasonId} | Correction by Season ID
[**standingsAll**](SportApi.md#standingsAll) | **GET** /{version}/{sport}/standings | All
[**standingsByRoundId**](SportApi.md#standingsByRoundId) | **GET** /{version}/{sport}/standings/rounds/{roundId} | By Round ID
[**standingsBySeasonId**](SportApi.md#standingsBySeasonId) | **GET** /{version}/{sport}/standings/seasons/{seasonId} | By Season ID
[**standingsLiveByLeagueId**](SportApi.md#standingsLiveByLeagueId) | **GET** /{version}/{sport}/standings/live/leagues/{leagueId} | By League ID
[**stateById**](SportApi.md#stateById) | **GET** /{version}/{sport}/states/{stateId} | By ID
[**statesBySport**](SportApi.md#statesBySport) | **GET** /{version}/{sport}/states | By Sport
[**teamsAll**](SportApi.md#teamsAll) | **GET** /{version}/{sport}/teams | All
[**teamsByCountryId**](SportApi.md#teamsByCountryId) | **GET** /{version}/{sport}/teams/countries/{countryId} | By Country ID
[**teamsById**](SportApi.md#teamsById) | **GET** /{version}/{sport}/teams/{teamId} | By ID
[**teamsBySeasonId**](SportApi.md#teamsBySeasonId) | **GET** /{version}/{sport}/teams/seasons/{seasonId} | By Season ID
[**teamsSearch**](SportApi.md#teamsSearch) | **GET** /{version}/{sport}/teams/search/{name} | Search
[**topScorersBySeasonId**](SportApi.md#topScorersBySeasonId) | **GET** /{version}/{sport}/topscorers/seasons/{seasonId} | By Season ID
[**topScorersByStageId**](SportApi.md#topScorersByStageId) | **GET** /{version}/{sport}/topscorers/stages/{stageId} | By Stage ID
[**tranfersByDateRange**](SportApi.md#tranfersByDateRange) | **GET** /{version}/{sport}/transfers/between/{startDate}/{endDate} | By Date Range
[**transferById**](SportApi.md#transferById) | **GET** /{version}/{sport}/transfers/{transferId} | By ID
[**transfersAll**](SportApi.md#transfersAll) | **GET** /{version}/{sport}/transfers | All
[**transfersByPlayerId**](SportApi.md#transfersByPlayerId) | **GET** /{version}/{sport}/transfers/players/{playerId} | By Player ID
[**transfersByTeamId**](SportApi.md#transfersByTeamId) | **GET** /{version}/{sport}/transfers/teams/{teamId} | By Team ID
[**transfersLatest**](SportApi.md#transfersLatest) | **GET** /{version}/{sport}/transfers/latest | Last Updated
[**tvStationById**](SportApi.md#tvStationById) | **GET** /{version}/{sport}/tv-stations/{tvStationId} | By ID
[**tvStationsAll**](SportApi.md#tvStationsAll) | **GET** /{version}/{sport}/tv-stations | All
[**tvStationsByFixtureId**](SportApi.md#tvStationsByFixtureId) | **GET** /{version}/{sport}/tv-stations/fixtures/{fixtureId} | By Fixture ID
[**venueById**](SportApi.md#venueById) | **GET** /{version}/{sport}/venues/{venueId} | By ID
[**venuesAll**](SportApi.md#venuesAll) | **GET** /{version}/{sport}/venues | All
[**venuesBySeasonId**](SportApi.md#venuesBySeasonId) | **GET** /{version}/{sport}/venues/seasons/{seasonId} | By Season ID
[**venuesSearch**](SportApi.md#venuesSearch) | **GET** /{version}/{sport}/venues/search/{name} | Search


# **coachById**

#### **GET** /{version}/{sport}/coaches/{coachId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const coachByIdResponse = await sportmonks.sport.coachById({
  coachId: 1,
});

console.log(coachByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coachId** | [**number**] | The ID of the coach you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportCoachByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **coachesAll**

#### **GET** /{version}/{sport}/coaches


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const coachesAllResponse = await sportmonks.sport.coachesAll({});

console.log(coachesAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportCoachesAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **coachesByCountryId**

#### **GET** /{version}/{sport}/coaches/countries/{countryId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const coachesByCountryIdResponse = await sportmonks.sport.coachesByCountryId({
  countryId: 1,
});

console.log(coachesByCountryIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryId** | [**number**] | The ID of the country you want to retrieve coaches from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportCoachesByCountryIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **coachesLatest**

#### **GET** /{version}/{sport}/coaches/latest


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const coachesLatestResponse = await sportmonks.sport.coachesLatest({});

console.log(coachesLatestResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportCoachesLatestResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **coachesSearch**

#### **GET** /{version}/{sport}/coaches/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const coachesSearchResponse = await sportmonks.sport.coachesSearch({
  name: "name_example",
});

console.log(coachesSearchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**string**] | The name you want to search on. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportCoachesSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **commentariesAll**

#### **GET** /{version}/{sport}/commentaries


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const commentariesAllResponse = await sportmonks.sport.commentariesAll({});

console.log(commentariesAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportCommentariesAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **commentariesByFixtureId**

#### **GET** /{version}/{sport}/commentaries/fixtures/{fixtureId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const commentariesByFixtureIdResponse =
  await sportmonks.sport.commentariesByFixtureId({
    fixtureId: 1,
  });

console.log(commentariesByFixtureIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixtureId** | [**number**] | The ID of the fixture you want to retrieve commentaries from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportCommentariesByFixtureIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **fixtureByDateRangeForTeam**

#### **GET** /{version}/{sport}/fixtures/between/{startDate}/{endDate}/{teamId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const fixtureByDateRangeForTeamResponse =
  await sportmonks.sport.fixtureByDateRangeForTeam({
    startDate: "startDate_example",
    endDate: "endDate_example",
    teamId: "teamId_example",
  });

console.log(fixtureByDateRangeForTeamResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startDate** | [**string**] |  | defaults to undefined
 **endDate** | [**string**] |  | defaults to undefined
 **teamId** | [**string**] |  | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportFixtureByDateRangeForTeamResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **fixtureById**

#### **GET** /{version}/{sport}/fixtures/{fixtureId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const fixtureByIdResponse = await sportmonks.sport.fixtureById({
  fixtureId: 1,
});

console.log(fixtureByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixtureId** | [**number**] | The ID of the fixture you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportFixtureByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **fixturesAll**

#### **GET** /{version}/{sport}/fixtures


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const fixturesAllResponse = await sportmonks.sport.fixturesAll({});

console.log(fixturesAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportFixturesAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **fixturesByDate**

#### **GET** /{version}/{sport}/fixtures/date/{date}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const fixturesByDateResponse = await sportmonks.sport.fixturesByDate({
  date: "date_example",
});

console.log(fixturesByDateResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | [**string**] | The date you want to retrieve fixtures from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportFixturesByDateResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **fixturesByDateRange**

#### **GET** /{version}/{sport}/fixtures/between/{startDate}/{endDate}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const fixturesByDateRangeResponse = await sportmonks.sport.fixturesByDateRange({
  startDate: "startDate_example",
  endDate: "endDate_example",
});

console.log(fixturesByDateRangeResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startDate** | [**string**] | The start date you want to retrieve fixtures from. | defaults to undefined
 **endDate** | [**string**] | The end date you want to retrieve fixtures from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportFixturesByDateRangeResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **fixturesByIds**

#### **GET** /{version}/{sport}/fixtures/multi/{fixtureIds}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const fixturesByIdsResponse = await sportmonks.sport.fixturesByIds({
  fixtureIds: "fixtureIds_example",
});

console.log(fixturesByIdsResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixtureIds** | [**string**] | The IDs you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportFixturesByIdsResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **fixturesHeadToHead**

#### **GET** /{version}/{sport}/fixtures/head-to-head/{firstTeam}/{secondTeam}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const fixturesHeadToHeadResponse = await sportmonks.sport.fixturesHeadToHead({
  firstTeam: 1,
  secondTeam: 1,
});

console.log(fixturesHeadToHeadResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firstTeam** | [**number**] | The ID of the first team retrieve fixtures from. | defaults to undefined
 **secondTeam** | [**number**] | The ID of the second team retrieve fixtures from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportFixturesHeadToHeadResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **fixturesLatest**

#### **GET** /{version}/{sport}/fixtures/latest


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const fixturesLatestResponse = await sportmonks.sport.fixturesLatest({});

console.log(fixturesLatestResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**string**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **fixturesSearch**

#### **GET** /{version}/{sport}/fixtures/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const fixturesSearchResponse = await sportmonks.sport.fixturesSearch({
  name: "name_example",
});

console.log(fixturesSearchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**string**] | The name you want search on. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportFixturesSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **leagueById**

#### **GET** /{version}/{sport}/leagues/{leagueId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const leagueByIdResponse = await sportmonks.sport.leagueById({
  leagueId: 1,
});

console.log(leagueByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leagueId** | [**number**] | The ID of the league you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportLeagueByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **leagueEnrichments**

#### **GET** /{version}/{sport}/leagues/{leagueId}/includes


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const leagueEnrichmentsResponse = await sportmonks.sport.leagueEnrichments({
  leagueId: 1,
});

console.log(leagueEnrichmentsResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leagueId** | [**number**] | The ID of the league you want to retrieve enrichments from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **leagueShirts**

#### **GET** /{version}/{sport}/leagues/{leagueId}/jerseys


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const leagueShirtsResponse = await sportmonks.sport.leagueShirts({
  leagueId: 1,
});

console.log(leagueShirtsResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leagueId** | [**number**] | The ID of the league you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **leaguesAll**

#### **GET** /{version}/{sport}/leagues


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const leaguesAllResponse = await sportmonks.sport.leaguesAll({});

console.log(leaguesAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportLeaguesAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **leaguesByCountryId**

#### **GET** /{version}/{sport}/leagues/countries/{countryId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const leaguesByCountryIdResponse = await sportmonks.sport.leaguesByCountryId({
  countryId: 1,
});

console.log(leaguesByCountryIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryId** | [**number**] | The ID of the country you want to retrieve leagues from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportLeaguesByCountryIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **leaguesByDate**

#### **GET** /{version}/{sport}/leagues/date/{date}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const leaguesByDateResponse = await sportmonks.sport.leaguesByDate({
  date: "date_example",
});

console.log(leaguesByDateResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | [**string**] | The date of fixtures you want to retrieve leagues from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportLeaguesByDateResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **leaguesByTeamId**

#### **GET** /{version}/{sport}/teams/{teamId}/leagues


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const leaguesByTeamIdResponse = await sportmonks.sport.leaguesByTeamId({
  teamId: 1,
});

console.log(leaguesByTeamIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | [**number**] | The ID of the team you want to retrieve leagues from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **leaguesCurrentByTeamId**

#### **GET** /{version}/{sport}/teams/{teamId}/leagues/current


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const leaguesCurrentByTeamIdResponse =
  await sportmonks.sport.leaguesCurrentByTeamId({
    teamId: 1,
  });

console.log(leaguesCurrentByTeamIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | [**number**] | The ID of the team you want to retrieve current leagues from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **leaguesLive**

#### **GET** /{version}/{sport}/leagues/live


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const leaguesLiveResponse = await sportmonks.sport.leaguesLive({});

console.log(leaguesLiveResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportLeaguesLiveResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **leaguesSearch**

#### **GET** /{version}/{sport}/leagues/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const leaguesSearchResponse = await sportmonks.sport.leaguesSearch({
  name: "name_example",
});

console.log(leaguesSearchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**string**] | The name you want to search on. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportLeaguesSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **livescoresAll**

#### **GET** /{version}/{sport}/livescores


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const livescoresAllResponse = await sportmonks.sport.livescoresAll({});

console.log(livescoresAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportLivescoresAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **livescoresAllInPlay**

#### **GET** /{version}/{sport}/livescores/inplay


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const livescoresAllInPlayResponse = await sportmonks.sport.livescoresAllInPlay(
  {}
);

console.log(livescoresAllInPlayResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportLivescoresAllInPlayResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **livescoresLatest**

#### **GET** /{version}/{sport}/livescores/latest


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const livescoresLatestResponse = await sportmonks.sport.livescoresLatest({});

console.log(livescoresLatestResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportLivescoresLatestResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **newsAllPostMatch**

#### **GET** /{version}/{sport}/news/post-match


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const newsAllPostMatchResponse = await sportmonks.sport.newsAllPostMatch({});

console.log(newsAllPostMatchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**string**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **newsAllPreMatch**

#### **GET** /{version}/{sport}/news/pre-match


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const newsAllPreMatchResponse = await sportmonks.sport.newsAllPreMatch({});

console.log(newsAllPreMatchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportNewsAllPreMatchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **newsPostMatchBySeasonId**

#### **GET** /{version}/{sport}/news/post-match/seasons/{seasonId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const newsPostMatchBySeasonIdResponse =
  await sportmonks.sport.newsPostMatchBySeasonId({
    seasonId: 1,
  });

console.log(newsPostMatchBySeasonIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve post-match news from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**string**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **newsPreMatchBySeasonId**

#### **GET** /{version}/{sport}/news/pre-match/seasons/{seasonId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const newsPreMatchBySeasonIdResponse =
  await sportmonks.sport.newsPreMatchBySeasonId({
    seasonId: 1,
  });

console.log(newsPreMatchBySeasonIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve post-match news from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportNewsPreMatchBySeasonIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **newsUpcomingPostMatch**

#### **GET** /{version}/{sport}/news/post-match/upcoming


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const newsUpcomingPostMatchResponse =
  await sportmonks.sport.newsUpcomingPostMatch({});

console.log(newsUpcomingPostMatchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**string**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **newsUpcomingPreMatch**

#### **GET** /{version}/{sport}/news/pre-match/upcoming


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const newsUpcomingPreMatchResponse =
  await sportmonks.sport.newsUpcomingPreMatch({});

console.log(newsUpcomingPreMatchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportNewsUpcomingPreMatchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **oddsAllInPlay**

#### **GET** /{version}/{sport}/odds/inplay


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const oddsAllInPlayResponse = await sportmonks.sport.oddsAllInPlay({});

console.log(oddsAllInPlayResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportOddsAllInPlayResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **oddsAllPreMatch**

#### **GET** /{version}/{sport}/odds/pre-match


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const oddsAllPreMatchResponse = await sportmonks.sport.oddsAllPreMatch({});

console.log(oddsAllPreMatchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportOddsAllPreMatchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **oddsInPlayByFixtureAndBookmakerId**

#### **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}/bookmakers/{bookmakerId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const oddsInPlayByFixtureAndBookmakerIdResponse =
  await sportmonks.sport.oddsInPlayByFixtureAndBookmakerId({
    fixtureId: 1,
    bookmakerId: 1,
  });

console.log(oddsInPlayByFixtureAndBookmakerIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixtureId** | [**number**] | The ID of the fixture you want to retrieve in-play odds from. | defaults to undefined
 **bookmakerId** | [**number**] | The ID of the bookmaker you want to retrieve in-play odds from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **oddsInPlayByFixtureAndMarketId**

#### **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}/markets/{marketId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const oddsInPlayByFixtureAndMarketIdResponse =
  await sportmonks.sport.oddsInPlayByFixtureAndMarketId({
    fixtureId: 1,
    marketId: 1,
  });

console.log(oddsInPlayByFixtureAndMarketIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixtureId** | [**number**] | The ID of the fixture you want to retrieve in-play odds from. | defaults to undefined
 **marketId** | [**number**] | The ID of the market you want to retrieve in-play odds from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **oddsInPlayByFixtureId**

#### **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const oddsInPlayByFixtureIdResponse =
  await sportmonks.sport.oddsInPlayByFixtureId({
    fixtureId: 1,
  });

console.log(oddsInPlayByFixtureIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixtureId** | [**number**] | The ID of the fixture you want to retrieve in-play odds from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportOddsInPlayByFixtureIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **oddsLatestInPlay**

#### **GET** /{version}/{sport}/odds/inplay/latest


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const oddsLatestInPlayResponse = await sportmonks.sport.oddsLatestInPlay({});

console.log(oddsLatestInPlayResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **oddsLatestPreMatch**

#### **GET** /{version}/{sport}/odds/pre-match/latest


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const oddsLatestPreMatchResponse = await sportmonks.sport.oddsLatestPreMatch(
  {}
);

console.log(oddsLatestPreMatchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **oddsPreMatchByFixtureAndBookmakerId**

#### **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}/bookmakers/{bookmakerId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const oddsPreMatchByFixtureAndBookmakerIdResponse =
  await sportmonks.sport.oddsPreMatchByFixtureAndBookmakerId({
    fixtureId: 1,
    bookmakerId: 1,
  });

console.log(oddsPreMatchByFixtureAndBookmakerIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixtureId** | [**number**] | The ID of the fixture you want to retrieve pre-match odds from. | defaults to undefined
 **bookmakerId** | [**number**] | The ID of the bookmaker you want to retrieve pre-match odds from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportOddsPreMatchByFixtureAndBookmakerIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **oddsPreMatchByFixtureAndMarketId**

#### **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}/markets/{marketId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const oddsPreMatchByFixtureAndMarketIdResponse =
  await sportmonks.sport.oddsPreMatchByFixtureAndMarketId({
    fixtureId: 1,
    marketId: 1,
  });

console.log(oddsPreMatchByFixtureAndMarketIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixtureId** | [**number**] | The ID of the fixture you want to retrieve pre-match odds from. | defaults to undefined
 **marketId** | [**number**] | The ID of the market you want to retrieve pre-match odds from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportOddsPreMatchByFixtureAndMarketIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **oddsPreMatchByFixtureId**

#### **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const oddsPreMatchByFixtureIdResponse =
  await sportmonks.sport.oddsPreMatchByFixtureId({
    fixtureId: 1,
  });

console.log(oddsPreMatchByFixtureIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixtureId** | [**number**] | The ID of the fixture you want to retrieve pre-match odds from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportOddsPreMatchByFixtureIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **playerById**

#### **GET** /{version}/{sport}/players/{playerId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const playerByIdResponse = await sportmonks.sport.playerById({
  playerId: 1,
});

console.log(playerByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playerId** | [**number**] | The ID of the player you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportPlayerByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **playersAll**

#### **GET** /{version}/{sport}/players


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const playersAllResponse = await sportmonks.sport.playersAll({});

console.log(playersAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportPlayersAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **playersByCountryId**

#### **GET** /{version}/{sport}/players/countries/{countryId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const playersByCountryIdResponse = await sportmonks.sport.playersByCountryId({
  countryId: 1,
});

console.log(playersByCountryIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryId** | [**number**] | The ID of the country you want to retrieve players from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportPlayersByCountryIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **playersLatest**

#### **GET** /{version}/{sport}/players/latest


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const playersLatestResponse = await sportmonks.sport.playersLatest({});

console.log(playersLatestResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportPlayersLatestResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **playersSearch**

#### **GET** /{version}/{sport}/players/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const playersSearchResponse = await sportmonks.sport.playersSearch({
  name: "name_example",
});

console.log(playersSearchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**string**] | The name you want to search on. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportPlayersSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **predictionsAll**

#### **GET** /{version}/{sport}/predictions/probabilities


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const predictionsAllResponse = await sportmonks.sport.predictionsAll({});

console.log(predictionsAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportPredictionsAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **predictionsAllValueBets**

#### **GET** /{version}/{sport}/predictions/value-bets


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const predictionsAllValueBetsResponse =
  await sportmonks.sport.predictionsAllValueBets({});

console.log(predictionsAllValueBetsResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportPredictionsAllValueBetsResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **predictionsByFixtureId**

#### **GET** /{version}/{sport}/predictions/probabilities/fixtures/{fixtureId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const predictionsByFixtureIdResponse =
  await sportmonks.sport.predictionsByFixtureId({
    fixtureId: 1,
  });

console.log(predictionsByFixtureIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixtureId** | [**number**] | The ID of the fixture you want to retrieve predictions from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportPredictionsByFixtureIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **predictionsValueBetsByFixtureId**

#### **GET** /{version}/{sport}/predictions/value-bets/fixtures/{fixtureId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const predictionsValueBetsByFixtureIdResponse =
  await sportmonks.sport.predictionsValueBetsByFixtureId({
    fixtureId: 1,
  });

console.log(predictionsValueBetsByFixtureIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixtureId** | [**number**] | The ID of the fixture you want to retrieve value bets from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **refereeById**

#### **GET** /{version}/{sport}/referees/{refereeId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const refereeByIdResponse = await sportmonks.sport.refereeById({
  refereeId: 1,
});

console.log(refereeByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refereeId** | [**number**] | The ID of the referee you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportRefereeByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **refereesAll**

#### **GET** /{version}/{sport}/referees


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const refereesAllResponse = await sportmonks.sport.refereesAll({});

console.log(refereesAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportRefereesAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **refereesByCountryId**

#### **GET** /{version}/{sport}/referees/countries/{countryId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const refereesByCountryIdResponse = await sportmonks.sport.refereesByCountryId({
  countryId: 1,
});

console.log(refereesByCountryIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryId** | [**number**] | The ID of the country you want to retrieve referees from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportRefereesByCountryIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **refereesBySeasonId**

#### **GET** /{version}/{sport}/referees/seasons/{seasonId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const refereesBySeasonIdResponse = await sportmonks.sport.refereesBySeasonId({
  seasonId: 1,
});

console.log(refereesBySeasonIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve referees from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportRefereesBySeasonIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **refereesSearch**

#### **GET** /{version}/{sport}/referees/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const refereesSearchResponse = await sportmonks.sport.refereesSearch({
  name: "name_example",
});

console.log(refereesSearchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**string**] | The name you want to search on. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportRefereesSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **rivalsAll**

#### **GET** /{version}/{sport}/rivals


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const rivalsAllResponse = await sportmonks.sport.rivalsAll({});

console.log(rivalsAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportRivalsAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **rivalsByTeamId**

#### **GET** /{version}/{sport}/rivals/teams/{teamId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const rivalsByTeamIdResponse = await sportmonks.sport.rivalsByTeamId({
  teamId: 1,
});

console.log(rivalsByTeamIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | [**number**] | The ID of the team you want to retrieve rivals from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportRivalsByTeamIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **roundById**

#### **GET** /{version}/{sport}/rounds/{roundId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const roundByIdResponse = await sportmonks.sport.roundById({
  roundId: 1,
});

console.log(roundByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roundId** | [**number**] | The ID of the round you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportRoundByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **roundsAll**

#### **GET** /{version}/{sport}/rounds


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const roundsAllResponse = await sportmonks.sport.roundsAll({});

console.log(roundsAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportRoundsAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **roundsBySeasonId**

#### **GET** /{version}/{sport}/rounds/seasons/{seasonId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const roundsBySeasonIdResponse = await sportmonks.sport.roundsBySeasonId({
  seasonId: 1,
});

console.log(roundsBySeasonIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve rounds from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportRoundsBySeasonIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **roundsSearch**

#### **GET** /{version}/{sport}/rounds/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const roundsSearchResponse = await sportmonks.sport.roundsSearch({
  name: 1,
});

console.log(roundsSearchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**number**] | The name you want to search on. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportRoundsSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **schedulesBySeasonId**

#### **GET** /{version}/{sport}/schedules/seasons/{seasonId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const schedulesBySeasonIdResponse = await sportmonks.sport.schedulesBySeasonId({
  seasonId: 1,
});

console.log(schedulesBySeasonIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] |  | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportSchedulesBySeasonIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **schedulesByTeamAndSeasonId**

#### **GET** /{version}/{sport}/schedules/seasons/{seasonId}/teams/{teamId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const schedulesByTeamAndSeasonIdResponse =
  await sportmonks.sport.schedulesByTeamAndSeasonId({
    seasonId: 1,
    teamId: 1,
  });

console.log(schedulesByTeamAndSeasonIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve schedule from. | defaults to undefined
 **teamId** | [**number**] | The ID of the team you want to retrieve schedule from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportSchedulesByTeamAndSeasonIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **schedulesByTeamId**

#### **GET** /{version}/{sport}/schedules/teams/{teamId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const schedulesByTeamIdResponse = await sportmonks.sport.schedulesByTeamId({
  teamId: 1,
});

console.log(schedulesByTeamIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | [**number**] | The ID of the team you want to retrieve schedule from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportSchedulesByTeamIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **seasonById**

#### **GET** /{version}/{sport}/seasons/{seasonId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const seasonByIdResponse = await sportmonks.sport.seasonById({
  seasonId: 1,
});

console.log(seasonByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportSeasonByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **seasonsAll**

#### **GET** /{version}/{sport}/seasons


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const seasonsAllResponse = await sportmonks.sport.seasonsAll({});

console.log(seasonsAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportSeasonsAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **seasonsByTeamId**

#### **GET** /{version}/{sport}/seasons/teams/{teamId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const seasonsByTeamIdResponse = await sportmonks.sport.seasonsByTeamId({
  teamId: 1,
});

console.log(seasonsByTeamIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | [**number**] | The ID of the team you want to retrieve seasons from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**object**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **seasonsSearch**

#### **GET** /{version}/{sport}/seasons/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const seasonsSearchResponse = await sportmonks.sport.seasonsSearch({
  name: 1,
});

console.log(seasonsSearchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**number**] | The name you want to search on. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportSeasonsSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **squadsBySeasonAndTeamId**

#### **GET** /{version}/{sport}/squads/seasons/{seasonId}/teams/{teamId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const squadsBySeasonAndTeamIdResponse =
  await sportmonks.sport.squadsBySeasonAndTeamId({
    seasonId: 1,
    teamId: 1,
  });

console.log(squadsBySeasonAndTeamIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve squads from. | defaults to undefined
 **teamId** | [**number**] | The ID of the team you want to retrieve squads from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportSquadsBySeasonAndTeamIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **squadsByTeamId**

#### **GET** /{version}/{sport}/squads/teams/{teamId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const squadsByTeamIdResponse = await sportmonks.sport.squadsByTeamId({
  teamId: 1,
});

console.log(squadsByTeamIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | [**number**] | The ID of the team you want to retrieve squads from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportSquadsByTeamIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **stageById**

#### **GET** /{version}/{sport}/stages/{stageId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const stageByIdResponse = await sportmonks.sport.stageById({
  stageId: 1,
});

console.log(stageByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stageId** | [**number**] | The ID of the stage you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportStageByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **stagesAll**

#### **GET** /{version}/{sport}/stages


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const stagesAllResponse = await sportmonks.sport.stagesAll({});

console.log(stagesAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportStagesAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **stagesBySeasonId**

#### **GET** /{version}/{sport}/stages/seasons/{seasonId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const stagesBySeasonIdResponse = await sportmonks.sport.stagesBySeasonId({
  seasonId: 1,
});

console.log(stagesBySeasonIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve stages from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportStagesBySeasonIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **stagesSearch**

#### **GET** /{version}/{sport}/stages/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const stagesSearchResponse = await sportmonks.sport.stagesSearch({
  name: "name_example",
});

console.log(stagesSearchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**string**] | The name you want to search on. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportStagesSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **standingCorrectionsBySeasonId**

#### **GET** /{version}/{sport}/standings/corrections/seasons/{seasonId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const standingCorrectionsBySeasonIdResponse =
  await sportmonks.sport.standingCorrectionsBySeasonId({
    seasonId: 1,
  });

console.log(standingCorrectionsBySeasonIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve standing corrections from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportStandingCorrectionsBySeasonIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **standingsAll**

#### **GET** /{version}/{sport}/standings


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const standingsAllResponse = await sportmonks.sport.standingsAll({});

console.log(standingsAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportStandingsAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **standingsByRoundId**

#### **GET** /{version}/{sport}/standings/rounds/{roundId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const standingsByRoundIdResponse = await sportmonks.sport.standingsByRoundId({
  roundId: 1,
});

console.log(standingsByRoundIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roundId** | [**number**] | The ID of the round you want to retrieve standing from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportStandingsByRoundIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **standingsBySeasonId**

#### **GET** /{version}/{sport}/standings/seasons/{seasonId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const standingsBySeasonIdResponse = await sportmonks.sport.standingsBySeasonId({
  seasonId: 1,
});

console.log(standingsBySeasonIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve standing from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportStandingsBySeasonIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **standingsLiveByLeagueId**

#### **GET** /{version}/{sport}/standings/live/leagues/{leagueId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const standingsLiveByLeagueIdResponse =
  await sportmonks.sport.standingsLiveByLeagueId({
    leagueId: 1,
  });

console.log(standingsLiveByLeagueIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leagueId** | [**number**] | The ID of the league you want to retrieve standings from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportStandingsLiveByLeagueIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **stateById**

#### **GET** /{version}/{sport}/states/{stateId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const stateByIdResponse = await sportmonks.sport.stateById({
  stateId: 1,
});

console.log(stateByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stateId** | [**number**] | The ID of the state you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportStateByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **statesBySport**

#### **GET** /{version}/{sport}/states


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const statesBySportResponse = await sportmonks.sport.statesBySport({});

console.log(statesBySportResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportStatesBySportResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **teamsAll**

#### **GET** /{version}/{sport}/teams


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const teamsAllResponse = await sportmonks.sport.teamsAll({});

console.log(teamsAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTeamsAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **teamsByCountryId**

#### **GET** /{version}/{sport}/teams/countries/{countryId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const teamsByCountryIdResponse = await sportmonks.sport.teamsByCountryId({
  countryId: 1,
});

console.log(teamsByCountryIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryId** | [**number**] | The ID of the country you want to retrieve teams from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTeamsByCountryIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **teamsById**

#### **GET** /{version}/{sport}/teams/{teamId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const teamsByIdResponse = await sportmonks.sport.teamsById({
  teamId: 1,
});

console.log(teamsByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | [**number**] | The ID of the team you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTeamsByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **teamsBySeasonId**

#### **GET** /{version}/{sport}/teams/seasons/{seasonId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const teamsBySeasonIdResponse = await sportmonks.sport.teamsBySeasonId({
  seasonId: 1,
});

console.log(teamsBySeasonIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve teams from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTeamsBySeasonIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **teamsSearch**

#### **GET** /{version}/{sport}/teams/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const teamsSearchResponse = await sportmonks.sport.teamsSearch({
  name: "name_example",
});

console.log(teamsSearchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**string**] | The name you want to search on. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTeamsSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **topScorersBySeasonId**

#### **GET** /{version}/{sport}/topscorers/seasons/{seasonId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const topScorersBySeasonIdResponse =
  await sportmonks.sport.topScorersBySeasonId({
    seasonId: 1,
  });

console.log(topScorersBySeasonIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve topscorers from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTopScorersBySeasonIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **topScorersByStageId**

#### **GET** /{version}/{sport}/topscorers/stages/{stageId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const topScorersByStageIdResponse = await sportmonks.sport.topScorersByStageId({
  stageId: 1,
});

console.log(topScorersByStageIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stageId** | [**number**] | The ID of the stage you want to retrieve topscorers from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTopScorersByStageIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **tranfersByDateRange**

#### **GET** /{version}/{sport}/transfers/between/{startDate}/{endDate}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const tranfersByDateRangeResponse = await sportmonks.sport.tranfersByDateRange({
  startDate: "startDate_example",
  endDate: "endDate_example",
});

console.log(tranfersByDateRangeResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startDate** | [**string**] | The start date you want to retrieve transfers from. | defaults to undefined
 **endDate** | [**string**] | The end date you want to retrieve transfers from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTranfersByDateRangeResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **transferById**

#### **GET** /{version}/{sport}/transfers/{transferId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const transferByIdResponse = await sportmonks.sport.transferById({
  transferId: 1,
});

console.log(transferByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transferId** | [**number**] |  | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTransferByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Date -  <br>  * Server -  <br>  * Cache-Control -  <br>  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * Vary -  <br>  * Content-Encoding -  <br>  * X-Robots-Tag -  <br>  * Content-Length -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **transfersAll**

#### **GET** /{version}/{sport}/transfers


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const transfersAllResponse = await sportmonks.sport.transfersAll({});

console.log(transfersAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTransfersAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **transfersByPlayerId**

#### **GET** /{version}/{sport}/transfers/players/{playerId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const transfersByPlayerIdResponse = await sportmonks.sport.transfersByPlayerId({
  playerId: 1,
});

console.log(transfersByPlayerIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playerId** | [**number**] | The ID of the player you want to retrieve transfers from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTransfersByPlayerIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **transfersByTeamId**

#### **GET** /{version}/{sport}/transfers/teams/{teamId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const transfersByTeamIdResponse = await sportmonks.sport.transfersByTeamId({
  teamId: 1,
});

console.log(transfersByTeamIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | [**number**] | The ID of the team you want to retrieve transfers from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTransfersByTeamIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **transfersLatest**

#### **GET** /{version}/{sport}/transfers/latest


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const transfersLatestResponse = await sportmonks.sport.transfersLatest({});

console.log(transfersLatestResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTransfersLatestResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **tvStationById**

#### **GET** /{version}/{sport}/tv-stations/{tvStationId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const tvStationByIdResponse = await sportmonks.sport.tvStationById({
  tvStationId: 1,
});

console.log(tvStationByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tvStationId** | [**number**] | The ID of the tv station you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTvStationByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **tvStationsAll**

#### **GET** /{version}/{sport}/tv-stations


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const tvStationsAllResponse = await sportmonks.sport.tvStationsAll({});

console.log(tvStationsAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTvStationsAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **tvStationsByFixtureId**

#### **GET** /{version}/{sport}/tv-stations/fixtures/{fixtureId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const tvStationsByFixtureIdResponse =
  await sportmonks.sport.tvStationsByFixtureId({
    fixtureId: 1,
  });

console.log(tvStationsByFixtureIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixtureId** | [**number**] | The ID of the fixture you want to retrieve tv-stations from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportTvStationsByFixtureIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **venueById**

#### **GET** /{version}/{sport}/venues/{venueId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const venueByIdResponse = await sportmonks.sport.venueById({
  venueId: 1,
});

console.log(venueByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **venueId** | [**number**] | The ID of the venue you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportVenueByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **venuesAll**

#### **GET** /{version}/{sport}/venues


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const venuesAllResponse = await sportmonks.sport.venuesAll({});

console.log(venuesAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportVenuesAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **venuesBySeasonId**

#### **GET** /{version}/{sport}/venues/seasons/{seasonId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const venuesBySeasonIdResponse = await sportmonks.sport.venuesBySeasonId({
  seasonId: 1,
});

console.log(venuesBySeasonIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seasonId** | [**number**] | The ID of the season you want to retrieve venues from. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportVenuesBySeasonIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **venuesSearch**

#### **GET** /{version}/{sport}/venues/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const venuesSearchResponse = await sportmonks.sport.venuesSearch({
  name: "name_example",
});

console.log(venuesSearchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**string**] | The name you want to search on. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined
 **sport** | [**string**] | The sport you want retrieve entities from. | (optional) defaults to undefined


### Return type

**SportVenuesSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


