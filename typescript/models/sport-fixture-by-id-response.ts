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
import { SportFixtureByIdResponseDataInner } from './sport-fixture-by-id-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportFixtureByIdResponsePagination } from './sport-fixture-by-id-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportFixtureByIdResponseRateLimit } from './sport-fixture-by-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportFixtureByIdResponseSubscriptionInner } from './sport-fixture-by-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportFixtureByIdResponse
 */
export interface SportFixtureByIdResponse {
    /**
     * 
     * @type {Array<SportFixtureByIdResponseDataInner>}
     * @memberof SportFixtureByIdResponse
     */
    'data'?: Array<SportFixtureByIdResponseDataInner>;
    /**
     * 
     * @type {SportFixtureByIdResponsePagination}
     * @memberof SportFixtureByIdResponse
     */
    'pagination'?: SportFixtureByIdResponsePagination;
    /**
     * 
     * @type {Array<SportFixtureByIdResponseSubscriptionInner>}
     * @memberof SportFixtureByIdResponse
     */
    'subscription'?: Array<SportFixtureByIdResponseSubscriptionInner>;
    /**
     * 
     * @type {SportFixtureByIdResponseRateLimit}
     * @memberof SportFixtureByIdResponse
     */
    'rate_limit'?: SportFixtureByIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportFixtureByIdResponse
     */
    'timezone'?: string;
}

