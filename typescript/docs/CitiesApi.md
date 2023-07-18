# CitiesApi

All URIs are relative to *https://api.sportmonks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](CitiesApi.md#all) | **GET** /{version}/core/cities | All
[**getById**](CitiesApi.md#getById) | **GET** /{version}/core/cities/{cityId} | By ID
[**search**](CitiesApi.md#search) | **GET** /{version}/core/cities/search/{name} | Search


# **all**

#### **GET** /{version}/core/cities


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

const allResponse = await sportmonks.cities.all({});

console.log(allResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined


### Return type

**CitiesAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **getById**

#### **GET** /{version}/core/cities/{cityId}


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

const getByIdResponse = await sportmonks.cities.getById({
  cityId: 1,
});

console.log(getByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cityId** | [**number**] | The ID of the city you want to retrieve | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined


### Return type

**CitiesGetByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **search**

#### **GET** /{version}/core/cities/search/{name}


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

const searchResponse = await sportmonks.cities.search({
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

**CitiesSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


