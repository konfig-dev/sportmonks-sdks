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
import { SportStateByIdResponseSubscriptionInnerPlansInner } from './sport-state-by-id-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportStateByIdResponseSubscriptionInner
 */
export interface SportStateByIdResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof SportStateByIdResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<SportStateByIdResponseSubscriptionInnerPlansInner>}
     * @memberof SportStateByIdResponseSubscriptionInner
     */
    'plans'?: Array<SportStateByIdResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportStateByIdResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportStateByIdResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}

