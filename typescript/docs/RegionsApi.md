# RegionsApi

All URIs are relative to *https://api.sportmonks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](RegionsApi.md#all) | **GET** /{version}/core/regions | All
[**getById**](RegionsApi.md#getById) | **GET** /{version}/core/regions/{regionId} | By ID
[**search**](RegionsApi.md#search) | **GET** /{version}/core/regions/search/{name} | Search


# **all**

#### **GET** /{version}/core/regions


### Example


```typescript
import { Sportmonks } from "sportmonks-typescript-sdk";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "v3",
  sport: "football",
  apiKey: "API_KEY",
});

const allResponse = await sportmonks.regions.all({});

console.log(allResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined


### Return type

**RegionsAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **getById**

#### **GET** /{version}/core/regions/{regionId}


### Example


```typescript
import { Sportmonks } from "sportmonks-typescript-sdk";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "v3",
  sport: "football",
  apiKey: "API_KEY",
});

const getByIdResponse = await sportmonks.regions.getById({
  regionId: 1,
});

console.log(getByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regionId** | [**number**] | The ID of the region you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined


### Return type

**RegionsGetByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **search**

#### **GET** /{version}/core/regions/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks-typescript-sdk";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "v3",
  sport: "football",
  apiKey: "API_KEY",
});

const searchResponse = await sportmonks.regions.search({
  name: "name_example",
});

console.log(searchResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**string**] | The name you want to search on | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined


### Return type

**RegionsSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


