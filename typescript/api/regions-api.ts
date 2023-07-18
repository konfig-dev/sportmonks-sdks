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
import { RegionsAllResponse } from '../models';
// @ts-ignore
import { RegionsGetByIdResponse } from '../models';
// @ts-ignore
import { RegionsSearchResponse } from '../models';
import { paginate } from "../pagination/paginate";
import { requestBeforeHook } from '../requestBeforeHook';
import { RegionsApiCustom } from "./regions-api-custom";
/**
 * RegionsApi - axios parameter creator
 * @export
 */
export const RegionsApiAxiosParamCreator = function (configuration?: Configuration) {
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
            const localVarPath = `/{version}/core/regions`
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
         * @param {number} regionId The ID of the region you want to retrieve.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getById: async (version: string, regionId: number, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'version' is not null or undefined
            assertParamExists('getById', 'version', version)
            // verify required parameter 'regionId' is not null or undefined
            assertParamExists('getById', 'regionId', regionId)
            const localVarPath = `/{version}/core/regions/{regionId}`
                .replace(`{${"version"}}`, encodeURIComponent(String(version)))
                .replace(`{${"regionId"}}`, encodeURIComponent(String(regionId)));
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
         * @summary Search
         * @param {string} version The version of the API.
         * @param {string} name The name you want to search on
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        search: async (version: string, name: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'version' is not null or undefined
            assertParamExists('search', 'version', version)
            // verify required parameter 'name' is not null or undefined
            assertParamExists('search', 'name', name)
            const localVarPath = `/{version}/core/regions/search/{name}`
                .replace(`{${"version"}}`, encodeURIComponent(String(version)))
                .replace(`{${"name"}}`, encodeURIComponent(String(name)));
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
 * RegionsApi - functional programming interface
 * @export
 */
export const RegionsApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = RegionsApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary All
         * @param {RegionsApiAllRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async all(requestParameters: RegionsApiAllRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<RegionsAllResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.all(requestParameters.version, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * 
         * @summary By ID
         * @param {RegionsApiGetByIdRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getById(requestParameters: RegionsApiGetByIdRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<RegionsGetByIdResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getById(requestParameters.version, requestParameters.regionId, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * 
         * @summary Search
         * @param {RegionsApiSearchRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async search(requestParameters: RegionsApiSearchRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<RegionsSearchResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.search(requestParameters.version, requestParameters.name, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * RegionsApi - factory interface
 * @export
 */
export const RegionsApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = RegionsApiFp(configuration)
    return {
        /**
         * 
         * @summary All
         * @param {RegionsApiAllRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        all(requestParameters: RegionsApiAllRequest, options?: AxiosRequestConfig): AxiosPromise<RegionsAllResponse> {
            return localVarFp.all(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary By ID
         * @param {RegionsApiGetByIdRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getById(requestParameters: RegionsApiGetByIdRequest, options?: AxiosRequestConfig): AxiosPromise<RegionsGetByIdResponse> {
            return localVarFp.getById(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary Search
         * @param {RegionsApiSearchRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        search(requestParameters: RegionsApiSearchRequest, options?: AxiosRequestConfig): AxiosPromise<RegionsSearchResponse> {
            return localVarFp.search(requestParameters, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for all operation in RegionsApi.
 * @export
 * @interface RegionsApiAllRequest
 */
export type RegionsApiAllRequest = {
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof RegionsApiAll
    */
    readonly version: string
    
}

/**
 * Request parameters for getById operation in RegionsApi.
 * @export
 * @interface RegionsApiGetByIdRequest
 */
export type RegionsApiGetByIdRequest = {
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof RegionsApiGetById
    */
    readonly version: string
    
    /**
    * The ID of the region you want to retrieve.
    * @type {number}
    * @memberof RegionsApiGetById
    */
    readonly regionId: number
    
}

/**
 * Request parameters for search operation in RegionsApi.
 * @export
 * @interface RegionsApiSearchRequest
 */
export type RegionsApiSearchRequest = {
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof RegionsApiSearch
    */
    readonly version: string
    
    /**
    * The name you want to search on
    * @type {string}
    * @memberof RegionsApiSearch
    */
    readonly name: string
    
}

/**
 * RegionsApi - object-oriented interface
 * @export
 * @class RegionsApi
 * @extends {BaseAPI}
 */
export class RegionsApi extends RegionsApiCustom {
    /**
     * 
     * @summary All
     * @param {RegionsApiAllRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof RegionsApi
     */
    public all(requestParameters: RegionsApiAllRequest, options?: AxiosRequestConfig) {
        return RegionsApiFp(this.configuration).all(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary By ID
     * @param {RegionsApiGetByIdRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof RegionsApi
     */
    public getById(requestParameters: RegionsApiGetByIdRequest, options?: AxiosRequestConfig) {
        return RegionsApiFp(this.configuration).getById(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary Search
     * @param {RegionsApiSearchRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof RegionsApi
     */
    public search(requestParameters: RegionsApiSearchRequest, options?: AxiosRequestConfig) {
        return RegionsApiFp(this.configuration).search(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }
}