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
import { SportFixturesAllResponseDataInner } from './sport-fixtures-all-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportFixturesAllResponsePagination } from './sport-fixtures-all-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportFixturesAllResponseRateLimit } from './sport-fixtures-all-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportFixturesAllResponseSubscriptionInner } from './sport-fixtures-all-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportFixturesAllResponse
 */
export interface SportFixturesAllResponse {
    /**
     * 
     * @type {Array<SportFixturesAllResponseDataInner>}
     * @memberof SportFixturesAllResponse
     */
    'data'?: Array<SportFixturesAllResponseDataInner>;
    /**
     * 
     * @type {SportFixturesAllResponsePagination}
     * @memberof SportFixturesAllResponse
     */
    'pagination'?: SportFixturesAllResponsePagination;
    /**
     * 
     * @type {Array<SportFixturesAllResponseSubscriptionInner>}
     * @memberof SportFixturesAllResponse
     */
    'subscription'?: Array<SportFixturesAllResponseSubscriptionInner>;
    /**
     * 
     * @type {SportFixturesAllResponseRateLimit}
     * @memberof SportFixturesAllResponse
     */
    'rate_limit'?: SportFixturesAllResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportFixturesAllResponse
     */
    'timezone'?: string;
}

