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
import { SportCoachesAllResponseDataInner } from './sport-coaches-all-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportCoachesAllResponsePagination } from './sport-coaches-all-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportCoachesAllResponseRateLimit } from './sport-coaches-all-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportCoachesAllResponseSubscriptionInner } from './sport-coaches-all-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportCoachesAllResponse
 */
export interface SportCoachesAllResponse {
    /**
     * 
     * @type {Array<SportCoachesAllResponseDataInner>}
     * @memberof SportCoachesAllResponse
     */
    'data'?: Array<SportCoachesAllResponseDataInner>;
    /**
     * 
     * @type {SportCoachesAllResponsePagination}
     * @memberof SportCoachesAllResponse
     */
    'pagination'?: SportCoachesAllResponsePagination;
    /**
     * 
     * @type {Array<SportCoachesAllResponseSubscriptionInner>}
     * @memberof SportCoachesAllResponse
     */
    'subscription'?: Array<SportCoachesAllResponseSubscriptionInner>;
    /**
     * 
     * @type {SportCoachesAllResponseRateLimit}
     * @memberof SportCoachesAllResponse
     */
    'rate_limit'?: SportCoachesAllResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportCoachesAllResponse
     */
    'timezone'?: string;
}

