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
import { SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner } from './sport-standings-live-by-league-id-response-subscription-inner-add-ons-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta } from './sport-standings-live-by-league-id-response-subscription-inner-meta';
// May contain unused imports in some cases
// @ts-ignore
import { SportStandingsLiveByLeagueIdResponseSubscriptionInnerPlansInner } from './sport-standings-live-by-league-id-response-subscription-inner-plans-inner';

/**
 * 
 * @export
 * @interface SportStandingsLiveByLeagueIdResponseSubscriptionInner
 */
export interface SportStandingsLiveByLeagueIdResponseSubscriptionInner {
    /**
     * 
     * @type {SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta}
     * @memberof SportStandingsLiveByLeagueIdResponseSubscriptionInner
     */
    'meta'?: SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta;
    /**
     * 
     * @type {Array<SportStandingsLiveByLeagueIdResponseSubscriptionInnerPlansInner>}
     * @memberof SportStandingsLiveByLeagueIdResponseSubscriptionInner
     */
    'plans'?: Array<SportStandingsLiveByLeagueIdResponseSubscriptionInnerPlansInner>;
    /**
     * 
     * @type {Array<SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner>}
     * @memberof SportStandingsLiveByLeagueIdResponseSubscriptionInner
     */
    'add_ons'?: Array<SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner>;
}

