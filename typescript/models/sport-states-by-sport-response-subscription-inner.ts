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
import { SportStatesBySportResponseSubscriptionInnerPlansInner } from './sport-states-by-sport-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportStatesBySportResponseSubscriptionInner
 */
export interface SportStatesBySportResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof SportStatesBySportResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<SportStatesBySportResponseSubscriptionInnerPlansInner>}
     * @memberof SportStatesBySportResponseSubscriptionInner
     */
    'plans'?: Array<SportStatesBySportResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportStatesBySportResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportStatesBySportResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}

