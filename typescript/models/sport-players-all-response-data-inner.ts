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
import { SportPlayersAllResponseDataInnerDetailedPositionId } from './sport-players-all-response-data-inner-detailed-position-id';

/**
 * 
 * @export
 * @interface SportPlayersAllResponseDataInner
 */
export interface SportPlayersAllResponseDataInner {
    /**
     * 
     * @type {number}
     * @memberof SportPlayersAllResponseDataInner
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportPlayersAllResponseDataInner
     */
    'sport_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportPlayersAllResponseDataInner
     */
    'country_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportPlayersAllResponseDataInner
     */
    'nationality_id'?: number;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersAllResponseDataInner
     */
    'city_id'?: string | null;
    /**
     * 
     * @type {number}
     * @memberof SportPlayersAllResponseDataInner
     */
    'position_id'?: number;
    /**
     * 
     * @type {SportPlayersAllResponseDataInnerDetailedPositionId}
     * @memberof SportPlayersAllResponseDataInner
     */
    'detailed_position_id'?: SportPlayersAllResponseDataInnerDetailedPositionId;
    /**
     * 
     * @type {number}
     * @memberof SportPlayersAllResponseDataInner
     */
    'type_id'?: number;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersAllResponseDataInner
     */
    'common_name'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersAllResponseDataInner
     */
    'firstname'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersAllResponseDataInner
     */
    'lastname'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersAllResponseDataInner
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersAllResponseDataInner
     */
    'display_name'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersAllResponseDataInner
     */
    'image_path'?: string;
    /**
     * 
     * @type {number}
     * @memberof SportPlayersAllResponseDataInner
     */
    'height'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportPlayersAllResponseDataInner
     */
    'weight'?: number;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersAllResponseDataInner
     */
    'date_of_birth'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportPlayersAllResponseDataInner
     */
    'gender'?: string;
}
