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
import { SportTeamsByIdResponseSubscriptionInnerPlansInner } from './sport-teams-by-id-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportTeamsByIdResponseSubscriptionInner
 */
export interface SportTeamsByIdResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof SportTeamsByIdResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<SportTeamsByIdResponseSubscriptionInnerPlansInner>}
     * @memberof SportTeamsByIdResponseSubscriptionInner
     */
    'plans'?: Array<SportTeamsByIdResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportTeamsByIdResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportTeamsByIdResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}

