# OddsApi

All URIs are relative to *https://api.sportmonks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookmakerById**](OddsApi.md#bookmakerById) | **GET** /{version}/odds/bookmakers/{bookmakerId} | By ID
[**bookmakersAll**](OddsApi.md#bookmakersAll) | **GET** /{version}/odds/bookmakers | All
[**bookmakersByFixtureId**](OddsApi.md#bookmakersByFixtureId) | **GET** /{version}/odds/bookmakers/fixtures/{fixtureId} | By Fixture ID
[**bookmakersMappingByFixtureId**](OddsApi.md#bookmakersMappingByFixtureId) | **GET** /{version}/odds/bookmakers/fixtures/{fixtureId}/mapping | Mapping by Fixture ID
[**bookmakersSearch**](OddsApi.md#bookmakersSearch) | **GET** /{version}/odds/bookmakers/search/{name} | Search
[**fixturesUpcomingByMarketId**](OddsApi.md#fixturesUpcomingByMarketId) | **GET** /{version}/{sport}/fixtures/upcoming/markets/{marketId} | Upcoming Fixtures by Market ID
[**marketById**](OddsApi.md#marketById) | **GET** /{version}/odds/markets/{marketId} | By ID
[**marketsAll**](OddsApi.md#marketsAll) | **GET** /{version}/odds/markets | All
[**marketsSearch**](OddsApi.md#marketsSearch) | **GET** /{version}/odds/markets/search/{name} | Search


# **bookmakerById**

#### **GET** /{version}/odds/bookmakers/{bookmakerId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
});

const bookmakerByIdResponse = await sportmonks.odds.bookmakerById({
  version: "version_example",
  bookmakerId: 1,
});

console.log(bookmakerByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | defaults to undefined
 **bookmakerId** | [**number**] | The ID of the bookmaker you want to retrieve. | defaults to undefined


### Return type

**OddsBookmakerByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **bookmakersAll**

#### **GET** /{version}/odds/bookmakers


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
});

const bookmakersAllResponse = await sportmonks.odds.bookmakersAll({
  version: "version_example",
});

console.log(bookmakersAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | defaults to undefined


### Return type

**OddsBookmakersAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **bookmakersByFixtureId**

#### **GET** /{version}/odds/bookmakers/fixtures/{fixtureId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
});

const bookmakersByFixtureIdResponse =
  await sportmonks.odds.bookmakersByFixtureId({
    version: "version_example",
    fixtureId: 1,
  });

console.log(bookmakersByFixtureIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | defaults to undefined
 **fixtureId** | [**number**] | The ID of the bookmaker you want to retrieve. | defaults to undefined


### Return type

**OddsBookmakersByFixtureIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **bookmakersMappingByFixtureId**

#### **GET** /{version}/odds/bookmakers/fixtures/{fixtureId}/mapping


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
});

const bookmakersMappingByFixtureIdResponse =
  await sportmonks.odds.bookmakersMappingByFixtureId({
    version: "version_example",
    fixtureId: 1,
  });

console.log(bookmakersMappingByFixtureIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | defaults to undefined
 **fixtureId** | [**number**] | The fixtureId you want to retrieve the bookmaker mapping from. | defaults to undefined


### Return type

**OddsBookmakersMappingByFixtureIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **bookmakersSearch**

#### **GET** /{version}/odds/bookmakers/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
});

const bookmakersSearchResponse = await sportmonks.odds.bookmakersSearch({
  version: "version_example",
  name: "name_example",
});

console.log(bookmakersSearchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | defaults to undefined
 **name** | [**string**] | The name you want to search on | defaults to undefined


### Return type

**OddsBookmakersSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **fixturesUpcomingByMarketId**

#### **GET** /{version}/{sport}/fixtures/upcoming/markets/{marketId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
});

const fixturesUpcomingByMarketIdResponse =
  await sportmonks.odds.fixturesUpcomingByMarketId({
    version: "version_example",
    sport: "sport_example",
    marketId: 1,
  });

console.log(fixturesUpcomingByMarketIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The sport you want to retrieve upcoming fixtures from. | defaults to undefined
 **sport** | [**string**] |  | defaults to undefined
 **marketId** | [**number**] | The ID of the market you want to retrieve upcoming fixtures from. | defaults to undefined


### Return type

**OddsFixturesUpcomingByMarketIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **marketById**

#### **GET** /{version}/odds/markets/{marketId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
});

const marketByIdResponse = await sportmonks.odds.marketById({
  version: "version_example",
  marketId: 1,
});

console.log(marketByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | defaults to undefined
 **marketId** | [**number**] | The ID of the market you want to retrieve. | defaults to undefined


### Return type

**OddsMarketByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **marketsAll**

#### **GET** /{version}/odds/markets


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
});

const marketsAllResponse = await sportmonks.odds.marketsAll({
  version: "version_example",
});

console.log(marketsAllResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | defaults to undefined


### Return type

**OddsMarketsAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **marketsSearch**

#### **GET** /{version}/odds/markets/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
});

const marketsSearchResponse = await sportmonks.odds.marketsSearch({
  version: "version_example",
  name: "name_example",
});

console.log(marketsSearchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | defaults to undefined
 **name** | [**string**] | The name you want to search on | defaults to undefined


### Return type

**OddsMarketsSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


