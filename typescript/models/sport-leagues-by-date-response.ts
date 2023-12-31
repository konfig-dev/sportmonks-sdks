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
import { SportLeaguesByDateResponseDataInner } from './sport-leagues-by-date-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportLeaguesByDateResponsePagination } from './sport-leagues-by-date-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportLeaguesByDateResponseRateLimit } from './sport-leagues-by-date-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportLeaguesByDateResponseSubscriptionInner } from './sport-leagues-by-date-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportLeaguesByDateResponse
 */
export interface SportLeaguesByDateResponse {
    /**
     * 
     * @type {Array<SportLeaguesByDateResponseDataInner>}
     * @memberof SportLeaguesByDateResponse
     */
    'data'?: Array<SportLeaguesByDateResponseDataInner>;
    /**
     * 
     * @type {SportLeaguesByDateResponsePagination}
     * @memberof SportLeaguesByDateResponse
     */
    'pagination'?: SportLeaguesByDateResponsePagination;
    /**
     * 
     * @type {Array<SportLeaguesByDateResponseSubscriptionInner>}
     * @memberof SportLeaguesByDateResponse
     */
    'subscription'?: Array<SportLeaguesByDateResponseSubscriptionInner>;
    /**
     * 
     * @type {SportLeaguesByDateResponseRateLimit}
     * @memberof SportLeaguesByDateResponse
     */
    'rate_limit'?: SportLeaguesByDateResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportLeaguesByDateResponse
     */
    'timezone'?: string;
}

