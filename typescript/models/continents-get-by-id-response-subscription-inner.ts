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
import { ContinentsGetByIdResponseSubscriptionInnerPlansInner } from './continents-get-by-id-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface ContinentsGetByIdResponseSubscriptionInner
 */
export interface ContinentsGetByIdResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof ContinentsGetByIdResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<ContinentsGetByIdResponseSubscriptionInnerPlansInner>}
     * @memberof ContinentsGetByIdResponseSubscriptionInner
     */
    'plans'?: Array<ContinentsGetByIdResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof ContinentsGetByIdResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof ContinentsGetByIdResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}
