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
import { SportLeaguesAllResponseDataInner } from './sport-leagues-all-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportLeaguesAllResponsePagination } from './sport-leagues-all-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportLeaguesAllResponseRateLimit } from './sport-leagues-all-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportLeaguesAllResponseSubscriptionInner } from './sport-leagues-all-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportLeaguesAllResponse
 */
export interface SportLeaguesAllResponse {
    /**
     * 
     * @type {Array<SportLeaguesAllResponseDataInner>}
     * @memberof SportLeaguesAllResponse
     */
    'data'?: Array<SportLeaguesAllResponseDataInner>;
    /**
     * 
     * @type {SportLeaguesAllResponsePagination}
     * @memberof SportLeaguesAllResponse
     */
    'pagination'?: SportLeaguesAllResponsePagination;
    /**
     * 
     * @type {Array<SportLeaguesAllResponseSubscriptionInner>}
     * @memberof SportLeaguesAllResponse
     */
    'subscription'?: Array<SportLeaguesAllResponseSubscriptionInner>;
    /**
     * 
     * @type {SportLeaguesAllResponseRateLimit}
     * @memberof SportLeaguesAllResponse
     */
    'rate_limit'?: SportLeaguesAllResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportLeaguesAllResponse
     */
    'timezone'?: string;
}
