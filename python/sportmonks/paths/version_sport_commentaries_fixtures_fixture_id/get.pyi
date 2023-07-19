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

from sportmonks.model.sport_commentaries_by_fixture_id_response import SportCommentariesByFixtureIdResponse as SportCommentariesByFixtureIdResponseSchema

from sportmonks.type.sport_commentaries_by_fixture_id_response import SportCommentariesByFixtureIdResponse

# Path params
VersionSchema = schemas.StrSchema
SportSchema = schemas.StrSchema
FixtureIdSchema = schemas.IntSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'fixtureId': typing.Union[FixtureIdSchema, decimal.Decimal, int, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
        'version': typing.Union[VersionSchema, str, ],
        'sport': typing.Union[SportSchema, str, ],
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_version = api_client.PathParameter(
    name="version",
    style=api_client.ParameterStyle.SIMPLE,
    schema=VersionSchema,
)
request_path_sport = api_client.PathParameter(
    name="sport",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SportSchema,
)
request_path_fixture_id = api_client.PathParameter(
    name="fixtureId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FixtureIdSchema,
    required=True,
)
SchemaFor0ResponseBodyApplicationJson = SportCommentariesByFixtureIdResponseSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: SportCommentariesByFixtureIdResponse


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: SportCommentariesByFixtureIdResponse


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _commentaries_by_fixture_id_mapped_args(
        self,
        fixture_id: int,
        version: typing.Optional[str] = None,
        sport: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if version is not None:
            _path_params["version"] = version
        if sport is not None:
            _path_params["sport"] = sport
        if fixture_id is not None:
            _path_params["fixtureId"] = fixture_id
        args.path = _path_params
        return args

    async def _acommentaries_by_fixture_id_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        By Fixture ID
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
            request_path_fixture_id,
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
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
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


    def _commentaries_by_fixture_id_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        By Fixture ID
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
            request_path_fixture_id,
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
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CommentariesByFixtureId(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acommentaries_by_fixture_id(
        self,
        fixture_id: int,
        version: typing.Optional[str] = None,
        sport: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._commentaries_by_fixture_id_mapped_args(
            fixture_id=fixture_id,
            version=version,
            sport=sport,
        )
        return await self._acommentaries_by_fixture_id_oapg(
            path_params=args.path,
        )
    
    def commentaries_by_fixture_id(
        self,
        fixture_id: int,
        version: typing.Optional[str] = None,
        sport: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._commentaries_by_fixture_id_mapped_args(
            fixture_id=fixture_id,
            version=version,
            sport=sport,
        )
        return self._commentaries_by_fixture_id_oapg(
            path_params=args.path,
        )

class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        fixture_id: int,
        version: typing.Optional[str] = None,
        sport: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._commentaries_by_fixture_id_mapped_args(
            fixture_id=fixture_id,
            version=version,
            sport=sport,
        )
        return await self._acommentaries_by_fixture_id_oapg(
            path_params=args.path,
        )
    
    def get(
        self,
        fixture_id: int,
        version: typing.Optional[str] = None,
        sport: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._commentaries_by_fixture_id_mapped_args(
            fixture_id=fixture_id,
            version=version,
            sport=sport,
        )
        return self._commentaries_by_fixture_id_oapg(
            path_params=args.path,
        )

