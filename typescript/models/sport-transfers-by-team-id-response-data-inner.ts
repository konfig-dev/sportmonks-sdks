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
import { SportTransfersByTeamIdResponseDataInnerDetailedPositionId } from './sport-transfers-by-team-id-response-data-inner-detailed-position-id';
// May contain unused imports in some cases
// @ts-ignore
import { SportTransfersByTeamIdResponseDataInnerPositionId } from './sport-transfers-by-team-id-response-data-inner-position-id';

/**
 * 
 * @export
 * @interface SportTransfersByTeamIdResponseDataInner
 */
export interface SportTransfersByTeamIdResponseDataInner {
    /**
     * 
     * @type {number}
     * @memberof SportTransfersByTeamIdResponseDataInner
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportTransfersByTeamIdResponseDataInner
     */
    'sport_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportTransfersByTeamIdResponseDataInner
     */
    'player_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportTransfersByTeamIdResponseDataInner
     */
    'type_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportTransfersByTeamIdResponseDataInner
     */
    'from_team_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportTransfersByTeamIdResponseDataInner
     */
    'to_team_id'?: number;
    /**
     * 
     * @type {SportTransfersByTeamIdResponseDataInnerPositionId}
     * @memberof SportTransfersByTeamIdResponseDataInner
     */
    'position_id'?: SportTransfersByTeamIdResponseDataInnerPositionId;
    /**
     * 
     * @type {SportTransfersByTeamIdResponseDataInnerDetailedPositionId}
     * @memberof SportTransfersByTeamIdResponseDataInner
     */
    'detailed_position_id'?: SportTransfersByTeamIdResponseDataInnerDetailedPositionId;
    /**
     * 
     * @type {string}
     * @memberof SportTransfersByTeamIdResponseDataInner
     */
    'date'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof SportTransfersByTeamIdResponseDataInner
     */
    'career_ended'?: boolean;
    /**
     * 
     * @type {boolean}
     * @memberof SportTransfersByTeamIdResponseDataInner
     */
    'completed'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof SportTransfersByTeamIdResponseDataInner
     */
    'completed_at'?: string;
}

