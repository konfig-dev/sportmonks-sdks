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
import { SportStandingsBySeasonIdResponseDataInner } from './sport-standings-by-season-id-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportStandingsBySeasonIdResponseRateLimit } from './sport-standings-by-season-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportStandingsBySeasonIdResponseSubscriptionInner } from './sport-standings-by-season-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportStandingsBySeasonIdResponse
 */
export interface SportStandingsBySeasonIdResponse {
    /**
     * 
     * @type {Array<SportStandingsBySeasonIdResponseDataInner>}
     * @memberof SportStandingsBySeasonIdResponse
     */
    'data'?: Array<SportStandingsBySeasonIdResponseDataInner>;
    /**
     * 
     * @type {Array<SportStandingsBySeasonIdResponseSubscriptionInner>}
     * @memberof SportStandingsBySeasonIdResponse
     */
    'subscription'?: Array<SportStandingsBySeasonIdResponseSubscriptionInner>;
    /**
     * 
     * @type {SportStandingsBySeasonIdResponseRateLimit}
     * @memberof SportStandingsBySeasonIdResponse
     */
    'rate_limit'?: SportStandingsBySeasonIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportStandingsBySeasonIdResponse
     */
    'timezone'?: string;
}
