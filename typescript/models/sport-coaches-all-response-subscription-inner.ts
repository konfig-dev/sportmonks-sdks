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
import { SportCoachesAllResponseSubscriptionInnerPlansInner } from './sport-coaches-all-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportCoachesAllResponseSubscriptionInner
 */
export interface SportCoachesAllResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof SportCoachesAllResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<SportCoachesAllResponseSubscriptionInnerPlansInner>}
     * @memberof SportCoachesAllResponseSubscriptionInner
     */
    'plans'?: Array<SportCoachesAllResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportCoachesAllResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportCoachesAllResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}
