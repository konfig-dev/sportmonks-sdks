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
import { SportCommentariesAllResponseDataInner } from './sport-commentaries-all-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportCommentariesAllResponsePagination } from './sport-commentaries-all-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportCommentariesAllResponseRateLimit } from './sport-commentaries-all-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportCommentariesAllResponseSubscriptionInner } from './sport-commentaries-all-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportCommentariesAllResponse
 */
export interface SportCommentariesAllResponse {
    /**
     * 
     * @type {Array<SportCommentariesAllResponseDataInner>}
     * @memberof SportCommentariesAllResponse
     */
    'data'?: Array<SportCommentariesAllResponseDataInner>;
    /**
     * 
     * @type {SportCommentariesAllResponsePagination}
     * @memberof SportCommentariesAllResponse
     */
    'pagination'?: SportCommentariesAllResponsePagination;
    /**
     * 
     * @type {Array<SportCommentariesAllResponseSubscriptionInner>}
     * @memberof SportCommentariesAllResponse
     */
    'subscription'?: Array<SportCommentariesAllResponseSubscriptionInner>;
    /**
     * 
     * @type {SportCommentariesAllResponseRateLimit}
     * @memberof SportCommentariesAllResponse
     */
    'rate_limit'?: SportCommentariesAllResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportCommentariesAllResponse
     */
    'timezone'?: string;
}
