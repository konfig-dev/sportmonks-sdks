# CountriesApi

All URIs are relative to *https://api.sportmonks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](CountriesApi.md#all) | **GET** /{version}/core/countries | All
[**getById**](CountriesApi.md#getById) | **GET** /{version}/core/countries/{countryId} | By ID
[**search**](CountriesApi.md#search) | **GET** /{version}/core/countries/search/{name} | Search


# **all**

#### **GET** /{version}/core/countries


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "v3",
  sport: "football",
  apiKey: "API_KEY",
});

const allResponse = await sportmonks.countries.all({});

console.log(allResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined


### Return type

**CountriesAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **getById**

#### **GET** /{version}/core/countries/{countryId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "v3",
  sport: "football",
  apiKey: "API_KEY",
});

const getByIdResponse = await sportmonks.countries.getById({
  countryId: 1,
});

console.log(getByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countryId** | [**number**] | The ID of the country you want to retrieve. | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined


### Return type

**CountriesGetByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **search**

#### **GET** /{version}/core/countries/search/{name}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
  version: "v3",
  sport: "football",
  apiKey: "API_KEY",
});

const searchResponse = await sportmonks.countries.search({
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

**CountriesSearchResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


