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
import { MyResourcesResponseDataInner } from './my-resources-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { MyResourcesResponseRateLimit } from './my-resources-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { MyResourcesResponseSubscriptionInner } from './my-resources-response-subscription-inner';

/**
 * 
 * @export
 * @interface MyResourcesResponse
 */
export interface MyResourcesResponse {
    /**
     * 
     * @type {Array<MyResourcesResponseDataInner>}
     * @memberof MyResourcesResponse
     */
    'data'?: Array<MyResourcesResponseDataInner>;
    /**
     * 
     * @type {Array<MyResourcesResponseSubscriptionInner>}
     * @memberof MyResourcesResponse
     */
    'subscription'?: Array<MyResourcesResponseSubscriptionInner>;
    /**
     * 
     * @type {MyResourcesResponseRateLimit}
     * @memberof MyResourcesResponse
     */
    'rate_limit'?: MyResourcesResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof MyResourcesResponse
     */
    'timezone'?: string;
}

