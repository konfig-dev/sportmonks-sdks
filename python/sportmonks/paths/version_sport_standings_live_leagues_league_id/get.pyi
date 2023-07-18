# coding: utf-8

"""
    SportMonks

    Surpass the competition with superior sports data

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from sportmonks.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from sportmonks.api_response import AsyncGeneratorResponse
from sportmonks import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sportmonks import schemas  # noqa: F401

from sportmonks.model.sport_standings_live_by_league_id_response import SportStandingsLiveByLeagueIdResponse as SportStandingsLiveByLeagueIdResponseSchema

from sportmonks.type.sport_standings_live_by_league_id_response import SportStandingsLiveByLeagueIdResponse

# Path params
VersionSchema = schemas.StrSchema
SportSchema = schemas.StrSchema
LeagueIdSchema = schemas.IntSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'version': typing.Union[VersionSchema, str, ],
        'sport': typing.Union[SportSchema, str, ],
        'leagueId': typing.Union[LeagueIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_version = api_client.PathParameter(
    name="version",
    style=api_client.ParameterStyle.SIMPLE,
    schema=VersionSchema,
    required=True,
)
request_path_sport = api_client.PathParameter(
    name="sport",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SportSchema,
    required=True,
)
request_path_league_id = api_client.PathParameter(
    name="leagueId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LeagueIdSchema,
    required=True,
)
DateSchema = schemas.StrSchema
ServerSchema = schemas.StrSchema
CacheControlSchema = schemas.StrSchema
XRateLimitLimitSchema = schemas.IntSchema
XRateLimitRemainingSchema = schemas.IntSchema
VarySchema = schemas.StrSchema
ContentEncodingSchema = schemas.StrSchema
XRobotsTagSchema = schemas.StrSchema
ContentLengthSchema = schemas.IntSchema
SchemaFor200ResponseBodyApplicationJson = SportStandingsLiveByLeagueIdResponseSchema
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'Date': DateSchema,
        'Server': ServerSchema,
        'Cache-Control': CacheControlSchema,
        'X-RateLimit-Limit': XRateLimitLimitSchema,
        'X-RateLimit-Remaining': XRateLimitRemainingSchema,
        'Vary': VarySchema,
        'Content-Encoding': ContentEncodingSchema,
        'X-Robots-Tag': XRobotsTagSchema,
        'Content-Length': ContentLengthSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SportStandingsLiveByLeagueIdResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SportStandingsLiveByLeagueIdResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
    headers=[
        date_parameter,
        server_parameter,
        cache_control_parameter,
        x_rate_limit_limit_parameter,
        x_rate_limit_remaining_parameter,
        vary_parameter,
        content_encoding_parameter,
        x_robots_tag_parameter,
        content_length_parameter,
    ]
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _standings_live_by_league_id_mapped_args(
        self,
        version: str,
        sport: str,
        league_id: int,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if version is not None:
            _path_params["version"] = version
        if sport is not None:
            _path_params["sport"] = sport
        if league_id is not None:
            _path_params["leagueId"] = league_id
        args.path = _path_params
        return args

    async def _astandings_live_by_league_id_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        By League ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_version,
            request_path_sport,
            request_path_league_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _standings_live_by_league_id_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        By League ID
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_version,
            request_path_sport,
            request_path_league_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class StandingsLiveByLeagueId(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def astandings_live_by_league_id(
        self,
        version: str,
        sport: str,
        league_id: int,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._standings_live_by_league_id_mapped_args(
            version=version,
            sport=sport,
            league_id=league_id,
        )
        return await self._astandings_live_by_league_id_oapg(
            path_params=args.path,
        )
    
    def standings_live_by_league_id(
        self,
        version: str,
        sport: str,
        league_id: int,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._standings_live_by_league_id_mapped_args(
            version=version,
            sport=sport,
            league_id=league_id,
        )
        return self._standings_live_by_league_id_oapg(
            path_params=args.path,
        )

class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        version: str,
        sport: str,
        league_id: int,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._standings_live_by_league_id_mapped_args(
            version=version,
            sport=sport,
            league_id=league_id,
        )
        return await self._astandings_live_by_league_id_oapg(
            path_params=args.path,
        )
    
    def get(
        self,
        version: str,
        sport: str,
        league_id: int,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._standings_live_by_league_id_mapped_args(
            version=version,
            sport=sport,
            league_id=league_id,
        )
        return self._standings_live_by_league_id_oapg(
            path_params=args.path,
        )

