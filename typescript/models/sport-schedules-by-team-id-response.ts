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
import { SportSchedulesByTeamIdResponseDataInner } from './sport-schedules-by-team-id-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { SportSchedulesByTeamIdResponseRateLimit } from './sport-schedules-by-team-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { SportSchedulesByTeamIdResponseSubscriptionInner } from './sport-schedules-by-team-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface SportSchedulesByTeamIdResponse
 */
export interface SportSchedulesByTeamIdResponse {
    /**
     * 
     * @type {Array<SportSchedulesByTeamIdResponseDataInner>}
     * @memberof SportSchedulesByTeamIdResponse
     */
    'data'?: Array<SportSchedulesByTeamIdResponseDataInner>;
    /**
     * 
     * @type {Array<SportSchedulesByTeamIdResponseSubscriptionInner>}
     * @memberof SportSchedulesByTeamIdResponse
     */
    'subscription'?: Array<SportSchedulesByTeamIdResponseSubscriptionInner>;
    /**
     * 
     * @type {SportSchedulesByTeamIdResponseRateLimit}
     * @memberof SportSchedulesByTeamIdResponse
     */
    'rate_limit'?: SportSchedulesByTeamIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesByTeamIdResponse
     */
    'timezone'?: string;
}

