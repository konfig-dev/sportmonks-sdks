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
> OddsBookmakerByIdResponse BookmakerById (int bookmakerId, string version = null)

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

            SportmonksClient client = new SportmonksClient();
            // Configure custom BasePath if desired
            client.SetBasePath("https://api.sportmonks.com");
            client.SetVersion("VERSION");
            client.SetSport("SPORT");
            // Configure API key authorization: apikeyAuth
            client.SetApiKey("YOUR_API_KEY");

            var apiInstance = new OddsApi(config);
            var bookmakerId = 1;  // int | The ID of the bookmaker you want to retrieve.
            var version = "v3";  // string | The version of the API. (optional) 

            try
            {
                // By ID
                OddsBookmakerByIdResponse result = apiInstance.BookmakerById(bookmakerId, version);
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
    ApiResponse<OddsBookmakerByIdResponse> response = apiInstance.BookmakerByIdWithHttpInfo(bookmakerId, version);
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
| **bookmakerId** | **int** | The ID of the bookmaker you want to retrieve. |  |
| **version** | **string** | The version of the API. | [optional]  |

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
> OddsBookmakersAllResponse BookmakersAll (string version = null)

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

            SportmonksClient client = new SportmonksClient();
            // Configure custom BasePath if desired
            client.SetBasePath("https://api.sportmonks.com");
            client.SetVersion("VERSION");
            client.SetSport("SPORT");
            // Configure API key authorization: apikeyAuth
            client.SetApiKey("YOUR_API_KEY");

            var apiInstance = new OddsApi(config);
            var version = "v3";  // string | The version of the API. (optional) 

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
| **version** | **string** | The version of the API. | [optional]  |

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
> OddsBookmakersByFixtureIdResponse BookmakersByFixtureId (int fixtureId, string version = null)

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

            SportmonksClient client = new SportmonksClient();
            // Configure custom BasePath if desired
            client.SetBasePath("https://api.sportmonks.com");
            client.SetVersion("VERSION");
            client.SetSport("SPORT");
            // Configure API key authorization: apikeyAuth
            client.SetApiKey("YOUR_API_KEY");

            var apiInstance = new OddsApi(config);
            var fixtureId = 18528479;  // int | The ID of the bookmaker you want to retrieve.
            var version = "v3";  // string | The version of the API. (optional) 

            try
            {
                // By Fixture ID
                OddsBookmakersByFixtureIdResponse result = apiInstance.BookmakersByFixtureId(fixtureId, version);
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
    ApiResponse<OddsBookmakersByFixtureIdResponse> response = apiInstance.BookmakersByFixtureIdWithHttpInfo(fixtureId, version);
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
| **fixtureId** | **int** | The ID of the bookmaker you want to retrieve. |  |
| **version** | **string** | The version of the API. | [optional]  |

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
> OddsBookmakersMappingByFixtureIdResponse BookmakersMappingByFixtureId (int fixtureId, string version = null)

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

            SportmonksClient client = new SportmonksClient();
            // Configure custom BasePath if desired
            client.SetBasePath("https://api.sportmonks.com");
            client.SetVersion("VERSION");
            client.SetSport("SPORT");
            // Configure API key authorization: apikeyAuth
            client.SetApiKey("YOUR_API_KEY");

            var apiInstance = new OddsApi(config);
            var fixtureId = 18528479;  // int | The fixtureId you want to retrieve the bookmaker mapping from.
            var version = "v3";  // string | The version of the API. (optional) 

            try
            {
                // Mapping by Fixture ID
                OddsBookmakersMappingByFixtureIdResponse result = apiInstance.BookmakersMappingByFixtureId(fixtureId, version);
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
    ApiResponse<OddsBookmakersMappingByFixtureIdResponse> response = apiInstance.BookmakersMappingByFixtureIdWithHttpInfo(fixtureId, version);
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
| **fixtureId** | **int** | The fixtureId you want to retrieve the bookmaker mapping from. |  |
| **version** | **string** | The version of the API. | [optional]  |

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
> OddsBookmakersSearchResponse BookmakersSearch (string name, string version = null)

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

            SportmonksClient client = new SportmonksClient();
            // Configure custom BasePath if desired
            client.SetBasePath("https://api.sportmonks.com");
            client.SetVersion("VERSION");
            client.SetSport("SPORT");
            // Configure API key authorization: apikeyAuth
            client.SetApiKey("YOUR_API_KEY");

            var apiInstance = new OddsApi(config);
            var name = "Bet";  // string | The name you want to search on
            var version = "v3";  // string | The version of the API. (optional) 

            try
            {
                // Search
                OddsBookmakersSearchResponse result = apiInstance.BookmakersSearch(name, version);
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
    ApiResponse<OddsBookmakersSearchResponse> response = apiInstance.BookmakersSearchWithHttpInfo(name, version);
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
| **name** | **string** | The name you want to search on |  |
| **version** | **string** | The version of the API. | [optional]  |

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
> OddsFixturesUpcomingByMarketIdResponse FixturesUpcomingByMarketId (int marketId, string version = null, string sport = null)

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

            SportmonksClient client = new SportmonksClient();
            // Configure custom BasePath if desired
            client.SetBasePath("https://api.sportmonks.com");
            client.SetVersion("VERSION");
            client.SetSport("SPORT");
            // Configure API key authorization: apikeyAuth
            client.SetApiKey("YOUR_API_KEY");

            var apiInstance = new OddsApi(config);
            var marketId = 1;  // int | The ID of the market you want to retrieve upcoming fixtures from.
            var version = "v3";  // string | The sport you want to retrieve upcoming fixtures from. (optional) 
            var sport = "football";  // string |  (optional) 

            try
            {
                // Upcoming Fixtures by Market ID
                OddsFixturesUpcomingByMarketIdResponse result = apiInstance.FixturesUpcomingByMarketId(marketId, version, sport);
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
    ApiResponse<OddsFixturesUpcomingByMarketIdResponse> response = apiInstance.FixturesUpcomingByMarketIdWithHttpInfo(marketId, version, sport);
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
| **marketId** | **int** | The ID of the market you want to retrieve upcoming fixtures from. |  |
| **version** | **string** | The sport you want to retrieve upcoming fixtures from. | [optional]  |
| **sport** | **string** |  | [optional]  |

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
> OddsMarketByIdResponse MarketById (int marketId, string version = null)

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

            SportmonksClient client = new SportmonksClient();
            // Configure custom BasePath if desired
            client.SetBasePath("https://api.sportmonks.com");
            client.SetVersion("VERSION");
            client.SetSport("SPORT");
            // Configure API key authorization: apikeyAuth
            client.SetApiKey("YOUR_API_KEY");

            var apiInstance = new OddsApi(config);
            var marketId = 1;  // int | The ID of the market you want to retrieve.
            var version = "v3";  // string | The version of the API. (optional) 

            try
            {
                // By ID
                OddsMarketByIdResponse result = apiInstance.MarketById(marketId, version);
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
    ApiResponse<OddsMarketByIdResponse> response = apiInstance.MarketByIdWithHttpInfo(marketId, version);
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
| **marketId** | **int** | The ID of the market you want to retrieve. |  |
| **version** | **string** | The version of the API. | [optional]  |

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
> OddsMarketsAllResponse MarketsAll (string version = null)

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

            SportmonksClient client = new SportmonksClient();
            // Configure custom BasePath if desired
            client.SetBasePath("https://api.sportmonks.com");
            client.SetVersion("VERSION");
            client.SetSport("SPORT");
            // Configure API key authorization: apikeyAuth
            client.SetApiKey("YOUR_API_KEY");

            var apiInstance = new OddsApi(config);
            var version = "v3";  // string | The version of the API. (optional) 

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
| **version** | **string** | The version of the API. | [optional]  |

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
> OddsMarketsSearchResponse MarketsSearch (string name, string version = null)

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

            SportmonksClient client = new SportmonksClient();
            // Configure custom BasePath if desired
            client.SetBasePath("https://api.sportmonks.com");
            client.SetVersion("VERSION");
            client.SetSport("SPORT");
            // Configure API key authorization: apikeyAuth
            client.SetApiKey("YOUR_API_KEY");

            var apiInstance = new OddsApi(config);
            var name = "Over";  // string | The name you want to search on
            var version = "v3";  // string | The version of the API. (optional) 

            try
            {
                // Search
                OddsMarketsSearchResponse result = apiInstance.MarketsSearch(name, version);
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
    ApiResponse<OddsMarketsSearchResponse> response = apiInstance.MarketsSearchWithHttpInfo(name, version);
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
| **name** | **string** | The name you want to search on |  |
| **version** | **string** | The version of the API. | [optional]  |

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

