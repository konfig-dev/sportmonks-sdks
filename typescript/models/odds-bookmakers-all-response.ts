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
import { OddsBookmakersAllResponseDataInner } from './odds-bookmakers-all-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { OddsBookmakersAllResponsePagination } from './odds-bookmakers-all-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { OddsBookmakersAllResponseRateLimit } from './odds-bookmakers-all-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { OddsBookmakersAllResponseSubscriptionInner } from './odds-bookmakers-all-response-subscription-inner';

/**
 * 
 * @export
 * @interface OddsBookmakersAllResponse
 */
export interface OddsBookmakersAllResponse {
    /**
     * 
     * @type {Array<OddsBookmakersAllResponseDataInner>}
     * @memberof OddsBookmakersAllResponse
     */
    'data'?: Array<OddsBookmakersAllResponseDataInner>;
    /**
     * 
     * @type {OddsBookmakersAllResponsePagination}
     * @memberof OddsBookmakersAllResponse
     */
    'pagination'?: OddsBookmakersAllResponsePagination;
    /**
     * 
     * @type {Array<OddsBookmakersAllResponseSubscriptionInner>}
     * @memberof OddsBookmakersAllResponse
     */
    'subscription'?: Array<OddsBookmakersAllResponseSubscriptionInner>;
    /**
     * 
     * @type {OddsBookmakersAllResponseRateLimit}
     * @memberof OddsBookmakersAllResponse
     */
    'rate_limit'?: OddsBookmakersAllResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof OddsBookmakersAllResponse
     */
    'timezone'?: string;
}

