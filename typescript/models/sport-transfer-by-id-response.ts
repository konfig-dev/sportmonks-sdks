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
import { SportTransferByIdResponseData } from './sport-transfer-by-id-response-data';
// May contain unused imports in some cases
// @ts-ignore
import { SportTransferByIdResponseRateLimit } from './sport-transfer-by-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportTransferByIdResponseSubscriptionInner } from './sport-transfer-by-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportTransferByIdResponse
 */
export interface SportTransferByIdResponse {
    /**
     * 
     * @type {SportTransferByIdResponseData}
     * @memberof SportTransferByIdResponse
     */
    'data'?: SportTransferByIdResponseData;
    /**
     * 
     * @type {Array<SportTransferByIdResponseSubscriptionInner>}
     * @memberof SportTransferByIdResponse
     */
    'subscription'?: Array<SportTransferByIdResponseSubscriptionInner>;
    /**
     * 
     * @type {SportTransferByIdResponseRateLimit}
     * @memberof SportTransferByIdResponse
     */
    'rate_limit'?: SportTransferByIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportTransferByIdResponse
     */
    'timezone'?: string;
}

