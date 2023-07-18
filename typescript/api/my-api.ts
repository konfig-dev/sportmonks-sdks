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
import { MyEnrichmentsResponse } from '../models';
// @ts-ignore
import { MyLeaguesResponse } from '../models';
// @ts-ignore
import { MyResourcesResponse } from '../models';
import { paginate } from "../pagination/paginate";
import { requestBeforeHook } from '../requestBeforeHook';
import { MyApiCustom } from "./my-api-custom";
/**
 * MyApi - axios parameter creator
 * @export
 */
export const MyApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary All
         * @param {string} version The version of the API.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        enrichments: async (version: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'version' is not null or undefined
            assertParamExists('enrichments', 'version', version)
            const localVarPath = `/{version}/my/enrichments`
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
         * @summary All
         * @param {string} version The version of the API.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        leagues: async (version: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'version' is not null or undefined
            assertParamExists('leagues', 'version', version)
            const localVarPath = `/{version}/my/leagues`
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
         * @summary All
         * @param {string} version The version of the API.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        resources: async (version: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'version' is not null or undefined
            assertParamExists('resources', 'version', version)
            const localVarPath = `/{version}/my/resources`
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
    }
};

/**
 * MyApi - functional programming interface
 * @export
 */
export const MyApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = MyApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary All
         * @param {MyApiEnrichmentsRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async enrichments(requestParameters: MyApiEnrichmentsRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<MyEnrichmentsResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.enrichments(requestParameters.version, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * 
         * @summary All
         * @param {MyApiLeaguesRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async leagues(requestParameters: MyApiLeaguesRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<MyLeaguesResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.leagues(requestParameters.version, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * 
         * @summary All
         * @param {MyApiResourcesRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async resources(requestParameters: MyApiResourcesRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<MyResourcesResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.resources(requestParameters.version, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * MyApi - factory interface
 * @export
 */
export const MyApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = MyApiFp(configuration)
    return {
        /**
         * 
         * @summary All
         * @param {MyApiEnrichmentsRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        enrichments(requestParameters: MyApiEnrichmentsRequest, options?: AxiosRequestConfig): AxiosPromise<MyEnrichmentsResponse> {
            return localVarFp.enrichments(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary All
         * @param {MyApiLeaguesRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        leagues(requestParameters: MyApiLeaguesRequest, options?: AxiosRequestConfig): AxiosPromise<MyLeaguesResponse> {
            return localVarFp.leagues(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary All
         * @param {MyApiResourcesRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        resources(requestParameters: MyApiResourcesRequest, options?: AxiosRequestConfig): AxiosPromise<MyResourcesResponse> {
            return localVarFp.resources(requestParameters, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for enrichments operation in MyApi.
 * @export
 * @interface MyApiEnrichmentsRequest
 */
export type MyApiEnrichmentsRequest = {
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof MyApiEnrichments
    */
    readonly version: string
    
}

/**
 * Request parameters for leagues operation in MyApi.
 * @export
 * @interface MyApiLeaguesRequest
 */
export type MyApiLeaguesRequest = {
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof MyApiLeagues
    */
    readonly version: string
    
}

/**
 * Request parameters for resources operation in MyApi.
 * @export
 * @interface MyApiResourcesRequest
 */
export type MyApiResourcesRequest = {
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof MyApiResources
    */
    readonly version: string
    
}

/**
 * MyApi - object-oriented interface
 * @export
 * @class MyApi
 * @extends {BaseAPI}
 */
export class MyApi extends MyApiCustom {
    /**
     * 
     * @summary All
     * @param {MyApiEnrichmentsRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof MyApi
     */
    public enrichments(requestParameters: MyApiEnrichmentsRequest, options?: AxiosRequestConfig) {
        return MyApiFp(this.configuration).enrichments(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary All
     * @param {MyApiLeaguesRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof MyApi
     */
    public leagues(requestParameters: MyApiLeaguesRequest, options?: AxiosRequestConfig) {
        return MyApiFp(this.configuration).leagues(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary All
     * @param {MyApiResourcesRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof MyApi
     */
    public resources(requestParameters: MyApiResourcesRequest, options?: AxiosRequestConfig) {
        return MyApiFp(this.configuration).resources(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }
}