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
import { SportPlayersByCountryIdResponseSubscriptionInnerPlansInner } from './sport-players-by-country-id-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportPlayersByCountryIdResponseSubscriptionInner
 */
export interface SportPlayersByCountryIdResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof SportPlayersByCountryIdResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<SportPlayersByCountryIdResponseSubscriptionInnerPlansInner>}
     * @memberof SportPlayersByCountryIdResponseSubscriptionInner
     */
    'plans'?: Array<SportPlayersByCountryIdResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportPlayersByCountryIdResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportPlayersByCountryIdResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}

