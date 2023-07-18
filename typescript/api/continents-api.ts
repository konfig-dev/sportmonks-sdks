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
import { ContinentsAllResponse } from '../models';
// @ts-ignore
import { ContinentsGetByIdResponse } from '../models';
import { paginate } from "../pagination/paginate";
import { requestBeforeHook } from '../requestBeforeHook';
import { ContinentsApiCustom } from "./continents-api-custom";
/**
 * ContinentsApi - axios parameter creator
 * @export
 */
export const ContinentsApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary All
         * @param {string} [version] The version of the API.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        all: async (version?: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/{version}/core/continents`
                .replace(`{${"version"}}`, encodeURIComponent(String(version !== undefined ? version : `-version-`)));
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
            await setApiKeyToObject({ object: localVarHeaderParameter, keyParamName: "Authorization", configuration })

    
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
         * @param {number} continentId The ID of the continent you want to retrieve
         * @param {string} [version] The version of the API.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getById: async (continentId: number, version?: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'continentId' is not null or undefined
            assertParamExists('getById', 'continentId', continentId)
            const localVarPath = `/{version}/core/continents/{continentId}`
                .replace(`{${"version"}}`, encodeURIComponent(String(version !== undefined ? version : `-version-`)))
                .replace(`{${"continentId"}}`, encodeURIComponent(String(continentId !== undefined ? continentId : `-continentId-`)));
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
            await setApiKeyToObject({ object: localVarHeaderParameter, keyParamName: "Authorization", configuration })

    
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
 * ContinentsApi - functional programming interface
 * @export
 */
export const ContinentsApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = ContinentsApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary All
         * @param {ContinentsApiAllRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async all(requestParameters: ContinentsApiAllRequest = {}, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ContinentsAllResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.all(requestParameters.version, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * 
         * @summary By ID
         * @param {ContinentsApiGetByIdRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getById(requestParameters: ContinentsApiGetByIdRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<ContinentsGetByIdResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getById(requestParameters.continentId, requestParameters.version, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * ContinentsApi - factory interface
 * @export
 */
export const ContinentsApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = ContinentsApiFp(configuration)
    return {
        /**
         * 
         * @summary All
         * @param {ContinentsApiAllRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        all(requestParameters: ContinentsApiAllRequest = {}, options?: AxiosRequestConfig): AxiosPromise<ContinentsAllResponse> {
            return localVarFp.all(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary By ID
         * @param {ContinentsApiGetByIdRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getById(requestParameters: ContinentsApiGetByIdRequest, options?: AxiosRequestConfig): AxiosPromise<ContinentsGetByIdResponse> {
            return localVarFp.getById(requestParameters, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for all operation in ContinentsApi.
 * @export
 * @interface ContinentsApiAllRequest
 */
export type ContinentsApiAllRequest = {
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof ContinentsApiAll
    */
    readonly version?: string
    
}

/**
 * Request parameters for getById operation in ContinentsApi.
 * @export
 * @interface ContinentsApiGetByIdRequest
 */
export type ContinentsApiGetByIdRequest = {
    
    /**
    * The ID of the continent you want to retrieve
    * @type {number}
    * @memberof ContinentsApiGetById
    */
    readonly continentId: number
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof ContinentsApiGetById
    */
    readonly version?: string
    
}

/**
 * ContinentsApi - object-oriented interface
 * @export
 * @class ContinentsApi
 * @extends {BaseAPI}
 */
export class ContinentsApi extends ContinentsApiCustom {
    /**
     * 
     * @summary All
     * @param {ContinentsApiAllRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ContinentsApi
     */
    public all(requestParameters: ContinentsApiAllRequest = {}, options?: AxiosRequestConfig) {
        return ContinentsApiFp(this.configuration).all(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary By ID
     * @param {ContinentsApiGetByIdRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof ContinentsApi
     */
    public getById(requestParameters: ContinentsApiGetByIdRequest, options?: AxiosRequestConfig) {
        return ContinentsApiFp(this.configuration).getById(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }
}
