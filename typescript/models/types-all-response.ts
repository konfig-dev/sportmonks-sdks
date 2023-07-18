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
import { TypesAllResponseDataInner } from './types-all-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { TypesAllResponsePagination } from './types-all-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { TypesAllResponseRateLimit } from './types-all-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { TypesAllResponseSubscriptionInner } from './types-all-response-subscription-inner';

/**
 * 
 * @export
 * @interface TypesAllResponse
 */
export interface TypesAllResponse {
    /**
     * 
     * @type {Array<TypesAllResponseDataInner>}
     * @memberof TypesAllResponse
     */
    'data'?: Array<TypesAllResponseDataInner>;
    /**
     * 
     * @type {TypesAllResponsePagination}
     * @memberof TypesAllResponse
     */
    'pagination'?: TypesAllResponsePagination;
    /**
     * 
     * @type {Array<TypesAllResponseSubscriptionInner>}
     * @memberof TypesAllResponse
     */
    'subscription'?: Array<TypesAllResponseSubscriptionInner>;
    /**
     * 
     * @type {TypesAllResponseRateLimit}
     * @memberof TypesAllResponse
     */
    'rate_limit'?: TypesAllResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof TypesAllResponse
     */
    'timezone'?: string;
}
