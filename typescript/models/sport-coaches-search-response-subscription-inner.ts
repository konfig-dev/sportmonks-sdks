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
import { SportCoachesSearchResponseSubscriptionInnerPlansInner } from './sport-coaches-search-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportCoachesSearchResponseSubscriptionInner
 */
export interface SportCoachesSearchResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof SportCoachesSearchResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<SportCoachesSearchResponseSubscriptionInnerPlansInner>}
     * @memberof SportCoachesSearchResponseSubscriptionInner
     */
    'plans'?: Array<SportCoachesSearchResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportCoachesSearchResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportCoachesSearchResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}
