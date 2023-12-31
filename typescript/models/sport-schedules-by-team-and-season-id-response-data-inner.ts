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
import { SportSchedulesByTeamAndSeasonIdResponseDataInnerRoundsInner } from './sport-schedules-by-team-and-season-id-response-data-inner-rounds-inner';

/**
 * 
 * @export
 * @interface SportSchedulesByTeamAndSeasonIdResponseDataInner
 */
export interface SportSchedulesByTeamAndSeasonIdResponseDataInner {
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'sport_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'league_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'season_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'type_id'?: number;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'name'?: string;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'sort_order'?: number;
    /**
     * 
     * @type {boolean}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'finished'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'is_current'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'starting_at'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'ending_at'?: string;
    /**
     * 
     * @type {Array<string>}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'aggregates'?: Array<string>;
    /**
     * 
     * @type {Array<SportSchedulesByTeamAndSeasonIdResponseDataInnerRoundsInner>}
     * @memberof SportSchedulesByTeamAndSeasonIdResponseDataInner
     */
    'rounds'?: Array<SportSchedulesByTeamAndSeasonIdResponseDataInnerRoundsInner>;
}

