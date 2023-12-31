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
import { CountriesAllResponse } from '../models';
// @ts-ignore
import { CountriesGetByIdResponse } from '../models';
// @ts-ignore
import { CountriesSearchResponse } from '../models';
import { paginate } from "../pagination/paginate";
import { requestBeforeHook } from '../requestBeforeHook';
import { CountriesApiCustom } from "./countries-api-custom";
/**
 * CountriesApi - axios parameter creator
 * @export
 */
export const CountriesApiAxiosParamCreator = function (configuration?: Configuration) {
    return {
        /**
         * 
         * @summary All
         * @param {string} [version] The version of the API.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        all: async (version?: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            const localVarPath = `/{version}/core/countries`
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
         * @param {number} countryId The ID of the country you want to retrieve.
         * @param {string} [version] The version of the API.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getById: async (countryId: number, version?: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'countryId' is not null or undefined
            assertParamExists('getById', 'countryId', countryId)
            const localVarPath = `/{version}/core/countries/{countryId}`
                .replace(`{${"version"}}`, encodeURIComponent(String(version !== undefined ? version : `-version-`)))
                .replace(`{${"countryId"}}`, encodeURIComponent(String(countryId !== undefined ? countryId : `-countryId-`)));
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
         * @summary Search
         * @param {string} name The name you want to search on
         * @param {string} [version] The version of the API.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        search: async (name: string, version?: string, options: AxiosRequestConfig = {}): Promise<RequestArgs> => {
            // verify required parameter 'name' is not null or undefined
            assertParamExists('search', 'name', name)
            const localVarPath = `/{version}/core/countries/search/{name}`
                .replace(`{${"version"}}`, encodeURIComponent(String(version !== undefined ? version : `-version-`)))
                .replace(`{${"name"}}`, encodeURIComponent(String(name !== undefined ? name : `-name-`)));
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
 * CountriesApi - functional programming interface
 * @export
 */
export const CountriesApiFp = function(configuration?: Configuration) {
    const localVarAxiosParamCreator = CountriesApiAxiosParamCreator(configuration)
    return {
        /**
         * 
         * @summary All
         * @param {CountriesApiAllRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async all(requestParameters: CountriesApiAllRequest = {}, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<CountriesAllResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.all(requestParameters.version, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * 
         * @summary By ID
         * @param {CountriesApiGetByIdRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async getById(requestParameters: CountriesApiGetByIdRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<CountriesGetByIdResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.getById(requestParameters.countryId, requestParameters.version, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
        /**
         * 
         * @summary Search
         * @param {CountriesApiSearchRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        async search(requestParameters: CountriesApiSearchRequest, options?: AxiosRequestConfig): Promise<(axios?: AxiosInstance, basePath?: string) => AxiosPromise<CountriesSearchResponse>> {
            const localVarAxiosArgs = await localVarAxiosParamCreator.search(requestParameters.name, requestParameters.version, options);
            return createRequestFunction(localVarAxiosArgs, globalAxios, BASE_PATH, configuration);
        },
    }
};

/**
 * CountriesApi - factory interface
 * @export
 */
export const CountriesApiFactory = function (configuration?: Configuration, basePath?: string, axios?: AxiosInstance) {
    const localVarFp = CountriesApiFp(configuration)
    return {
        /**
         * 
         * @summary All
         * @param {CountriesApiAllRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        all(requestParameters: CountriesApiAllRequest = {}, options?: AxiosRequestConfig): AxiosPromise<CountriesAllResponse> {
            return localVarFp.all(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary By ID
         * @param {CountriesApiGetByIdRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        getById(requestParameters: CountriesApiGetByIdRequest, options?: AxiosRequestConfig): AxiosPromise<CountriesGetByIdResponse> {
            return localVarFp.getById(requestParameters, options).then((request) => request(axios, basePath));
        },
        /**
         * 
         * @summary Search
         * @param {CountriesApiSearchRequest} requestParameters Request parameters.
         * @param {*} [options] Override http request option.
         * @throws {RequiredError}
         */
        search(requestParameters: CountriesApiSearchRequest, options?: AxiosRequestConfig): AxiosPromise<CountriesSearchResponse> {
            return localVarFp.search(requestParameters, options).then((request) => request(axios, basePath));
        },
    };
};

/**
 * Request parameters for all operation in CountriesApi.
 * @export
 * @interface CountriesApiAllRequest
 */
export type CountriesApiAllRequest = {
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof CountriesApiAll
    */
    readonly version?: string
    
}

/**
 * Request parameters for getById operation in CountriesApi.
 * @export
 * @interface CountriesApiGetByIdRequest
 */
export type CountriesApiGetByIdRequest = {
    
    /**
    * The ID of the country you want to retrieve.
    * @type {number}
    * @memberof CountriesApiGetById
    */
    readonly countryId: number
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof CountriesApiGetById
    */
    readonly version?: string
    
}

/**
 * Request parameters for search operation in CountriesApi.
 * @export
 * @interface CountriesApiSearchRequest
 */
export type CountriesApiSearchRequest = {
    
    /**
    * The name you want to search on
    * @type {string}
    * @memberof CountriesApiSearch
    */
    readonly name: string
    
    /**
    * The version of the API.
    * @type {string}
    * @memberof CountriesApiSearch
    */
    readonly version?: string
    
}

/**
 * CountriesApi - object-oriented interface
 * @export
 * @class CountriesApi
 * @extends {BaseAPI}
 */
export class CountriesApi extends CountriesApiCustom {
    /**
     * 
     * @summary All
     * @param {CountriesApiAllRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof CountriesApi
     */
    public all(requestParameters: CountriesApiAllRequest = {}, options?: AxiosRequestConfig) {
        return CountriesApiFp(this.configuration).all(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary By ID
     * @param {CountriesApiGetByIdRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof CountriesApi
     */
    public getById(requestParameters: CountriesApiGetByIdRequest, options?: AxiosRequestConfig) {
        return CountriesApiFp(this.configuration).getById(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }

    /**
     * 
     * @summary Search
     * @param {CountriesApiSearchRequest} requestParameters Request parameters.
     * @param {*} [options] Override http request option.
     * @throws {RequiredError}
     * @memberof CountriesApi
     */
    public search(requestParameters: CountriesApiSearchRequest, options?: AxiosRequestConfig) {
        return CountriesApiFp(this.configuration).search(requestParameters, options).then((request) => request(this.axios, this.basePath));
    }
}
