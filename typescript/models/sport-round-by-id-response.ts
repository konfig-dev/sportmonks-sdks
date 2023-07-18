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
import { SportRoundByIdResponseData } from './sport-round-by-id-response-data';
// May contain unused imports in some cases
// @ts-ignore
import { SportRoundByIdResponseRateLimit } from './sport-round-by-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportRoundByIdResponseSubscriptionInner } from './sport-round-by-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportRoundByIdResponse
 */
export interface SportRoundByIdResponse {
    /**
     * 
     * @type {SportRoundByIdResponseData}
     * @memberof SportRoundByIdResponse
     */
    'data'?: SportRoundByIdResponseData;
    /**
     * 
     * @type {Array<SportRoundByIdResponseSubscriptionInner>}
     * @memberof SportRoundByIdResponse
     */
    'subscription'?: Array<SportRoundByIdResponseSubscriptionInner>;
    /**
     * 
     * @type {SportRoundByIdResponseRateLimit}
     * @memberof SportRoundByIdResponse
     */
    'rate_limit'?: SportRoundByIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportRoundByIdResponse
     */
    'timezone'?: string;
}
