<a name="__pageTop"></a>
# sportmonks.apis.tags.odds_api.OddsApi

All URIs are relative to *https://api.sportmonks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookmaker_by_id**](#bookmaker_by_id) | **get** /{version}/odds/bookmakers/{bookmakerId} | By ID
[**bookmakers_all**](#bookmakers_all) | **get** /{version}/odds/bookmakers | All
[**bookmakers_by_fixture_id**](#bookmakers_by_fixture_id) | **get** /{version}/odds/bookmakers/fixtures/{fixtureId} | By Fixture ID
[**bookmakers_mapping_by_fixture_id**](#bookmakers_mapping_by_fixture_id) | **get** /{version}/odds/bookmakers/fixtures/{fixtureId}/mapping | Mapping by Fixture ID
[**bookmakers_search**](#bookmakers_search) | **get** /{version}/odds/bookmakers/search/{name} | Search
[**fixtures_upcoming_by_market_id**](#fixtures_upcoming_by_market_id) | **get** /{version}/{sport}/fixtures/upcoming/markets/{marketId} | Upcoming Fixtures by Market ID
[**market_by_id**](#market_by_id) | **get** /{version}/odds/markets/{marketId} | By ID
[**markets_all**](#markets_all) | **get** /{version}/odds/markets | All
[**markets_search**](#markets_search) | **get** /{version}/odds/markets/search/{name} | Search

# **bookmaker_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
)

try:
    # By ID
    bookmaker_by_id_response = sportmonks.odds.bookmaker_by_id(
        version="v3",  # required
        bookmaker_id=1,  # required
    )
    pprint(bookmaker_by_id_response.body)
    pprint(bookmaker_by_id_response.body["data"])
    pprint(bookmaker_by_id_response.body["subscription"])
    pprint(bookmaker_by_id_response.body["rate_limit"])
    pprint(bookmaker_by_id_response.body["timezone"])
    pprint(bookmaker_by_id_response.headers)
    pprint(bookmaker_by_id_response.status)
    pprint(bookmaker_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling OddsApi.bookmaker_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | 
bookmakerId | BookmakerIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BookmakerIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#bookmaker_by_id.ApiResponseForDefault) | 

#### bookmaker_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OddsBookmakerByIdResponse**](../../models/OddsBookmakerByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **bookmakers_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
)

try:
    # All
    bookmakers_all_response = sportmonks.odds.bookmakers_all(
        version="v3",  # required
    )
    pprint(bookmakers_all_response.body)
    pprint(bookmakers_all_response.body["data"])
    pprint(bookmakers_all_response.body["pagination"])
    pprint(bookmakers_all_response.body["subscription"])
    pprint(bookmakers_all_response.body["rate_limit"])
    pprint(bookmakers_all_response.body["timezone"])
    pprint(bookmakers_all_response.headers)
    pprint(bookmakers_all_response.status)
    pprint(bookmakers_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling OddsApi.bookmakers_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#bookmakers_all.ApiResponseForDefault) | 

#### bookmakers_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OddsBookmakersAllResponse**](../../models/OddsBookmakersAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **bookmakers_by_fixture_id**

By Fixture ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
)

try:
    # By Fixture ID
    bookmakers_by_fixture_id_response = sportmonks.odds.bookmakers_by_fixture_id(
        version="v3",  # required
        fixture_id=18528479,  # required
    )
    pprint(bookmakers_by_fixture_id_response.body)
    pprint(bookmakers_by_fixture_id_response.body["data"])
    pprint(bookmakers_by_fixture_id_response.body["pagination"])
    pprint(bookmakers_by_fixture_id_response.body["subscription"])
    pprint(bookmakers_by_fixture_id_response.body["rate_limit"])
    pprint(bookmakers_by_fixture_id_response.body["timezone"])
    pprint(bookmakers_by_fixture_id_response.headers)
    pprint(bookmakers_by_fixture_id_response.status)
    pprint(bookmakers_by_fixture_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling OddsApi.bookmakers_by_fixture_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | 
fixtureId | FixtureIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#bookmakers_by_fixture_id.ApiResponseForDefault) | 

#### bookmakers_by_fixture_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OddsBookmakersByFixtureIdResponse**](../../models/OddsBookmakersByFixtureIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **bookmakers_mapping_by_fixture_id**

Mapping by Fixture ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
)

try:
    # Mapping by Fixture ID
    bookmakers_mapping_by_fixture_id_response = (
        sportmonks.odds.bookmakers_mapping_by_fixture_id(
            version="v3",  # required
            fixture_id=18528479,  # required
        )
    )
    pprint(bookmakers_mapping_by_fixture_id_response.body)
    pprint(bookmakers_mapping_by_fixture_id_response.body["data"])
    pprint(bookmakers_mapping_by_fixture_id_response.body["subscription"])
    pprint(bookmakers_mapping_by_fixture_id_response.body["rate_limit"])
    pprint(bookmakers_mapping_by_fixture_id_response.body["timezone"])
    pprint(bookmakers_mapping_by_fixture_id_response.headers)
    pprint(bookmakers_mapping_by_fixture_id_response.status)
    pprint(bookmakers_mapping_by_fixture_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling OddsApi.bookmakers_mapping_by_fixture_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | 
fixtureId | FixtureIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FixtureIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#bookmakers_mapping_by_fixture_id.ApiResponseForDefault) | 

#### bookmakers_mapping_by_fixture_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OddsBookmakersMappingByFixtureIdResponse**](../../models/OddsBookmakersMappingByFixtureIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **bookmakers_search**

Search

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
)

try:
    # Search
    bookmakers_search_response = sportmonks.odds.bookmakers_search(
        version="v3",  # required
        name="Bet",  # required
    )
    pprint(bookmakers_search_response.body)
    pprint(bookmakers_search_response.body["data"])
    pprint(bookmakers_search_response.body["pagination"])
    pprint(bookmakers_search_response.body["subscription"])
    pprint(bookmakers_search_response.body["rate_limit"])
    pprint(bookmakers_search_response.body["timezone"])
    pprint(bookmakers_search_response.headers)
    pprint(bookmakers_search_response.status)
    pprint(bookmakers_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling OddsApi.bookmakers_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | 
name | NameSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#bookmakers_search.ApiResponseForDefault) | 

#### bookmakers_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OddsBookmakersSearchResponse**](../../models/OddsBookmakersSearchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **fixtures_upcoming_by_market_id**

Upcoming Fixtures by Market ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
)

try:
    # Upcoming Fixtures by Market ID
    fixtures_upcoming_by_market_id_response = (
        sportmonks.odds.fixtures_upcoming_by_market_id(
            version="v3",  # required
            sport="football",  # required
            market_id=1,  # required
        )
    )
    pprint(fixtures_upcoming_by_market_id_response.body)
    pprint(fixtures_upcoming_by_market_id_response.body["data"])
    pprint(fixtures_upcoming_by_market_id_response.body["message"])
    pprint(fixtures_upcoming_by_market_id_response.body["subscription"])
    pprint(fixtures_upcoming_by_market_id_response.body["rate_limit"])
    pprint(fixtures_upcoming_by_market_id_response.body["timezone"])
    pprint(fixtures_upcoming_by_market_id_response.headers)
    pprint(fixtures_upcoming_by_market_id_response.status)
    pprint(fixtures_upcoming_by_market_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling OddsApi.fixtures_upcoming_by_market_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | 
sport | SportSchema | | 
marketId | MarketIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SportSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MarketIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#fixtures_upcoming_by_market_id.ApiResponseForDefault) | 

#### fixtures_upcoming_by_market_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OddsFixturesUpcomingByMarketIdResponse**](../../models/OddsFixturesUpcomingByMarketIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **market_by_id**

By ID

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
)

try:
    # By ID
    market_by_id_response = sportmonks.odds.market_by_id(
        version="v3",  # required
        market_id=1,  # required
    )
    pprint(market_by_id_response.body)
    pprint(market_by_id_response.body["data"])
    pprint(market_by_id_response.body["subscription"])
    pprint(market_by_id_response.body["rate_limit"])
    pprint(market_by_id_response.body["timezone"])
    pprint(market_by_id_response.headers)
    pprint(market_by_id_response.status)
    pprint(market_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling OddsApi.market_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | 
marketId | MarketIdSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MarketIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#market_by_id.ApiResponseForDefault) | 

#### market_by_id.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OddsMarketByIdResponse**](../../models/OddsMarketByIdResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **markets_all**

All

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
)

try:
    # All
    markets_all_response = sportmonks.odds.markets_all(
        version="v3",  # required
    )
    pprint(markets_all_response.body)
    pprint(markets_all_response.body["data"])
    pprint(markets_all_response.body["pagination"])
    pprint(markets_all_response.body["subscription"])
    pprint(markets_all_response.body["rate_limit"])
    pprint(markets_all_response.body["timezone"])
    pprint(markets_all_response.headers)
    pprint(markets_all_response.status)
    pprint(markets_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling OddsApi.markets_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#markets_all.ApiResponseForDefault) | 

#### markets_all.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OddsMarketsAllResponse**](../../models/OddsMarketsAllResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **markets_search**

Search

### Example

```python
from pprint import pprint
from sportmonks import Sportmonks, ApiException

sportmonks = Sportmonks(
    # Defining the host is optional and defaults to https://api.sportmonks.com
    # See configuration.py for a list of all supported configuration parameters.
    host="https://api.sportmonks.com",
)

try:
    # Search
    markets_search_response = sportmonks.odds.markets_search(
        version="v3",  # required
        name="Over",  # required
    )
    pprint(markets_search_response.body)
    pprint(markets_search_response.body["data"])
    pprint(markets_search_response.body["pagination"])
    pprint(markets_search_response.body["subscription"])
    pprint(markets_search_response.body["rate_limit"])
    pprint(markets_search_response.body["timezone"])
    pprint(markets_search_response.headers)
    pprint(markets_search_response.status)
    pprint(markets_search_response.round_trip_time)
except ApiException as e:
    print("Exception when calling OddsApi.markets_search: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | 
name | NameSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#markets_search.ApiResponseForDefault) | 

#### markets_search.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OddsMarketsSearchResponse**](../../models/OddsMarketsSearchResponse.md) |  | 


### Authorization

[apikeyAuth](../../../README.md#apikeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

