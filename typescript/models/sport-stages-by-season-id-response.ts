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
import { SportStagesBySeasonIdResponseDataInner } from './sport-stages-by-season-id-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportStagesBySeasonIdResponseRateLimit } from './sport-stages-by-season-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportStagesBySeasonIdResponseSubscriptionInner } from './sport-stages-by-season-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportStagesBySeasonIdResponse
 */
export interface SportStagesBySeasonIdResponse {
    /**
     * 
     * @type {Array<SportStagesBySeasonIdResponseDataInner>}
     * @memberof SportStagesBySeasonIdResponse
     */
    'data'?: Array<SportStagesBySeasonIdResponseDataInner>;
    /**
     * 
     * @type {Array<SportStagesBySeasonIdResponseSubscriptionInner>}
     * @memberof SportStagesBySeasonIdResponse
     */
    'subscription'?: Array<SportStagesBySeasonIdResponseSubscriptionInner>;
    /**
     * 
     * @type {SportStagesBySeasonIdResponseRateLimit}
     * @memberof SportStagesBySeasonIdResponse
     */
    'rate_limit'?: SportStagesBySeasonIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportStagesBySeasonIdResponse
     */
    'timezone'?: string;
}

