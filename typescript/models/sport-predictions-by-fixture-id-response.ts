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
import { SportPredictionsByFixtureIdResponseDataInner } from './sport-predictions-by-fixture-id-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportPredictionsByFixtureIdResponsePagination } from './sport-predictions-by-fixture-id-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportPredictionsByFixtureIdResponseRateLimit } from './sport-predictions-by-fixture-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportPredictionsByFixtureIdResponseSubscriptionInner } from './sport-predictions-by-fixture-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportPredictionsByFixtureIdResponse
 */
export interface SportPredictionsByFixtureIdResponse {
    /**
     * 
     * @type {Array<SportPredictionsByFixtureIdResponseDataInner>}
     * @memberof SportPredictionsByFixtureIdResponse
     */
    'data'?: Array<SportPredictionsByFixtureIdResponseDataInner>;
    /**
     * 
     * @type {SportPredictionsByFixtureIdResponsePagination}
     * @memberof SportPredictionsByFixtureIdResponse
     */
    'pagination'?: SportPredictionsByFixtureIdResponsePagination;
    /**
     * 
     * @type {Array<SportPredictionsByFixtureIdResponseSubscriptionInner>}
     * @memberof SportPredictionsByFixtureIdResponse
     */
    'subscription'?: Array<SportPredictionsByFixtureIdResponseSubscriptionInner>;
    /**
     * 
     * @type {SportPredictionsByFixtureIdResponseRateLimit}
     * @memberof SportPredictionsByFixtureIdResponse
     */
    'rate_limit'?: SportPredictionsByFixtureIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportPredictionsByFixtureIdResponse
     */
    'timezone'?: string;
}
