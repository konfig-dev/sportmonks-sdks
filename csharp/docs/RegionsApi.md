# Sportmonks.Net.Api.RegionsApi

All URIs are relative to *https://api.sportmonks.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**All**](RegionsApi.md#all) | **GET** /{version}/core/regions | All |
| [**GetById**](RegionsApi.md#getbyid) | **GET** /{version}/core/regions/{regionId} | By ID |
| [**Search**](RegionsApi.md#search) | **GET** /{version}/core/regions/search/{name} | Search |

<a name="all"></a>
# **All**
> RegionsAllResponse All (string version)

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


            var apiInstance = new RegionsApi(config);
            var version = v3;  // string | The version of the API.

            try
            {
                // All
                RegionsAllResponse result = apiInstance.All(version);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling RegionsApi.All: " + e.Message);
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
    ApiResponse<RegionsAllResponse> response = apiInstance.AllWithHttpInfo(version);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling RegionsApi.AllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |

### Return type

[**RegionsAllResponse**](RegionsAllResponse.md)

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
> RegionsGetByIdResponse GetById (string version, int regionId)

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


            var apiInstance = new RegionsApi(config);
            var version = v3;  // string | The version of the API.
            var regionId = 367;  // int | The ID of the region you want to retrieve.

            try
            {
                // By ID
                RegionsGetByIdResponse result = apiInstance.GetById(version, regionId);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling RegionsApi.GetById: " + e.Message);
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
    ApiResponse<RegionsGetByIdResponse> response = apiInstance.GetByIdWithHttpInfo(version, regionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling RegionsApi.GetByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. |  |
| **regionId** | **int** | The ID of the region you want to retrieve. |  |

### Return type

[**RegionsGetByIdResponse**](RegionsGetByIdResponse.md)

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
> RegionsSearchResponse Search (string version, string name)

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


            var apiInstance = new RegionsApi(config);
            var version = v3;  // string | The version of the API.
            var name = Br;  // string | The name you want to search on

            try
            {
                // Search
                RegionsSearchResponse result = apiInstance.Search(version, name);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling RegionsApi.Search: " + e.Message);
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
    ApiResponse<RegionsSearchResponse> response = apiInstance.SearchWithHttpInfo(version, name);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling RegionsApi.SearchWithHttpInfo: " + e.Message);
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

[**RegionsSearchResponse**](RegionsSearchResponse.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

