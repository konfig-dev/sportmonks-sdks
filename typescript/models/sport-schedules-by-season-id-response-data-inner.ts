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
import { SportSchedulesBySeasonIdResponseDataInnerRoundsInner } from './sport-schedules-by-season-id-response-data-inner-rounds-inner';

/**
 * 
 * @export
 * @interface SportSchedulesBySeasonIdResponseDataInner
 */
export interface SportSchedulesBySeasonIdResponseDataInner {
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'sport_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'league_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'season_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'type_id'?: number;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'name'?: string;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'sort_order'?: number;
    /**
     * 
     * @type {boolean}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'finished'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'is_current'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'starting_at'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'ending_at'?: string;
    /**
     * 
     * @type {Array<SportSchedulesBySeasonIdResponseDataInnerRoundsInner>}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'rounds'?: Array<SportSchedulesBySeasonIdResponseDataInnerRoundsInner>;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportSchedulesBySeasonIdResponseDataInner
     */
    'aggregates'?: Array<string>;
}

