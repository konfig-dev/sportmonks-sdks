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
import { OddsMarketsAllResponseDataInnerLegacyId } from './odds-markets-all-response-data-inner-legacy-id';

/**
 * 
 * @export
 * @interface OddsMarketsAllResponseDataInner
 */
export interface OddsMarketsAllResponseDataInner {
    /**
     * 
     * @type {number}
     * @memberof OddsMarketsAllResponseDataInner
     */
    'id'?: number;
    /**
     * 
     * @type {OddsMarketsAllResponseDataInnerLegacyId}
     * @memberof OddsMarketsAllResponseDataInner
     */
    'legacy_id'?: OddsMarketsAllResponseDataInnerLegacyId;
    /**
     * 
     * @type {string}
     * @memberof OddsMarketsAllResponseDataInner
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof OddsMarketsAllResponseDataInner
     */
    'developer_name'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof OddsMarketsAllResponseDataInner
     */
    'has_winning_calculations'?: boolean;
}

