# sportmonks.model.sport_predictions_by_fixture_id_response.SportPredictionsByFixtureIdResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[data](#data)** | list, tuple,  | tuple,  |  | [optional] 
**[pagination](#pagination)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[subscription](#subscription)** | list, tuple,  | tuple,  |  | [optional] 
**[rate_limit](#rate_limit)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**timezone** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**fixture_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**[predictions](#predictions)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**type_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# predictions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**true** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**false** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**[scores](#scores)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**home** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**draw** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**away** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# scores

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**0-0** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**0-1** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**0-2** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**0-3** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**0-4** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**0-5** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**0-6** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**0-7** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**1-0** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**1-1** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**1-2** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**1-3** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**1-4** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**1-5** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**1-6** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**1-7** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**1-8** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**2-0** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**2-1** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**2-2** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**2-3** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**2-4** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**2-5** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**2-6** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**2-7** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**3-0** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**3-1** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**3-2** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**3-3** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**3-4** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**3-5** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**3-6** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**3-7** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**4-0** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**4-1** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**4-2** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**4-3** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**4-4** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**4-5** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**4-6** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**4-7** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**5-0** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**5-1** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**5-2** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**5-3** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**5-4** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**5-5** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**5-6** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**6-0** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**6-1** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**6-2** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**6-3** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**6-4** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**6-5** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**6-6** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**7-0** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**7-1** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**7-2** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**7-3** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**7-4** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**7-5** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**8-0** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**8-1** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**8-2** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**8-3** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**8-4** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**9-0** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**9-1** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**9-2** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**9-3** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# pagination

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**per_page** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**current_page** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**next_page** | None, str,  | NoneClass, str,  |  | [optional] 
**has_more** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# subscription

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[meta](#meta)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[plans](#plans)** | list, tuple,  | tuple,  |  | [optional] 
**[add_ons](#add_ons)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# meta

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**trial_ends_at** | None, str,  | NoneClass, str,  |  | [optional] 
**ends_at** | None, str,  | NoneClass, str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# plans

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**plan** | str,  | str,  |  | [optional] 
**sport** | str,  | str,  |  | [optional] 
**category** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# add_ons

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**add_on** | str,  | str,  |  | [optional] 
**sport** | str,  | str,  |  | [optional] 
**category** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rate_limit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**resets_in_seconds** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**remaining** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**requested_entity** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

