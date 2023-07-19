# sportmonks.model.sport_odds_pre_match_by_fixture_and_bookmaker_id_response_data_item.SportOddsPreMatchByFixtureAndBookmakerIdResponseDataItem

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**fixture_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**market_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**bookmaker_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**label** | str,  | str,  |  | [optional] 
**value** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**sort_order** | None, str,  | NoneClass, str,  |  | [optional] 
**market_description** | str,  | str,  |  | [optional] 
**probability** | str,  | str,  |  | [optional] 
**dp3** | str,  | str,  |  | [optional] 
**fractional** | str,  | str,  |  | [optional] 
**american** | str,  | str,  |  | [optional] 
**[winning](#winning)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**stopped** | bool,  | BoolClass,  |  | [optional] 
**total** | None, str,  | NoneClass, str,  |  | [optional] 
**handicap** | None, str,  | NoneClass, str,  |  | [optional] 
**participants** | None, str,  | NoneClass, str,  |  | [optional] 
**created_at** | str,  | str,  |  | [optional] 
**updated_at** | str,  | str,  |  | [optional] 
**original_label** | None, str,  | NoneClass, str,  |  | [optional] 
**latest_bookmaker_update** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# winning

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | bool,  | BoolClass,  |  | 
[one_of_1](#one_of_1) | None, str,  | NoneClass, str,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
