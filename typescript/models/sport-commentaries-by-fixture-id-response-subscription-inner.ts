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
import { SportCommentariesByFixtureIdResponseSubscriptionInnerPlansInner } from './sport-commentaries-by-fixture-id-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportCommentariesByFixtureIdResponseSubscriptionInner
 */
export interface SportCommentariesByFixtureIdResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof SportCommentariesByFixtureIdResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<SportCommentariesByFixtureIdResponseSubscriptionInnerPlansInner>}
     * @memberof SportCommentariesByFixtureIdResponseSubscriptionInner
     */
    'plans'?: Array<SportCommentariesByFixtureIdResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportCommentariesByFixtureIdResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportCommentariesByFixtureIdResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}
