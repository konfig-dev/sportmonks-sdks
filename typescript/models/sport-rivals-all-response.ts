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
import { SportRivalsAllResponseDataInner } from './sport-rivals-all-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportRivalsAllResponsePagination } from './sport-rivals-all-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportRivalsAllResponseRateLimit } from './sport-rivals-all-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportRivalsAllResponseSubscriptionInner } from './sport-rivals-all-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportRivalsAllResponse
 */
export interface SportRivalsAllResponse {
    /**
     * 
     * @type {Array<SportRivalsAllResponseDataInner>}
     * @memberof SportRivalsAllResponse
     */
    'data'?: Array<SportRivalsAllResponseDataInner>;
    /**
     * 
     * @type {SportRivalsAllResponsePagination}
     * @memberof SportRivalsAllResponse
     */
    'pagination'?: SportRivalsAllResponsePagination;
    /**
     * 
     * @type {Array<SportRivalsAllResponseSubscriptionInner>}
     * @memberof SportRivalsAllResponse
     */
    'subscription'?: Array<SportRivalsAllResponseSubscriptionInner>;
    /**
     * 
     * @type {SportRivalsAllResponseRateLimit}
     * @memberof SportRivalsAllResponse
     */
    'rate_limit'?: SportRivalsAllResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportRivalsAllResponse
     */
    'timezone'?: string;
}

