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
import { OddsBookmakersSearchResponseSubscriptionInnerPlansInner } from './odds-bookmakers-search-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface OddsBookmakersSearchResponseSubscriptionInner
 */
export interface OddsBookmakersSearchResponseSubscriptionInner {
    /**
     * 
     * @type {Array<string>}
     * @memberof OddsBookmakersSearchResponseSubscriptionInner
     */
    'meta'?: Array<string>;
    /**
     * 
     * @type {Array<OddsBookmakersSearchResponseSubscriptionInnerPlansInner>}
     * @memberof OddsBookmakersSearchResponseSubscriptionInner
     */
    'plans'?: Array<OddsBookmakersSearchResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof OddsBookmakersSearchResponseSubscriptionInner
     */
    'add_ons'?: Array<string>;
    /**
     * 
     * @type {Array<string>}
     * @memberof OddsBookmakersSearchResponseSubscriptionInner
     */
    'widgets'?: Array<string>;
}
