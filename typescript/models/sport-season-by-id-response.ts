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
import { SportSeasonByIdResponseData } from './sport-season-by-id-response-data';
// May contain unused imports in some cases
// @ts-ignore
import { SportSeasonByIdResponseRateLimit } from './sport-season-by-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportSeasonByIdResponseSubscriptionInner } from './sport-season-by-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportSeasonByIdResponse
 */
export interface SportSeasonByIdResponse {
    /**
     * 
     * @type {SportSeasonByIdResponseData}
     * @memberof SportSeasonByIdResponse
     */
    'data'?: SportSeasonByIdResponseData;
    /**
     * 
     * @type {Array<SportSeasonByIdResponseSubscriptionInner>}
     * @memberof SportSeasonByIdResponse
     */
    'subscription'?: Array<SportSeasonByIdResponseSubscriptionInner>;
    /**
     * 
     * @type {SportSeasonByIdResponseRateLimit}
     * @memberof SportSeasonByIdResponse
     */
    'rate_limit'?: SportSeasonByIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportSeasonByIdResponse
     */
    'timezone'?: string;
}

