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
import { CitiesSearchResponseSubscriptionInnerPlansInner } from './cities-search-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface CitiesSearchResponseSubscriptionInner
 */
export interface CitiesSearchResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof CitiesSearchResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<CitiesSearchResponseSubscriptionInnerPlansInner>}
     * @memberof CitiesSearchResponseSubscriptionInner
     */
    'plans'?: Array<CitiesSearchResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof CitiesSearchResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof CitiesSearchResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}

