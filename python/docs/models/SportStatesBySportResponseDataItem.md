# sportmonks.model.sport_states_by_sport_response_data_item.SportStatesBySportResponseDataItem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**state** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**short_name** | str,  | str,  |  | [optional] 
**developer_name** | str,  | str,  |  | [optional] 
**is_live** | bool,  | BoolClass,  |  | [optional] 
**is_pending** | bool,  | BoolClass,  |  | [optional] 
**is_period_end** | bool,  | BoolClass,  |  | [optional] 
**is_final_state** | bool,  | BoolClass,  |  | [optional] 
**is_cancelled** | bool,  | BoolClass,  |  | [optional] 
**is_final_standing_state** | bool,  | BoolClass,  |  | [optional] 
**is_completed** | bool,  | BoolClass,  |  | [optional] 
**[type_id](#type_id)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**is_deleted** | bool,  | BoolClass,  |  | [optional] 
**is_notstarted** | bool,  | BoolClass,  |  | [optional] 
**sections_active** | bool,  | BoolClass,  |  | [optional] 
**schedule_overrule** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# type_id

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | None, str,  | NoneClass, str,  |  | 
[one_of_1](#one_of_1) | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

