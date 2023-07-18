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
import { OddsMarketsSearchResponseDataInner } from './odds-markets-search-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { OddsMarketsSearchResponsePagination } from './odds-markets-search-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { OddsMarketsSearchResponseRateLimit } from './odds-markets-search-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { OddsMarketsSearchResponseSubscriptionInner } from './odds-markets-search-response-subscription-inner';

/**
 * 
 * @export
 * @interface OddsMarketsSearchResponse
 */
export interface OddsMarketsSearchResponse {
    /**
     * 
     * @type {Array<OddsMarketsSearchResponseDataInner>}
     * @memberof OddsMarketsSearchResponse
     */
    'data'?: Array<OddsMarketsSearchResponseDataInner>;
    /**
     * 
     * @type {OddsMarketsSearchResponsePagination}
     * @memberof OddsMarketsSearchResponse
     */
    'pagination'?: OddsMarketsSearchResponsePagination;
    /**
     * 
     * @type {Array<OddsMarketsSearchResponseSubscriptionInner>}
     * @memberof OddsMarketsSearchResponse
     */
    'subscription'?: Array<OddsMarketsSearchResponseSubscriptionInner>;
    /**
     * 
     * @type {OddsMarketsSearchResponseRateLimit}
     * @memberof OddsMarketsSearchResponse
     */
    'rate_limit'?: OddsMarketsSearchResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof OddsMarketsSearchResponse
     */
    'timezone'?: string;
}

