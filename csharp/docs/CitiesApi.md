# Sportmonks.Net.Api.CitiesApi

All URIs are relative to *https://api.sportmonks.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**All**](CitiesApi.md#all) | **GET** /{version}/core/cities | All |
| [**GetById**](CitiesApi.md#getbyid) | **GET** /{version}/core/cities/{cityId} | By ID |
| [**Search**](CitiesApi.md#search) | **GET** /{version}/core/cities/search/{name} | Search |

<a name="all"></a>
# **All**
> CitiesAllResponse All (string version)

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
    public class AllExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new CitiesApi(config);
            var version = v3;  // string | The version of the API.

            try
            {
                // All
                CitiesAllResponse result = apiInstance.All(version);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling CitiesApi.All: " + e.Message);
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

#### Using the AllWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // All
    ApiResponse<CitiesAllResponse> response = apiInstance.AllWithHttpInfo(version);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CitiesApi.AllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |

### Return type

[**CitiesAllResponse**](CitiesAllResponse.md)

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

<a name="getbyid"></a>
# **GetById**
> CitiesGetByIdResponse GetById (string version, int cityId)

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
    public class GetByIdExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new CitiesApi(config);
            var version = v3;  // string | The version of the API.
            var cityId = 29834;  // int | The ID of the city you want to retrieve

            try
            {
                // By ID
                CitiesGetByIdResponse result = apiInstance.GetById(version, cityId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling CitiesApi.GetById: " + e.Message);
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

#### Using the GetByIdWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // By ID
    ApiResponse<CitiesGetByIdResponse> response = apiInstance.GetByIdWithHttpInfo(version, cityId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CitiesApi.GetByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **cityId** | **int** | The ID of the city you want to retrieve |  |

### Return type

[**CitiesGetByIdResponse**](CitiesGetByIdResponse.md)

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

<a name="search"></a>
# **Search**
> CitiesSearchResponse Search (string version, string name)

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
    public class SearchExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();

            // Configure custom BasePath if desired
            // config.BasePath = "https://api.sportmonks.com";


            var apiInstance = new CitiesApi(config);
            var version = v3;  // string | The version of the API.
            var name = Lon;  // string | The name you want to search on

            try
            {
                // Search
                CitiesSearchResponse result = apiInstance.Search(version, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling CitiesApi.Search: " + e.Message);
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

#### Using the SearchWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Search
    ApiResponse<CitiesSearchResponse> response = apiInstance.SearchWithHttpInfo(version, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CitiesApi.SearchWithHttpInfo: " + e.Message);
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

[**CitiesSearchResponse**](CitiesSearchResponse.md)

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
