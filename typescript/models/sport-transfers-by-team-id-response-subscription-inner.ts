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
import { SportTransfersByTeamIdResponseSubscriptionInnerPlansInner } from './sport-transfers-by-team-id-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportTransfersByTeamIdResponseSubscriptionInner
 */
export interface SportTransfersByTeamIdResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof SportTransfersByTeamIdResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<SportTransfersByTeamIdResponseSubscriptionInnerPlansInner>}
     * @memberof SportTransfersByTeamIdResponseSubscriptionInner
     */
    'plans'?: Array<SportTransfersByTeamIdResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportTransfersByTeamIdResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportTransfersByTeamIdResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}

