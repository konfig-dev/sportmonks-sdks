# TypesApi

All URIs are relative to *https://api.sportmonks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](TypesApi.md#all) | **GET** /{version}/core/types | All
[**getById**](TypesApi.md#getById) | **GET** /{version}/core/types/{typeId} | By ID


# **all**

#### **GET** /{version}/core/types


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

const allResponse = await sportmonks.types.all({});

console.log(allResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined


### Return type

**TypesAllResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **getById**

#### **GET** /{version}/core/types/{typeId}


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

const getByIdResponse = await sportmonks.types.getById({
  typeId: 1,
});

console.log(getByIdResponse);
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **typeId** | [**number**] | The ID of the type you want to retrieve | defaults to undefined
 **version** | [**string**] | The version of the API. | (optional) defaults to undefined


### Return type

**TypesGetByIdResponse**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


