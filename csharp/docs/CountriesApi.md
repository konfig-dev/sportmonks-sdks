# Sportmonks.Net.Api.CountriesApi

All URIs are relative to *https://api.sportmonks.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**All**](CountriesApi.md#all) | **GET** /{version}/core/countries | All |
| [**GetById**](CountriesApi.md#getbyid) | **GET** /{version}/core/countries/{countryId} | By ID |
| [**Search**](CountriesApi.md#search) | **GET** /{version}/core/countries/search/{name} | Search |

<a name="all"></a>
# **All**
> CountriesAllResponse All (string version = null)

All

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class AllExample
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

            var version = "v3";  // string | The version of the API. (optional) 

            try
            {
                // All
                CountriesAllResponse result = client.Countries.All(version);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling CountriesApi.All: " + e.Message);
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
    ApiResponse<CountriesAllResponse> response = apiInstance.AllWithHttpInfo(version);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CountriesApi.AllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. | [optional]  |

### Return type

[**CountriesAllResponse**](CountriesAllResponse.md)

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
> CountriesGetByIdResponse GetById (int countryId, string version = null)

By ID

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class GetByIdExample
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

            var countryId = 1161;  // int | The ID of the country you want to retrieve.
            var version = "v3";  // string | The version of the API. (optional) 

            try
            {
                // By ID
                CountriesGetByIdResponse result = client.Countries.GetById(countryId, version);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling CountriesApi.GetById: " + e.Message);
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
    ApiResponse<CountriesGetByIdResponse> response = apiInstance.GetByIdWithHttpInfo(countryId, version);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CountriesApi.GetByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **countryId** | **int** | The ID of the country you want to retrieve. |  |
| **version** | **string** | The version of the API. | [optional]  |

### Return type

[**CountriesGetByIdResponse**](CountriesGetByIdResponse.md)

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
> CountriesSearchResponse Search (string name, string version = null)

Search

### Example
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Example
{
    public class SearchExample
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

            var name = "Fra";  // string | The name you want to search on
            var version = "v3";  // string | The version of the API. (optional) 

            try
            {
                // Search
                CountriesSearchResponse result = client.Countries.Search(name, version);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling CountriesApi.Search: " + e.Message);
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
    ApiResponse<CountriesSearchResponse> response = apiInstance.SearchWithHttpInfo(name, version);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CountriesApi.SearchWithHttpInfo: " + e.Message);
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

[**CountriesSearchResponse**](CountriesSearchResponse.md)

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

