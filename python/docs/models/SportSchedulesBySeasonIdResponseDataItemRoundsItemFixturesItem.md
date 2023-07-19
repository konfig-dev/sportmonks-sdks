# sportmonks.model.sport_schedules_by_season_id_response_data_item_rounds_item_fixtures_item.SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItem

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
**group_id** | None, str,  | NoneClass, str,  |  | [optional] 
**aggregate_id** | None, str,  | NoneClass, str,  |  | [optional] 
**round_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**state_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**venue_id** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**[home_score](#home_score)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**[away_score](#away_score)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**starting_at** | str,  | str,  |  | [optional] 
**result_info** | None, str,  | NoneClass, str,  |  | [optional] 
**leg** | str,  | str,  |  | [optional] 
**details** | None, str,  | NoneClass, str,  |  | [optional] 
**length** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**placeholder** | bool,  | BoolClass,  |  | [optional] 
**last_processed_at** | None, str,  | NoneClass, str,  |  | [optional] 
**starting_at_timestamp** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**participants** | [**SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipants**](SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipants.md) | [**SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipants**](SportSchedulesBySeasonIdResponseDataItemRoundsItemFixturesItemParticipants.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# home_score

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
[one_of_1](#one_of_1) | None, str,  | NoneClass, str,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | 

# away_score

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
[one_of_1](#one_of_1) | None, str,  | NoneClass, str,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

