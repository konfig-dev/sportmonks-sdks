# sportmonks@1.0.0

Surpass the competition with superior sports data
## Installing

### npm
```
npm install sportmonks --save
```

### yarn
```
yarn add sportmonks
```

**Important note: this library can be used in both the client-side or server-side, but using it
in client-side browser code is not recommended as you would expose security credentials.**



## Getting Started

```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "version",
  sport: "sport",
  apiKey: "API_KEY",
});

const allResponse = await sportmonks.cities.all({});

console.log(allResponse);
```

## Documentation for API Endpoints

All URIs are relative to *https://api.sportmonks.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CitiesApi* | [**all**](docs/CitiesApi.md#all) | **GET** /{version}/core/cities | All
*CitiesApi* | [**getById**](docs/CitiesApi.md#getById) | **GET** /{version}/core/cities/{cityId} | By ID
*CitiesApi* | [**search**](docs/CitiesApi.md#search) | **GET** /{version}/core/cities/search/{name} | Search
*ContinentsApi* | [**all**](docs/ContinentsApi.md#all) | **GET** /{version}/core/continents | All
*ContinentsApi* | [**getById**](docs/ContinentsApi.md#getById) | **GET** /{version}/core/continents/{continentId} | By ID
*CountriesApi* | [**all**](docs/CountriesApi.md#all) | **GET** /{version}/core/countries | All
*CountriesApi* | [**getById**](docs/CountriesApi.md#getById) | **GET** /{version}/core/countries/{countryId} | By ID
*CountriesApi* | [**search**](docs/CountriesApi.md#search) | **GET** /{version}/core/countries/search/{name} | Search
*MyApi* | [**enrichments**](docs/MyApi.md#enrichments) | **GET** /{version}/my/enrichments | All
*MyApi* | [**leagues**](docs/MyApi.md#leagues) | **GET** /{version}/my/leagues | All
*MyApi* | [**resources**](docs/MyApi.md#resources) | **GET** /{version}/my/resources | All
*OddsApi* | [**bookmakerById**](docs/OddsApi.md#bookmakerById) | **GET** /{version}/odds/bookmakers/{bookmakerId} | By ID
*OddsApi* | [**bookmakersAll**](docs/OddsApi.md#bookmakersAll) | **GET** /{version}/odds/bookmakers | All
*OddsApi* | [**bookmakersByFixtureId**](docs/OddsApi.md#bookmakersByFixtureId) | **GET** /{version}/odds/bookmakers/fixtures/{fixtureId} | By Fixture ID
*OddsApi* | [**bookmakersMappingByFixtureId**](docs/OddsApi.md#bookmakersMappingByFixtureId) | **GET** /{version}/odds/bookmakers/fixtures/{fixtureId}/mapping | Mapping by Fixture ID
*OddsApi* | [**bookmakersSearch**](docs/OddsApi.md#bookmakersSearch) | **GET** /{version}/odds/bookmakers/search/{name} | Search
*OddsApi* | [**fixturesUpcomingByMarketId**](docs/OddsApi.md#fixturesUpcomingByMarketId) | **GET** /{version}/{sport}/fixtures/upcoming/markets/{marketId} | Upcoming Fixtures by Market ID
*OddsApi* | [**marketById**](docs/OddsApi.md#marketById) | **GET** /{version}/odds/markets/{marketId} | By ID
*OddsApi* | [**marketsAll**](docs/OddsApi.md#marketsAll) | **GET** /{version}/odds/markets | All
*OddsApi* | [**marketsSearch**](docs/OddsApi.md#marketsSearch) | **GET** /{version}/odds/markets/search/{name} | Search
*RegionsApi* | [**all**](docs/RegionsApi.md#all) | **GET** /{version}/core/regions | All
*RegionsApi* | [**getById**](docs/RegionsApi.md#getById) | **GET** /{version}/core/regions/{regionId} | By ID
*RegionsApi* | [**search**](docs/RegionsApi.md#search) | **GET** /{version}/core/regions/search/{name} | Search
*SportApi* | [**coachById**](docs/SportApi.md#coachById) | **GET** /{version}/{sport}/coaches/{coachId} | By ID
*SportApi* | [**coachesAll**](docs/SportApi.md#coachesAll) | **GET** /{version}/{sport}/coaches | All
*SportApi* | [**coachesByCountryId**](docs/SportApi.md#coachesByCountryId) | **GET** /{version}/{sport}/coaches/countries/{countryId} | By Country ID
*SportApi* | [**coachesLatest**](docs/SportApi.md#coachesLatest) | **GET** /{version}/{sport}/coaches/latest | Last updated
*SportApi* | [**coachesSearch**](docs/SportApi.md#coachesSearch) | **GET** /{version}/{sport}/coaches/search/{name} | Search
*SportApi* | [**commentariesAll**](docs/SportApi.md#commentariesAll) | **GET** /{version}/{sport}/commentaries | All
*SportApi* | [**commentariesByFixtureId**](docs/SportApi.md#commentariesByFixtureId) | **GET** /{version}/{sport}/commentaries/fixtures/{fixtureId} | By Fixture ID
*SportApi* | [**fixtureByDateRangeForTeam**](docs/SportApi.md#fixtureByDateRangeForTeam) | **GET** /{version}/{sport}/fixtures/between/{startDate}/{endDate}/{teamId} | By Date Range for Team
*SportApi* | [**fixtureById**](docs/SportApi.md#fixtureById) | **GET** /{version}/{sport}/fixtures/{fixtureId} | Fixture ID
*SportApi* | [**fixturesAll**](docs/SportApi.md#fixturesAll) | **GET** /{version}/{sport}/fixtures | All
*SportApi* | [**fixturesByDate**](docs/SportApi.md#fixturesByDate) | **GET** /{version}/{sport}/fixtures/date/{date} | By Date
*SportApi* | [**fixturesByDateRange**](docs/SportApi.md#fixturesByDateRange) | **GET** /{version}/{sport}/fixtures/between/{startDate}/{endDate} | By Date Range
*SportApi* | [**fixturesByIds**](docs/SportApi.md#fixturesByIds) | **GET** /{version}/{sport}/fixtures/multi/{fixtureIds} | By IDs
*SportApi* | [**fixturesHeadToHead**](docs/SportApi.md#fixturesHeadToHead) | **GET** /{version}/{sport}/fixtures/head-to-head/{firstTeam}/{secondTeam} | Head to Head
*SportApi* | [**fixturesLatest**](docs/SportApi.md#fixturesLatest) | **GET** /{version}/{sport}/fixtures/latest | Last Updated
*SportApi* | [**fixturesSearch**](docs/SportApi.md#fixturesSearch) | **GET** /{version}/{sport}/fixtures/search/{name} | Search
*SportApi* | [**leagueById**](docs/SportApi.md#leagueById) | **GET** /{version}/{sport}/leagues/{leagueId} | By ID
*SportApi* | [**leagueEnrichments**](docs/SportApi.md#leagueEnrichments) | **GET** /{version}/{sport}/leagues/{leagueId}/includes | Enrichments
*SportApi* | [**leagueShirts**](docs/SportApi.md#leagueShirts) | **GET** /{version}/{sport}/leagues/{leagueId}/jerseys | Shirts By League ID
*SportApi* | [**leaguesAll**](docs/SportApi.md#leaguesAll) | **GET** /{version}/{sport}/leagues | All
*SportApi* | [**leaguesByCountryId**](docs/SportApi.md#leaguesByCountryId) | **GET** /{version}/{sport}/leagues/countries/{countryId} | By Country ID
*SportApi* | [**leaguesByDate**](docs/SportApi.md#leaguesByDate) | **GET** /{version}/{sport}/leagues/date/{date} | By Date
*SportApi* | [**leaguesByTeamId**](docs/SportApi.md#leaguesByTeamId) | **GET** /{version}/{sport}/teams/{teamId}/leagues | Leagues By Team ID
*SportApi* | [**leaguesCurrentByTeamId**](docs/SportApi.md#leaguesCurrentByTeamId) | **GET** /{version}/{sport}/teams/{teamId}/leagues/current | Current Leagues By Team ID
*SportApi* | [**leaguesLive**](docs/SportApi.md#leaguesLive) | **GET** /{version}/{sport}/leagues/live | Live
*SportApi* | [**leaguesSearch**](docs/SportApi.md#leaguesSearch) | **GET** /{version}/{sport}/leagues/search/{name} | Search
*SportApi* | [**livescoresAll**](docs/SportApi.md#livescoresAll) | **GET** /{version}/{sport}/livescores | All
*SportApi* | [**livescoresAllInPlay**](docs/SportApi.md#livescoresAllInPlay) | **GET** /{version}/{sport}/livescores/inplay | All In-play
*SportApi* | [**livescoresLatest**](docs/SportApi.md#livescoresLatest) | **GET** /{version}/{sport}/livescores/latest | Last Updated In-play
*SportApi* | [**newsAllPostMatch**](docs/SportApi.md#newsAllPostMatch) | **GET** /{version}/{sport}/news/post-match | All Post Match
*SportApi* | [**newsAllPreMatch**](docs/SportApi.md#newsAllPreMatch) | **GET** /{version}/{sport}/news/pre-match | All Pre-match
*SportApi* | [**newsPostMatchBySeasonId**](docs/SportApi.md#newsPostMatchBySeasonId) | **GET** /{version}/{sport}/news/post-match/seasons/{seasonId} | Post Match by Season ID
*SportApi* | [**newsPreMatchBySeasonId**](docs/SportApi.md#newsPreMatchBySeasonId) | **GET** /{version}/{sport}/news/pre-match/seasons/{seasonId} | Pre-match By Season ID
*SportApi* | [**newsUpcomingPostMatch**](docs/SportApi.md#newsUpcomingPostMatch) | **GET** /{version}/{sport}/news/post-match/upcoming | Upcoming Post Match
*SportApi* | [**newsUpcomingPreMatch**](docs/SportApi.md#newsUpcomingPreMatch) | **GET** /{version}/{sport}/news/pre-match/upcoming | Upcoming Pre-match
*SportApi* | [**oddsAllInPlay**](docs/SportApi.md#oddsAllInPlay) | **GET** /{version}/{sport}/odds/inplay | All In-play
*SportApi* | [**oddsAllPreMatch**](docs/SportApi.md#oddsAllPreMatch) | **GET** /{version}/{sport}/odds/pre-match | All Pre-match
*SportApi* | [**oddsInPlayByFixtureAndBookmakerId**](docs/SportApi.md#oddsInPlayByFixtureAndBookmakerId) | **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}/bookmakers/{bookmakerId} | In-play by Fixture and Bookmaker ID
*SportApi* | [**oddsInPlayByFixtureAndMarketId**](docs/SportApi.md#oddsInPlayByFixtureAndMarketId) | **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId}/markets/{marketId} | In-play by Fixture and Market ID
*SportApi* | [**oddsInPlayByFixtureId**](docs/SportApi.md#oddsInPlayByFixtureId) | **GET** /{version}/{sport}/odds/inplay/fixtures/{fixtureId} | In-play by Fixture ID
*SportApi* | [**oddsLatestInPlay**](docs/SportApi.md#oddsLatestInPlay) | **GET** /{version}/{sport}/odds/inplay/latest | Latest In-play
*SportApi* | [**oddsLatestPreMatch**](docs/SportApi.md#oddsLatestPreMatch) | **GET** /{version}/{sport}/odds/pre-match/latest | Last Updated Pre-match
*SportApi* | [**oddsPreMatchByFixtureAndBookmakerId**](docs/SportApi.md#oddsPreMatchByFixtureAndBookmakerId) | **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}/bookmakers/{bookmakerId} | Pre-match by Fixture and Bookmaker ID
*SportApi* | [**oddsPreMatchByFixtureAndMarketId**](docs/SportApi.md#oddsPreMatchByFixtureAndMarketId) | **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId}/markets/{marketId} | Pre-match by Fixture and Market ID
*SportApi* | [**oddsPreMatchByFixtureId**](docs/SportApi.md#oddsPreMatchByFixtureId) | **GET** /{version}/{sport}/odds/pre-match/fixtures/{fixtureId} | Pre-match by Fixture ID
*SportApi* | [**playerById**](docs/SportApi.md#playerById) | **GET** /{version}/{sport}/players/{playerId} | By ID
*SportApi* | [**playersAll**](docs/SportApi.md#playersAll) | **GET** /{version}/{sport}/players | All
*SportApi* | [**playersByCountryId**](docs/SportApi.md#playersByCountryId) | **GET** /{version}/{sport}/players/countries/{countryId} | By Country ID
*SportApi* | [**playersLatest**](docs/SportApi.md#playersLatest) | **GET** /{version}/{sport}/players/latest | Latest Updated
*SportApi* | [**playersSearch**](docs/SportApi.md#playersSearch) | **GET** /{version}/{sport}/players/search/{name} | Search
*SportApi* | [**predictionsAll**](docs/SportApi.md#predictionsAll) | **GET** /{version}/{sport}/predictions/probabilities | All
*SportApi* | [**predictionsAllValueBets**](docs/SportApi.md#predictionsAllValueBets) | **GET** /{version}/{sport}/predictions/value-bets | All Value Bets
*SportApi* | [**predictionsByFixtureId**](docs/SportApi.md#predictionsByFixtureId) | **GET** /{version}/{sport}/predictions/probabilities/fixtures/{fixtureId} | By Fixture ID
*SportApi* | [**predictionsValueBetsByFixtureId**](docs/SportApi.md#predictionsValueBetsByFixtureId) | **GET** /{version}/{sport}/predictions/value-bets/fixtures/{fixtureId} | Value Bets by Fixture ID
*SportApi* | [**refereeById**](docs/SportApi.md#refereeById) | **GET** /{version}/{sport}/referees/{refereeId} | By ID
*SportApi* | [**refereesAll**](docs/SportApi.md#refereesAll) | **GET** /{version}/{sport}/referees | All
*SportApi* | [**refereesByCountryId**](docs/SportApi.md#refereesByCountryId) | **GET** /{version}/{sport}/referees/countries/{countryId} | By Country ID
*SportApi* | [**refereesBySeasonId**](docs/SportApi.md#refereesBySeasonId) | **GET** /{version}/{sport}/referees/seasons/{seasonId} | By Season ID
*SportApi* | [**refereesSearch**](docs/SportApi.md#refereesSearch) | **GET** /{version}/{sport}/referees/search/{name} | Search
*SportApi* | [**rivalsAll**](docs/SportApi.md#rivalsAll) | **GET** /{version}/{sport}/rivals | All
*SportApi* | [**rivalsByTeamId**](docs/SportApi.md#rivalsByTeamId) | **GET** /{version}/{sport}/rivals/teams/{teamId} | By Team ID
*SportApi* | [**roundById**](docs/SportApi.md#roundById) | **GET** /{version}/{sport}/rounds/{roundId} | By ID
*SportApi* | [**roundsAll**](docs/SportApi.md#roundsAll) | **GET** /{version}/{sport}/rounds | All
*SportApi* | [**roundsBySeasonId**](docs/SportApi.md#roundsBySeasonId) | **GET** /{version}/{sport}/rounds/seasons/{seasonId} | Season ID
*SportApi* | [**roundsSearch**](docs/SportApi.md#roundsSearch) | **GET** /{version}/{sport}/rounds/search/{name} | Search
*SportApi* | [**schedulesBySeasonId**](docs/SportApi.md#schedulesBySeasonId) | **GET** /{version}/{sport}/schedules/seasons/{seasonId} | By Season ID
*SportApi* | [**schedulesByTeamAndSeasonId**](docs/SportApi.md#schedulesByTeamAndSeasonId) | **GET** /{version}/{sport}/schedules/seasons/{seasonId}/teams/{teamId} | By Team and Season ID
*SportApi* | [**schedulesByTeamId**](docs/SportApi.md#schedulesByTeamId) | **GET** /{version}/{sport}/schedules/teams/{teamId} | By Team ID
*SportApi* | [**seasonById**](docs/SportApi.md#seasonById) | **GET** /{version}/{sport}/seasons/{seasonId} | By ID
*SportApi* | [**seasonsAll**](docs/SportApi.md#seasonsAll) | **GET** /{version}/{sport}/seasons | All
*SportApi* | [**seasonsByTeamId**](docs/SportApi.md#seasonsByTeamId) | **GET** /{version}/{sport}/seasons/teams/{teamId} | By Team ID
*SportApi* | [**seasonsSearch**](docs/SportApi.md#seasonsSearch) | **GET** /{version}/{sport}/seasons/search/{name} | Search
*SportApi* | [**squadsBySeasonAndTeamId**](docs/SportApi.md#squadsBySeasonAndTeamId) | **GET** /{version}/{sport}/squads/seasons/{seasonId}/teams/{teamId} | By Season and Team ID
*SportApi* | [**squadsByTeamId**](docs/SportApi.md#squadsByTeamId) | **GET** /{version}/{sport}/squads/teams/{teamId} | By Team ID
*SportApi* | [**stageById**](docs/SportApi.md#stageById) | **GET** /{version}/{sport}/stages/{stageId} | By ID
*SportApi* | [**stagesAll**](docs/SportApi.md#stagesAll) | **GET** /{version}/{sport}/stages | All
*SportApi* | [**stagesBySeasonId**](docs/SportApi.md#stagesBySeasonId) | **GET** /{version}/{sport}/stages/seasons/{seasonId} | By Season ID
*SportApi* | [**stagesSearch**](docs/SportApi.md#stagesSearch) | **GET** /{version}/{sport}/stages/search/{name} | Search
*SportApi* | [**standingCorrectionsBySeasonId**](docs/SportApi.md#standingCorrectionsBySeasonId) | **GET** /{version}/{sport}/standings/corrections/seasons/{seasonId} | Correction by Season ID
*SportApi* | [**standingsAll**](docs/SportApi.md#standingsAll) | **GET** /{version}/{sport}/standings | All
*SportApi* | [**standingsByRoundId**](docs/SportApi.md#standingsByRoundId) | **GET** /{version}/{sport}/standings/rounds/{roundId} | By Round ID
*SportApi* | [**standingsBySeasonId**](docs/SportApi.md#standingsBySeasonId) | **GET** /{version}/{sport}/standings/seasons/{seasonId} | By Season ID
*SportApi* | [**standingsLiveByLeagueId**](docs/SportApi.md#standingsLiveByLeagueId) | **GET** /{version}/{sport}/standings/live/leagues/{leagueId} | By League ID
*SportApi* | [**stateById**](docs/SportApi.md#stateById) | **GET** /{version}/{sport}/states/{stateId} | By ID
*SportApi* | [**statesBySport**](docs/SportApi.md#statesBySport) | **GET** /{version}/{sport}/states | By Sport
*SportApi* | [**teamsAll**](docs/SportApi.md#teamsAll) | **GET** /{version}/{sport}/teams | All
*SportApi* | [**teamsByCountryId**](docs/SportApi.md#teamsByCountryId) | **GET** /{version}/{sport}/teams/countries/{countryId} | By Country ID
*SportApi* | [**teamsById**](docs/SportApi.md#teamsById) | **GET** /{version}/{sport}/teams/{teamId} | By ID
*SportApi* | [**teamsBySeasonId**](docs/SportApi.md#teamsBySeasonId) | **GET** /{version}/{sport}/teams/seasons/{seasonId} | By Season ID
*SportApi* | [**teamsSearch**](docs/SportApi.md#teamsSearch) | **GET** /{version}/{sport}/teams/search/{name} | Search
*SportApi* | [**topScorersBySeasonId**](docs/SportApi.md#topScorersBySeasonId) | **GET** /{version}/{sport}/topscorers/seasons/{seasonId} | By Season ID
*SportApi* | [**topScorersByStageId**](docs/SportApi.md#topScorersByStageId) | **GET** /{version}/{sport}/topscorers/stages/{stageId} | By Stage ID
*SportApi* | [**tranfersByDateRange**](docs/SportApi.md#tranfersByDateRange) | **GET** /{version}/{sport}/transfers/between/{startDate}/{endDate} | By Date Range
*SportApi* | [**transferById**](docs/SportApi.md#transferById) | **GET** /{version}/{sport}/transfers/{transferId} | By ID
*SportApi* | [**transfersAll**](docs/SportApi.md#transfersAll) | **GET** /{version}/{sport}/transfers | All
*SportApi* | [**transfersByPlayerId**](docs/SportApi.md#transfersByPlayerId) | **GET** /{version}/{sport}/transfers/players/{playerId} | By Player ID
*SportApi* | [**transfersByTeamId**](docs/SportApi.md#transfersByTeamId) | **GET** /{version}/{sport}/transfers/teams/{teamId} | By Team ID
*SportApi* | [**transfersLatest**](docs/SportApi.md#transfersLatest) | **GET** /{version}/{sport}/transfers/latest | Last Updated
*SportApi* | [**tvStationById**](docs/SportApi.md#tvStationById) | **GET** /{version}/{sport}/tv-stations/{tvStationId} | By ID
*SportApi* | [**tvStationsAll**](docs/SportApi.md#tvStationsAll) | **GET** /{version}/{sport}/tv-stations | All
*SportApi* | [**tvStationsByFixtureId**](docs/SportApi.md#tvStationsByFixtureId) | **GET** /{version}/{sport}/tv-stations/fixtures/{fixtureId} | By Fixture ID
*SportApi* | [**venueById**](docs/SportApi.md#venueById) | **GET** /{version}/{sport}/venues/{venueId} | By ID
*SportApi* | [**venuesAll**](docs/SportApi.md#venuesAll) | **GET** /{version}/{sport}/venues | All
*SportApi* | [**venuesBySeasonId**](docs/SportApi.md#venuesBySeasonId) | **GET** /{version}/{sport}/venues/seasons/{seasonId} | By Season ID
*SportApi* | [**venuesSearch**](docs/SportApi.md#venuesSearch) | **GET** /{version}/{sport}/venues/search/{name} | Search
*TypesApi* | [**all**](docs/TypesApi.md#all) | **GET** /{version}/core/types | All
*TypesApi* | [**getById**](docs/TypesApi.md#getById) | **GET** /{version}/core/types/{typeId} | By ID

