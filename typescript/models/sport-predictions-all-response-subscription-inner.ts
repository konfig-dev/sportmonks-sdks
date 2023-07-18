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
import { SportPredictionsAllResponseSubscriptionInnerAddOnsInner } from './sport-predictions-all-response-subscription-inner-add-ons-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportPredictionsAllResponseSubscriptionInnerPlansInner } from './sport-predictions-all-response-subscription-inner-plans-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta } from './sport-standings-live-by-league-id-response-subscription-inner-meta';

/**
 * 
 * @export
 * @interface SportPredictionsAllResponseSubscriptionInner
 */
export interface SportPredictionsAllResponseSubscriptionInner {
    /**
     * 
     * @type {SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta}
     * @memberof SportPredictionsAllResponseSubscriptionInner
     */
    'meta'?: SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta;
    /**
     * 
     * @type {Array<SportPredictionsAllResponseSubscriptionInnerPlansInner>}
     * @memberof SportPredictionsAllResponseSubscriptionInner
     */
    'plans'?: Array<SportPredictionsAllResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<SportPredictionsAllResponseSubscriptionInnerAddOnsInner>}
     * @memberof SportPredictionsAllResponseSubscriptionInner
     */
    'add_ons'?: Array<SportPredictionsAllResponseSubscriptionInnerAddOnsInner>;
}
