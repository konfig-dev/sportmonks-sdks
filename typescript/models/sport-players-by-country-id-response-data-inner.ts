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
import { SportPlayersByCountryIdResponseDataInnerDetailedPositionId } from './sport-players-by-country-id-response-data-inner-detailed-position-id';
// May contain unused imports in some cases
// @ts-ignore
import { SportPlayersByCountryIdResponseDataInnerHeight } from './sport-players-by-country-id-response-data-inner-height';
// May contain unused imports in some cases
// @ts-ignore
import { SportPlayersByCountryIdResponseDataInnerPositionId } from './sport-players-by-country-id-response-data-inner-position-id';
// May contain unused imports in some cases
// @ts-ignore
import { SportPlayersByCountryIdResponseDataInnerWeight } from './sport-players-by-country-id-response-data-inner-weight';

/**
 * 
 * @export
 * @interface SportPlayersByCountryIdResponseDataInner
 */
export interface SportPlayersByCountryIdResponseDataInner {
    /**
     * 
     * @type {number}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'sport_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'country_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'nationality_id'?: number;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'city_id'?: string | null;
    /**
     * 
     * @type {SportPlayersByCountryIdResponseDataInnerPositionId}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'position_id'?: SportPlayersByCountryIdResponseDataInnerPositionId;
    /**
     * 
     * @type {SportPlayersByCountryIdResponseDataInnerDetailedPositionId}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'detailed_position_id'?: SportPlayersByCountryIdResponseDataInnerDetailedPositionId;
    /**
     * 
     * @type {number}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'type_id'?: number;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'common_name'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'firstname'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'lastname'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'display_name'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'image_path'?: string;
    /**
     * 
     * @type {SportPlayersByCountryIdResponseDataInnerHeight}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'height'?: SportPlayersByCountryIdResponseDataInnerHeight;
    /**
     * 
     * @type {SportPlayersByCountryIdResponseDataInnerWeight}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'weight'?: SportPlayersByCountryIdResponseDataInnerWeight;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'date_of_birth'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersByCountryIdResponseDataInner
     */
    'gender'?: string;
}
