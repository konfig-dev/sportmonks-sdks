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
import { CountriesAllResponseSubscriptionInnerPlansInner } from './countries-all-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface CountriesAllResponseSubscriptionInner
 */
export interface CountriesAllResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof CountriesAllResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<CountriesAllResponseSubscriptionInnerPlansInner>}
     * @memberof CountriesAllResponseSubscriptionInner
     */
    'plans'?: Array<CountriesAllResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof CountriesAllResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof CountriesAllResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}

