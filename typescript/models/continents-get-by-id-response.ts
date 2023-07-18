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
import { ContinentsGetByIdResponseData } from './continents-get-by-id-response-data';
// May contain unused imports in some cases
// @ts-ignore
import { ContinentsGetByIdResponseRateLimit } from './continents-get-by-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { ContinentsGetByIdResponseSubscriptionInner } from './continents-get-by-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface ContinentsGetByIdResponse
 */
export interface ContinentsGetByIdResponse {
    /**
     * 
     * @type {ContinentsGetByIdResponseData}
     * @memberof ContinentsGetByIdResponse
     */
    'data'?: ContinentsGetByIdResponseData;
    /**
     * 
     * @type {Array<ContinentsGetByIdResponseSubscriptionInner>}
     * @memberof ContinentsGetByIdResponse
     */
    'subscription'?: Array<ContinentsGetByIdResponseSubscriptionInner>;
    /**
     * 
     * @type {ContinentsGetByIdResponseRateLimit}
     * @memberof ContinentsGetByIdResponse
     */
    'rate_limit'?: ContinentsGetByIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof ContinentsGetByIdResponse
     */
    'timezone'?: string;
}
