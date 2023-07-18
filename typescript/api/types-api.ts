/* tslint:disable */
/* eslint-disable */
/**
 * SportMonks
 * Surpass the competition with superior sports data
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This file is auto generated by Konfig (https://konfigthis.com).
 * Do not edit the class manually.
 */

import globalAxios, { AxiosPromise, AxiosInstance, AxiosRequestConfig } from 'axios';
import { Configuration } from '../configuration';
// Some imports not used depending on template conditions
// @ts-ignore
import { DUMMY_BASE_URL, assertParamExists, setApiKeyToObject, setBasicAuthToObject, setBearerAuthToObject, setSearchParams, serializeDataIfNeeded, toPathString, createRequestFunction, isBrowser } from '../common';
// @ts-ignore
import { BASE_PATH, COLLECTION_FORMATS, RequestArgs, BaseAPI, RequiredError } from '../base';
// @ts-ignore
import { TypesAllResponse } from '../models';
// @ts-ignore
import { TypesGetByIdResponse } from '../models';
import { paginate } from "../pagination/paginate";
import { requestBeforeHook } from '../requestBeforeHook';
import { TypesApiCustom } from "./types-api-custom";
/**
 * TypesApi - axios parameter creator
 * @export
 */
export const TypesApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary All
         * @param {string} version The version of the API.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        all: async (version: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'version' is not null or undefined
            assertParamExists('all', 'version', version)
            const localVarPath = `/{version}/core/types`
                .replace(`{${"version"}}`, encodeURIComponent(String(version)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions: AxiosRequestConfig = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = configuration && !isBrowser() ? { "User-Agent": configuration.userAgent } : {} as any;
            const localVarQueryParameter = {} as any;

            // authentication apikeyAuth required

    
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration
            });

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
        /**
         * 
         * @summary By ID
         * @param {string} version The version of the API.
         * @param {number} typeId The ID of the type you want to retrieve
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getById: async (version: string, typeId: number, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'version' is not null or undefined
            assertParamExists('getById', 'version', version)
            // verify required parameter 'typeId' is not null or undefined
            assertParamExists('getById', 'typeId', typeId)
            const localVarPath = `/{version}/core/types/{typeId}`
                .replace(`{${"version"}}`, encodeURIComponent(String(version)))
                .replace(`{${"typeId"}}`, encodeURIComponent(String(typeId)));
            // use dummy base URL string because the URL constructor only accepts absolute URLs.
            const localVarUrlObj = new URL(localVarPath, DUMMY_BASE_URL);
            let baseOptions;
            if (configuration) {
                baseOptions = configuration.baseOptions;
            }

            const localVarRequestOptions: AxiosRequestConfig = { method: 'GET', ...baseOptions, ...options};
            const localVarHeaderParameter = configuration && !isBrowser() ? { "User-Agent": configuration.userAgent } : {} as any;
            const localVarQueryParameter = {} as any;

            // authentication apikeyAuth required

    
            let headersFromBaseOptions = baseOptions && baseOptions.headers ? baseOptions.headers : {};
            localVarRequestOptions.headers = {...localVarHeaderParameter, ...headersFromBaseOptions, ...options.headers};
            requestBeforeHook({
                queryParameters: localVarQueryParameter,
                requestConfig: localVarRequestOptions,
                path: localVarPath,
                configuration
            });

            setSearchParams(localVarUrlObj, localVarQueryParameter);
            return {
                url: toPathString(localVarUrlObj),
                options: localVarRequestOptions,
            };
        },
    }
};

/**
 * TypesApi - functional programming interface
 * @export
 */
export const TypesApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = TypesApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary All
         * @param {TypesApiAllRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async all(requestParameters: TypesApiAllRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<TypesAllResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.all(requestParameters.version, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * 
         * @summary By ID
         * @param {TypesApiGetByIdRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getById(requestParameters: TypesApiGetByIdRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<TypesGetByIdResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getById(requestParameters.version, requestParameters.typeId, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * TypesApi - factory interface
 * @export
 */
export const TypesApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = TypesApiFp(configuration)
    return {
        /**
         * 
         * @summary All
         * @param {TypesApiAllRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        all(requestParameters: TypesApiAllRequest, options?: AxiosRequestConfig): AxiosPromise<TypesAllResponse> {
            return localVarFp.all(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary By ID
         * @param {TypesApiGetByIdRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getById(requestParameters: TypesApiGetByIdRequest, options?: AxiosRequestConfig): AxiosPromise<TypesGetByIdResponse> {
            return localVarFp.getById(requestParameters, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for all operation in TypesApi.
 * @export
 * @interface TypesApiAllRequest
 */
export type TypesApiAllRequest = {
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof TypesApiAll
    */
    readonly version: string
    
}

/**
 * Request parameters for getById operation in TypesApi.
 * @export
 * @interface TypesApiGetByIdRequest
 */
export type TypesApiGetByIdRequest = {
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof TypesApiGetById
    */
    readonly version: string
    
    /**
    * The ID of the type you want to retrieve
    * @type {number}
    * @memberof TypesApiGetById
    */
    readonly typeId: number
    
}

/**
 * TypesApi - object-oriented interface
 * @export
 * @class TypesApi
 * @extends {BaseAPI}
 */
export class TypesApi extends TypesApiCustom {
    /**
     * 
     * @summary All
     * @param {TypesApiAllRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof TypesApi
     */
    public all(requestParameters: TypesApiAllRequest, options?: AxiosRequestConfig) {
        return TypesApiFp(this.configuration).all(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary By ID
     * @param {TypesApiGetByIdRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof TypesApi
     */
    public getById(requestParameters: TypesApiGetByIdRequest, options?: AxiosRequestConfig) {
        return TypesApiFp(this.configuration).getById(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }
}
