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
import { SportPlayersAllResponseSubscriptionInnerPlansInner } from './sport-players-all-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportPlayersAllResponseSubscriptionInner
 */
export interface SportPlayersAllResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof SportPlayersAllResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<SportPlayersAllResponseSubscriptionInnerPlansInner>}
     * @memberof SportPlayersAllResponseSubscriptionInner
     */
    'plans'?: Array<SportPlayersAllResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportPlayersAllResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportPlayersAllResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}
