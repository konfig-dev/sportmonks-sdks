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
import { OddsBookmakersMappingByFixtureIdResponseDataInner } from './odds-bookmakers-mapping-by-fixture-id-response-data-inner';
// May contain unused imports in some cases
// @ts-ignore
import { OddsBookmakersMappingByFixtureIdResponseRateLimit } from './odds-bookmakers-mapping-by-fixture-id-response-rate-limit';
// May contain unused imports in some cases
// @ts-ignore
import { OddsBookmakersMappingByFixtureIdResponseSubscriptionInner } from './odds-bookmakers-mapping-by-fixture-id-response-subscription-inner';

/**
 * 
 * @export
 * @interface OddsBookmakersMappingByFixtureIdResponse
 */
export interface OddsBookmakersMappingByFixtureIdResponse {
    /**
     * 
     * @type {Array<OddsBookmakersMappingByFixtureIdResponseDataInner>}
     * @memberof OddsBookmakersMappingByFixtureIdResponse
     */
    'data'?: Array<OddsBookmakersMappingByFixtureIdResponseDataInner>;
    /**
     * 
     * @type {Array<OddsBookmakersMappingByFixtureIdResponseSubscriptionInner>}
     * @memberof OddsBookmakersMappingByFixtureIdResponse
     */
    'subscription'?: Array<OddsBookmakersMappingByFixtureIdResponseSubscriptionInner>;
    /**
     * 
     * @type {OddsBookmakersMappingByFixtureIdResponseRateLimit}
     * @memberof OddsBookmakersMappingByFixtureIdResponse
     */
    'rate_limit'?: OddsBookmakersMappingByFixtureIdResponseRateLimit;
    /**
     * 
     * @type {string}
     * @memberof OddsBookmakersMappingByFixtureIdResponse
     */
    'timezone'?: string;
}

