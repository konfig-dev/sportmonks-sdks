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
import { SportTopScorersBySeasonIdResponseDataInner } from './sport-top-scorers-by-season-id-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportTopScorersBySeasonIdResponsePagination } from './sport-top-scorers-by-season-id-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportTopScorersBySeasonIdResponseRateLimit } from './sport-top-scorers-by-season-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportTopScorersBySeasonIdResponseSubscriptionInner } from './sport-top-scorers-by-season-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportTopScorersBySeasonIdResponse
 */
export interface SportTopScorersBySeasonIdResponse {
    /**
     * 
     * @type {Array<SportTopScorersBySeasonIdResponseDataInner>}
     * @memberof SportTopScorersBySeasonIdResponse
     */
    'data'?: Array<SportTopScorersBySeasonIdResponseDataInner>;
    /**
     * 
     * @type {SportTopScorersBySeasonIdResponsePagination}
     * @memberof SportTopScorersBySeasonIdResponse
     */
    'pagination'?: SportTopScorersBySeasonIdResponsePagination;
    /**
     * 
     * @type {Array<SportTopScorersBySeasonIdResponseSubscriptionInner>}
     * @memberof SportTopScorersBySeasonIdResponse
     */
    'subscription'?: Array<SportTopScorersBySeasonIdResponseSubscriptionInner>;
    /**
     * 
     * @type {SportTopScorersBySeasonIdResponseRateLimit}
     * @memberof SportTopScorersBySeasonIdResponse
     */
    'rate_limit'?: SportTopScorersBySeasonIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportTopScorersBySeasonIdResponse
     */
    'timezone'?: string;
}
