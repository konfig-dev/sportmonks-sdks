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
import { SportOddsPreMatchByFixtureIdResponseDataInner } from './sport-odds-pre-match-by-fixture-id-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportOddsPreMatchByFixtureIdResponseRateLimit } from './sport-odds-pre-match-by-fixture-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportOddsPreMatchByFixtureIdResponseSubscriptionInner } from './sport-odds-pre-match-by-fixture-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportOddsPreMatchByFixtureIdResponse
 */
export interface SportOddsPreMatchByFixtureIdResponse {
    /**
     * 
     * @type {Array<SportOddsPreMatchByFixtureIdResponseDataInner>}
     * @memberof SportOddsPreMatchByFixtureIdResponse
     */
    'data'?: Array<SportOddsPreMatchByFixtureIdResponseDataInner>;
    /**
     * 
     * @type {Array<SportOddsPreMatchByFixtureIdResponseSubscriptionInner>}
     * @memberof SportOddsPreMatchByFixtureIdResponse
     */
    'subscription'?: Array<SportOddsPreMatchByFixtureIdResponseSubscriptionInner>;
    /**
     * 
     * @type {SportOddsPreMatchByFixtureIdResponseRateLimit}
     * @memberof SportOddsPreMatchByFixtureIdResponse
     */
    'rate_limit'?: SportOddsPreMatchByFixtureIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureIdResponse
     */
    'timezone'?: string;
}

