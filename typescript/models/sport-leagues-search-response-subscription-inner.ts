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
import { SportLeaguesSearchResponseSubscriptionInnerPlansInner } from './sport-leagues-search-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportLeaguesSearchResponseSubscriptionInner
 */
export interface SportLeaguesSearchResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof SportLeaguesSearchResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<SportLeaguesSearchResponseSubscriptionInnerPlansInner>}
     * @memberof SportLeaguesSearchResponseSubscriptionInner
     */
    'plans'?: Array<SportLeaguesSearchResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportLeaguesSearchResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportLeaguesSearchResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}
