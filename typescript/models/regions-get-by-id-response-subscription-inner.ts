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
import { RegionsGetByIdResponseSubscriptionInnerPlansInner } from './regions-get-by-id-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface RegionsGetByIdResponseSubscriptionInner
 */
export interface RegionsGetByIdResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof RegionsGetByIdResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<RegionsGetByIdResponseSubscriptionInnerPlansInner>}
     * @memberof RegionsGetByIdResponseSubscriptionInner
     */
    'plans'?: Array<RegionsGetByIdResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof RegionsGetByIdResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof RegionsGetByIdResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}

