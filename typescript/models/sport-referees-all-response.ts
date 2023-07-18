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
import { SportRefereesAllResponseDataInner } from './sport-referees-all-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportRefereesAllResponsePagination } from './sport-referees-all-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportRefereesAllResponseRateLimit } from './sport-referees-all-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportRefereesAllResponseSubscriptionInner } from './sport-referees-all-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportRefereesAllResponse
 */
export interface SportRefereesAllResponse {
    /**
     * 
     * @type {Array<SportRefereesAllResponseDataInner>}
     * @memberof SportRefereesAllResponse
     */
    'data'?: Array<SportRefereesAllResponseDataInner>;
    /**
     * 
     * @type {SportRefereesAllResponsePagination}
     * @memberof SportRefereesAllResponse
     */
    'pagination'?: SportRefereesAllResponsePagination;
    /**
     * 
     * @type {Array<SportRefereesAllResponseSubscriptionInner>}
     * @memberof SportRefereesAllResponse
     */
    'subscription'?: Array<SportRefereesAllResponseSubscriptionInner>;
    /**
     * 
     * @type {SportRefereesAllResponseRateLimit}
     * @memberof SportRefereesAllResponse
     */
    'rate_limit'?: SportRefereesAllResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportRefereesAllResponse
     */
    'timezone'?: string;
}

