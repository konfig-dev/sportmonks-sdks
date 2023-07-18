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
import { SportTeamsByCountryIdResponseDataInner } from './sport-teams-by-country-id-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportTeamsByCountryIdResponsePagination } from './sport-teams-by-country-id-response-pagination';
// May contain unused imports in some cases
// @ts-ignore
import { SportTeamsByCountryIdResponseRateLimit } from './sport-teams-by-country-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportTeamsByCountryIdResponseSubscriptionInner } from './sport-teams-by-country-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportTeamsByCountryIdResponse
 */
export interface SportTeamsByCountryIdResponse {
    /**
     * 
     * @type {Array<SportTeamsByCountryIdResponseDataInner>}
     * @memberof SportTeamsByCountryIdResponse
     */
    'data'?: Array<SportTeamsByCountryIdResponseDataInner>;
    /**
     * 
     * @type {SportTeamsByCountryIdResponsePagination}
     * @memberof SportTeamsByCountryIdResponse
     */
    'pagination'?: SportTeamsByCountryIdResponsePagination;
    /**
     * 
     * @type {Array<SportTeamsByCountryIdResponseSubscriptionInner>}
     * @memberof SportTeamsByCountryIdResponse
     */
    'subscription'?: Array<SportTeamsByCountryIdResponseSubscriptionInner>;
    /**
     * 
     * @type {SportTeamsByCountryIdResponseRateLimit}
     * @memberof SportTeamsByCountryIdResponse
     */
    'rate_limit'?: SportTeamsByCountryIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportTeamsByCountryIdResponse
     */
    'timezone'?: string;
}

