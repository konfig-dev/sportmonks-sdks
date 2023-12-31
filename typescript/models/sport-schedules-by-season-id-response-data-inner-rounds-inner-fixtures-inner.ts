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
import { SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInner } from './sport-schedules-by-season-id-response-data-inner-rounds-inner-fixtures-inner-participants-inner';

/**
 * 
 * @export
 * @interface SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
 */
export interface SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner {
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'sport_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'league_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'season_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'stage_id'?: number;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'group_id'?: string | null;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'aggregate_id'?: string | null;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'round_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'state_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'venue_id'?: number;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'name'?: string;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'home_score'?: number | null;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'away_score'?: number | null;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'starting_at'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'result_info'?: string | null;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'leg'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'details'?: string | null;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'length'?: number;
    /**
     * 
     * @type {boolean}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'placeholder'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'last_processed_at'?: string | null;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'starting_at_timestamp'?: number;
    /**
     * 
     * @type {Array<SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInner>}
     * @memberof SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInner
     */
    'participants'?: Array<SportSchedulesBySeasonIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInner>;
}

