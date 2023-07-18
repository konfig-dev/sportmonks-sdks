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
import { SportLeaguesLiveResponseDataInner } from './sport-leagues-live-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportLeaguesLiveResponseRateLimit } from './sport-leagues-live-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportLeaguesLiveResponseSubscriptionInner } from './sport-leagues-live-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportLeaguesLiveResponse
 */
export interface SportLeaguesLiveResponse {
    /**
     * 
     * @type {Array<SportLeaguesLiveResponseDataInner>}
     * @memberof SportLeaguesLiveResponse
     */
    'data'?: Array<SportLeaguesLiveResponseDataInner>;
    /**
     * 
     * @type {Array<SportLeaguesLiveResponseSubscriptionInner>}
     * @memberof SportLeaguesLiveResponse
     */
    'subscription'?: Array<SportLeaguesLiveResponseSubscriptionInner>;
    /**
     * 
     * @type {SportLeaguesLiveResponseRateLimit}
     * @memberof SportLeaguesLiveResponse
     */
    'rate_limit'?: SportLeaguesLiveResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportLeaguesLiveResponse
     */
    'timezone'?: string;
}
