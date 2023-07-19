# sportmonks.model.sport_fixtures_head_to_head_response_data_item.SportFixturesHeadToHeadResponseDataItem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**sport_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**league_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**season_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**stage_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**[group_id](#group_id)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**aggregate_id** | None, str,  | NoneClass, str,  |  | [optional] 
**round_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**state_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**venue_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**home_score** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**away_score** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**starting_at** | str,  | str,  |  | [optional] 
**result_info** | None, str,  | NoneClass, str,  |  | [optional] 
**leg** | str,  | str,  |  | [optional] 
**details** | None, str,  | NoneClass, str,  |  | [optional] 
**length** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**placeholder** | bool,  | BoolClass,  |  | [optional] 
**last_processed_at** | None, str,  | NoneClass, str,  |  | [optional] 
**starting_at_timestamp** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# group_id

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

