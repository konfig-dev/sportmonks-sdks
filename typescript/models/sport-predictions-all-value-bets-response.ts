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
import { SportPredictionsAllValueBetsResponseDataInner } from './sport-predictions-all-value-bets-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportPredictionsAllValueBetsResponsePagination } from './sport-predictions-all-value-bets-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportPredictionsAllValueBetsResponseRateLimit } from './sport-predictions-all-value-bets-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportPredictionsAllValueBetsResponseSubscriptionInner } from './sport-predictions-all-value-bets-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportPredictionsAllValueBetsResponse
 */
export interface SportPredictionsAllValueBetsResponse {
    /**
     * 
     * @type {Array<SportPredictionsAllValueBetsResponseDataInner>}
     * @memberof SportPredictionsAllValueBetsResponse
     */
    'data'?: Array<SportPredictionsAllValueBetsResponseDataInner>;
    /**
     * 
     * @type {SportPredictionsAllValueBetsResponsePagination}
     * @memberof SportPredictionsAllValueBetsResponse
     */
    'pagination'?: SportPredictionsAllValueBetsResponsePagination;
    /**
     * 
     * @type {Array<SportPredictionsAllValueBetsResponseSubscriptionInner>}
     * @memberof SportPredictionsAllValueBetsResponse
     */
    'subscription'?: Array<SportPredictionsAllValueBetsResponseSubscriptionInner>;
    /**
     * 
     * @type {SportPredictionsAllValueBetsResponseRateLimit}
     * @memberof SportPredictionsAllValueBetsResponse
     */
    'rate_limit'?: SportPredictionsAllValueBetsResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportPredictionsAllValueBetsResponse
     */
    'timezone'?: string;
}
