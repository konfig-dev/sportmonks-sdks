# Sportmonks.Net.Api.OddsApi

All URIs are relative to *https://api.sportmonks.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**BookmakerById**](OddsApi.md#bookmakerbyid) | **GET** /{version}/odds/bookmakers/{bookmakerId} | By ID |
| [**BookmakersAll**](OddsApi.md#bookmakersall) | **GET** /{version}/odds/bookmakers | All |
| [**BookmakersByFixtureId**](OddsApi.md#bookmakersbyfixtureid) | **GET** /{version}/odds/bookmakers/fixtures/{fixtureId} | By Fixture ID |
| [**BookmakersMappingByFixtureId**](OddsApi.md#bookmakersmappingbyfixtureid) | **GET** /{version}/odds/bookmakers/fixtures/{fixtureId}/mapping | Mapping by Fixture ID |
| [**BookmakersSearch**](OddsApi.md#bookmakerssearch) | **GET** /{version}/odds/bookmakers/search/{name} | Search |
| [**FixturesUpcomingByMarketId**](OddsApi.md#fixturesupcomingbymarketid) | **GET** /{version}/{sport}/fixtures/upcoming/markets/{marketId} | Upcoming Fixtures by Market ID |
| [**MarketById**](OddsApi.md#marketbyid) | **GET** /{version}/odds/markets/{marketId} | By ID |
| [**MarketsAll**](OddsApi.md#marketsall) | **GET** /{version}/odds/markets | All |
| [**MarketsSearch**](OddsApi.md#marketssearch) | **GET** /{version}/odds/markets/search/{name} | Search |

<a name="bookmakerbyid"></a>
# **BookmakerById**
> OddsBookmakerByIdResponse BookmakerById (string version, int bookmakerId)

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
    public class BookmakerByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new OddsApi(config);
            var version = v3;  // string | The version of the API.
            var bookmakerId = 1;  // int | The ID of the bookmaker you want to retrieve.

            try
            {
                // By ID
                OddsBookmakerByIdResponse result = apiInstance.BookmakerById(version, bookmakerId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling OddsApi.BookmakerById: " + e.Message);
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

#### Using the BookmakerByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<OddsBookmakerByIdResponse> response = apiInstance.BookmakerByIdWithHttpInfo(version, bookmakerId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OddsApi.BookmakerByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **bookmakerId** | **int** | The ID of the bookmaker you want to retrieve. |  |

### Return type

[**OddsBookmakerByIdResponse**](OddsBookmakerByIdResponse.md)

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

<a name="bookmakersall"></a>
# **BookmakersAll**
> OddsBookmakersAllResponse BookmakersAll (string version)

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
    public class BookmakersAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new OddsApi(config);
            var version = v3;  // string | The version of the API.

            try
            {
                // All
                OddsBookmakersAllResponse result = apiInstance.BookmakersAll(version);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling OddsApi.BookmakersAll: " + e.Message);
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

#### Using the BookmakersAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<OddsBookmakersAllResponse> response = apiInstance.BookmakersAllWithHttpInfo(version);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OddsApi.BookmakersAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |

### Return type

[**OddsBookmakersAllResponse**](OddsBookmakersAllResponse.md)

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

<a name="bookmakersbyfixtureid"></a>
# **BookmakersByFixtureId**
> OddsBookmakersByFixtureIdResponse BookmakersByFixtureId (string version, int fixtureId)

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
    public class BookmakersByFixtureIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new OddsApi(config);
            var version = v3;  // string | The version of the API.
            var fixtureId = 18528479;  // int | The ID of the bookmaker you want to retrieve.

            try
            {
                // By Fixture ID
                OddsBookmakersByFixtureIdResponse result = apiInstance.BookmakersByFixtureId(version, fixtureId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling OddsApi.BookmakersByFixtureId: " + e.Message);
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

#### Using the BookmakersByFixtureIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By Fixture ID
    ApiResponse<OddsBookmakersByFixtureIdResponse> response = apiInstance.BookmakersByFixtureIdWithHttpInfo(version, fixtureId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OddsApi.BookmakersByFixtureIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **fixtureId** | **int** | The ID of the bookmaker you want to retrieve. |  |

### Return type

[**OddsBookmakersByFixtureIdResponse**](OddsBookmakersByFixtureIdResponse.md)

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

<a name="bookmakersmappingbyfixtureid"></a>
# **BookmakersMappingByFixtureId**
> OddsBookmakersMappingByFixtureIdResponse BookmakersMappingByFixtureId (string version, int fixtureId)

Mapping by Fixture ID

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
    public class BookmakersMappingByFixtureIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new OddsApi(config);
            var version = v3;  // string | The version of the API.
            var fixtureId = 18528479;  // int | The fixtureId you want to retrieve the bookmaker mapping from.

            try
            {
                // Mapping by Fixture ID
                OddsBookmakersMappingByFixtureIdResponse result = apiInstance.BookmakersMappingByFixtureId(version, fixtureId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling OddsApi.BookmakersMappingByFixtureId: " + e.Message);
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

#### Using the BookmakersMappingByFixtureIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Mapping by Fixture ID
    ApiResponse<OddsBookmakersMappingByFixtureIdResponse> response = apiInstance.BookmakersMappingByFixtureIdWithHttpInfo(version, fixtureId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OddsApi.BookmakersMappingByFixtureIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **fixtureId** | **int** | The fixtureId you want to retrieve the bookmaker mapping from. |  |

### Return type

[**OddsBookmakersMappingByFixtureIdResponse**](OddsBookmakersMappingByFixtureIdResponse.md)

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

<a name="bookmakerssearch"></a>
# **BookmakersSearch**
> OddsBookmakersSearchResponse BookmakersSearch (string version, string name)

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
    public class BookmakersSearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new OddsApi(config);
            var version = v3;  // string | The version of the API.
            var name = Bet;  // string | The name you want to search on

            try
            {
                // Search
                OddsBookmakersSearchResponse result = apiInstance.BookmakersSearch(version, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling OddsApi.BookmakersSearch: " + e.Message);
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

#### Using the BookmakersSearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<OddsBookmakersSearchResponse> response = apiInstance.BookmakersSearchWithHttpInfo(version, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OddsApi.BookmakersSearchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **name** | **string** | The name you want to search on |  |

### Return type

[**OddsBookmakersSearchResponse**](OddsBookmakersSearchResponse.md)

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

<a name="fixturesupcomingbymarketid"></a>
# **FixturesUpcomingByMarketId**
> OddsFixturesUpcomingByMarketIdResponse FixturesUpcomingByMarketId (string version, string sport, int marketId)

Upcoming Fixtures by Market ID

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
    public class FixturesUpcomingByMarketIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new OddsApi(config);
            var version = v3;  // string | The sport you want to retrieve upcoming fixtures from.
            var sport = football;  // string | 
            var marketId = 1;  // int | The ID of the market you want to retrieve upcoming fixtures from.

            try
            {
                // Upcoming Fixtures by Market ID
                OddsFixturesUpcomingByMarketIdResponse result = apiInstance.FixturesUpcomingByMarketId(version, sport, marketId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling OddsApi.FixturesUpcomingByMarketId: " + e.Message);
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

#### Using the FixturesUpcomingByMarketIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Upcoming Fixtures by Market ID
    ApiResponse<OddsFixturesUpcomingByMarketIdResponse> response = apiInstance.FixturesUpcomingByMarketIdWithHttpInfo(version, sport, marketId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OddsApi.FixturesUpcomingByMarketIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The sport you want to retrieve upcoming fixtures from. |  |
| **sport** | **string** |  |  |
| **marketId** | **int** | The ID of the market you want to retrieve upcoming fixtures from. |  |

### Return type

[**OddsFixturesUpcomingByMarketIdResponse**](OddsFixturesUpcomingByMarketIdResponse.md)

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

<a name="marketbyid"></a>
# **MarketById**
> OddsMarketByIdResponse MarketById (string version, int marketId)

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
    public class MarketByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new OddsApi(config);
            var version = v3;  // string | The version of the API.
            var marketId = 1;  // int | The ID of the market you want to retrieve.

            try
            {
                // By ID
                OddsMarketByIdResponse result = apiInstance.MarketById(version, marketId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling OddsApi.MarketById: " + e.Message);
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

#### Using the MarketByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<OddsMarketByIdResponse> response = apiInstance.MarketByIdWithHttpInfo(version, marketId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OddsApi.MarketByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **marketId** | **int** | The ID of the market you want to retrieve. |  |

### Return type

[**OddsMarketByIdResponse**](OddsMarketByIdResponse.md)

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

<a name="marketsall"></a>
# **MarketsAll**
> OddsMarketsAllResponse MarketsAll (string version)

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
    public class MarketsAllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new OddsApi(config);
            var version = v3;  // string | The version of the API.

            try
            {
                // All
                OddsMarketsAllResponse result = apiInstance.MarketsAll(version);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling OddsApi.MarketsAll: " + e.Message);
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

#### Using the MarketsAllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<OddsMarketsAllResponse> response = apiInstance.MarketsAllWithHttpInfo(version);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OddsApi.MarketsAllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |

### Return type

[**OddsMarketsAllResponse**](OddsMarketsAllResponse.md)

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

<a name="marketssearch"></a>
# **MarketsSearch**
> OddsMarketsSearchResponse MarketsSearch (string version, string name)

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
    public class MarketsSearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new OddsApi(config);
            var version = v3;  // string | The version of the API.
            var name = Over;  // string | The name you want to search on

            try
            {
                // Search
                OddsMarketsSearchResponse result = apiInstance.MarketsSearch(version, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling OddsApi.MarketsSearch: " + e.Message);
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

#### Using the MarketsSearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<OddsMarketsSearchResponse> response = apiInstance.MarketsSearchWithHttpInfo(version, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling OddsApi.MarketsSearchWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **name** | **string** | The name you want to search on |  |

### Return type

[**OddsMarketsSearchResponse**](OddsMarketsSearchResponse.md)

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

