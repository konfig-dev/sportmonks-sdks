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
import { RegionsSearchResponseSubscriptionInnerPlansInner } from './regions-search-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface RegionsSearchResponseSubscriptionInner
 */
export interface RegionsSearchResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof RegionsSearchResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<RegionsSearchResponseSubscriptionInnerPlansInner>}
     * @memberof RegionsSearchResponseSubscriptionInner
     */
    'plans'?: Array<RegionsSearchResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof RegionsSearchResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof RegionsSearchResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}

