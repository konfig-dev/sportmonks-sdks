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
import { SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInnerWinning } from './sport-odds-pre-match-by-fixture-and-bookmaker-id-response-data-inner-winning';

/**
 * 
 * @export
 * @interface SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
 */
export interface SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner {
    /**
     * 
     * @type {number}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'fixture_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'market_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'bookmaker_id'?: number;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'label'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'value'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'name'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'sort_order'?: string | null;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'market_description'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'probability'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'dp3'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'fractional'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'american'?: string;
    /**
     * 
     * @type {SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInnerWinning}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'winning'?: SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInnerWinning;
    /**
     * 
     * @type {boolean}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'stopped'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'total'?: string | null;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'handicap'?: string | null;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'participants'?: string | null;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'created_at'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'updated_at'?: string;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'original_label'?: string | null;
    /**
     * 
     * @type {string}
     * @memberof SportOddsPreMatchByFixtureAndBookmakerIdResponseDataInner
     */
    'latest_bookmaker_update'?: string;
}
