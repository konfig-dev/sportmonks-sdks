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
import { OddsBookmakersSearchResponseDataInner } from './odds-bookmakers-search-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { OddsBookmakersSearchResponsePagination } from './odds-bookmakers-search-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { OddsBookmakersSearchResponseRateLimit } from './odds-bookmakers-search-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { OddsBookmakersSearchResponseSubscriptionInner } from './odds-bookmakers-search-response-subscription-inner';

/**
 * 
 * @export
 * @interface OddsBookmakersSearchResponse
 */
export interface OddsBookmakersSearchResponse {
    /**
     * 
     * @type {Array<OddsBookmakersSearchResponseDataInner>}
     * @memberof OddsBookmakersSearchResponse
     */
    'data'?: Array<OddsBookmakersSearchResponseDataInner>;
    /**
     * 
     * @type {OddsBookmakersSearchResponsePagination}
     * @memberof OddsBookmakersSearchResponse
     */
    'pagination'?: OddsBookmakersSearchResponsePagination;
    /**
     * 
     * @type {Array<OddsBookmakersSearchResponseSubscriptionInner>}
     * @memberof OddsBookmakersSearchResponse
     */
    'subscription'?: Array<OddsBookmakersSearchResponseSubscriptionInner>;
    /**
     * 
     * @type {OddsBookmakersSearchResponseRateLimit}
     * @memberof OddsBookmakersSearchResponse
     */
    'rate_limit'?: OddsBookmakersSearchResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof OddsBookmakersSearchResponse
     */
    'timezone'?: string;
}

