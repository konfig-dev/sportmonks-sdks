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
import { SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerAwayScore } from './sport-schedules-by-team-id-response-data-inner-rounds-inner-fixtures-inner-away-score';
// May contain unused imports in some cases
// @ts-ignore
import { SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerHomeScore } from './sport-schedules-by-team-id-response-data-inner-rounds-inner-fixtures-inner-home-score';
// May contain unused imports in some cases
// @ts-ignore
import { SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInner } from './sport-schedules-by-team-id-response-data-inner-rounds-inner-fixtures-inner-participants-inner';

/**
 * 
 * @export
 * @interface SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
 */
export interface SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner {
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'sport_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'league_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'season_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'stage_id'?: number;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'group_id'?: string | null;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'aggregate_id'?: string | null;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'round_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'state_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'venue_id'?: number;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'name'?: string;
    /**
     * 
     * @type {SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerHomeScore}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'home_score'?: SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerHomeScore;
    /**
     * 
     * @type {SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerAwayScore}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'away_score'?: SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerAwayScore;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'starting_at'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'result_info'?: string | null;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'leg'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'details'?: string | null;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'length'?: number;
    /**
     * 
     * @type {boolean}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'placeholder'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'last_processed_at'?: string | null;
    /**
     * 
     * @type {number}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'starting_at_timestamp'?: number;
    /**
     * 
     * @type {Array<SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInner>}
     * @memberof SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner
     */
    'participants'?: Array<SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInner>;
}
