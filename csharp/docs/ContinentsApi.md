# Sportmonks.Net.Api.ContinentsApi

All URIs are relative to *https://api.sportmonks.com*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**All**](ContinentsApi.md#all) | **GET** /{version}/core/continents | All |
| [**GetById**](ContinentsApi.md#getbyid) | **GET** /{version}/core/continents/{continentId} | By ID |

<a name="all"></a>
# **All**
> ContinentsAllResponse All (string version = null)

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

            SportmonksClient client = new SportmonksClient();
            // Configure custom BasePath if desired
            client.SetBasePath("https://api.sportmonks.com");
            client.SetVersion("VERSION");
            client.SetSport("SPORT");
            // Configure API key authorization: apikeyAuth
            client.SetApiKey("YOUR_API_KEY");

            var apiInstance = new ContinentsApi(config);
            var version = "v3";  // string | The version of the API. (optional) 

            try
            {
                // All
                ContinentsAllResponse result = apiInstance.All(version);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling ContinentsApi.All: " + e.Message);
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
    ApiResponse<ContinentsAllResponse> response = apiInstance.AllWithHttpInfo(version);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ContinentsApi.AllWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** | The version of the API. | [optional]  |

### Return type

[**ContinentsAllResponse**](ContinentsAllResponse.md)

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
> ContinentsGetByIdResponse GetById (int continentId, string version = null)

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

            SportmonksClient client = new SportmonksClient();
            // Configure custom BasePath if desired
            client.SetBasePath("https://api.sportmonks.com");
            client.SetVersion("VERSION");
            client.SetSport("SPORT");
            // Configure API key authorization: apikeyAuth
            client.SetApiKey("YOUR_API_KEY");

            var apiInstance = new ContinentsApi(config);
            var continentId = 1;  // int | The ID of the continent you want to retrieve
            var version = "v3";  // string | The version of the API. (optional) 

            try
            {
                // By ID
                ContinentsGetByIdResponse result = apiInstance.GetById(continentId, version);
                Console.WriteLine(result);
            }
            catch (ApiException e)
            {
                Console.WriteLine("Exception when calling ContinentsApi.GetById: " + e.Message);
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
    ApiResponse<ContinentsGetByIdResponse> response = apiInstance.GetByIdWithHttpInfo(continentId, version);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ContinentsApi.GetByIdWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **continentId** | **int** | The ID of the continent you want to retrieve |  |
| **version** | **string** | The version of the API. | [optional]  |

### Return type

[**ContinentsGetByIdResponse**](ContinentsGetByIdResponse.md)

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

