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


/**
 * 
 * @export
 * @interface SportTranfersByDateRangeResponseDataInner
 */
export interface SportTranfersByDateRangeResponseDataInner {
    /**
     * 
     * @type {number}
     * @memberof SportTranfersByDateRangeResponseDataInner
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportTranfersByDateRangeResponseDataInner
     */
    'sport_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportTranfersByDateRangeResponseDataInner
     */
    'player_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportTranfersByDateRangeResponseDataInner
     */
    'type_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportTranfersByDateRangeResponseDataInner
     */
    'from_team_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportTranfersByDateRangeResponseDataInner
     */
    'to_team_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportTranfersByDateRangeResponseDataInner
     */
    'position_id'?: number | null;
    /**
     * 
     * @type {number}
     * @memberof SportTranfersByDateRangeResponseDataInner
     */
    'detailed_position_id'?: number | null;
    /**
     * 
     * @type {string}
     * @memberof SportTranfersByDateRangeResponseDataInner
     */
    'date'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof SportTranfersByDateRangeResponseDataInner
     */
    'career_ended'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof SportTranfersByDateRangeResponseDataInner
     */
    'completed'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof SportTranfersByDateRangeResponseDataInner
     */
    'completed_at'?: string;
}

