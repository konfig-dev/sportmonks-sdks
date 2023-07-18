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

// May contain unused imports in some cases
// @ts-ignore
import { SportCoachesByCountryIdResponseDataInner } from './sport-coaches-by-country-id-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportCoachesByCountryIdResponsePagination } from './sport-coaches-by-country-id-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportCoachesByCountryIdResponseRateLimit } from './sport-coaches-by-country-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportCoachesByCountryIdResponseSubscriptionInner } from './sport-coaches-by-country-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportCoachesByCountryIdResponse
 */
export interface SportCoachesByCountryIdResponse {
    /**
     * 
     * @type {Array<SportCoachesByCountryIdResponseDataInner>}
     * @memberof SportCoachesByCountryIdResponse
     */
    'data'?: Array<SportCoachesByCountryIdResponseDataInner>;
    /**
     * 
     * @type {SportCoachesByCountryIdResponsePagination}
     * @memberof SportCoachesByCountryIdResponse
     */
    'pagination'?: SportCoachesByCountryIdResponsePagination;
    /**
     * 
     * @type {Array<SportCoachesByCountryIdResponseSubscriptionInner>}
     * @memberof SportCoachesByCountryIdResponse
     */
    'subscription'?: Array<SportCoachesByCountryIdResponseSubscriptionInner>;
    /**
     * 
     * @type {SportCoachesByCountryIdResponseRateLimit}
     * @memberof SportCoachesByCountryIdResponse
     */
    'rate_limit'?: SportCoachesByCountryIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportCoachesByCountryIdResponse
     */
    'timezone'?: string;
}

