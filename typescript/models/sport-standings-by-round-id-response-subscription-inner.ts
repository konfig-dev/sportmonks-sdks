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
import { SportStandingsByRoundIdResponseSubscriptionInnerPlansInner } from './sport-standings-by-round-id-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportStandingsByRoundIdResponseSubscriptionInner
 */
export interface SportStandingsByRoundIdResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof SportStandingsByRoundIdResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<SportStandingsByRoundIdResponseSubscriptionInnerPlansInner>}
     * @memberof SportStandingsByRoundIdResponseSubscriptionInner
     */
    'plans'?: Array<SportStandingsByRoundIdResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportStandingsByRoundIdResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportStandingsByRoundIdResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}

