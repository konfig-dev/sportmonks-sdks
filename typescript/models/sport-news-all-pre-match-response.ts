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
import { SportNewsAllPreMatchResponseDataInner } from './sport-news-all-pre-match-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportNewsAllPreMatchResponsePagination } from './sport-news-all-pre-match-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportNewsAllPreMatchResponseRateLimit } from './sport-news-all-pre-match-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportNewsAllPreMatchResponseSubscriptionInner } from './sport-news-all-pre-match-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportNewsAllPreMatchResponse
 */
export interface SportNewsAllPreMatchResponse {
    /**
     * 
     * @type {Array<SportNewsAllPreMatchResponseDataInner>}
     * @memberof SportNewsAllPreMatchResponse
     */
    'data'?: Array<SportNewsAllPreMatchResponseDataInner>;
    /**
     * 
     * @type {SportNewsAllPreMatchResponsePagination}
     * @memberof SportNewsAllPreMatchResponse
     */
    'pagination'?: SportNewsAllPreMatchResponsePagination;
    /**
     * 
     * @type {Array<SportNewsAllPreMatchResponseSubscriptionInner>}
     * @memberof SportNewsAllPreMatchResponse
     */
    'subscription'?: Array<SportNewsAllPreMatchResponseSubscriptionInner>;
    /**
     * 
     * @type {SportNewsAllPreMatchResponseRateLimit}
     * @memberof SportNewsAllPreMatchResponse
     */
    'rate_limit'?: SportNewsAllPreMatchResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportNewsAllPreMatchResponse
     */
    'timezone'?: string;
}
