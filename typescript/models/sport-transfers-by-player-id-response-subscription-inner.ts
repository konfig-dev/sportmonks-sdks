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
import { SportTransfersByPlayerIdResponseSubscriptionInnerPlansInner } from './sport-transfers-by-player-id-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportTransfersByPlayerIdResponseSubscriptionInner
 */
export interface SportTransfersByPlayerIdResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof SportTransfersByPlayerIdResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<SportTransfersByPlayerIdResponseSubscriptionInnerPlansInner>}
     * @memberof SportTransfersByPlayerIdResponseSubscriptionInner
     */
    'plans'?: Array<SportTransfersByPlayerIdResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportTransfersByPlayerIdResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportTransfersByPlayerIdResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}

