# ContinentsApi

All URIs are relative to *https://api.sportmonks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](ContinentsApi.md#all) | **GET** /{version}/core/continents | All
[**getById**](ContinentsApi.md#getById) | **GET** /{version}/core/continents/{continentId} | By ID


# **all**

#### **GET** /{version}/core/continents


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
});

const allResponse = await sportmonks.continents.all({
  version: "version_example",
});

console.log(allResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | defaults to undefined


### Return type

**ContinentsAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **getById**

#### **GET** /{version}/core/continents/{continentId}


### Example


```typescript
import { Sportmonks } from "sportmonks";

const sportmonks = new Sportmonks({
  // Defining the base path is optional and defaults to https://api.sportmonks.com
  // basePath: "https://api.sportmonks.com",
});

const getByIdResponse = await sportmonks.continents.getById({
  version: "version_example",
  continentId: 1,
});

console.log(getByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | defaults to undefined
 **continentId** | [**number**] | The ID of the continent you want to retrieve | defaults to undefined


### Return type

**ContinentsGetByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


