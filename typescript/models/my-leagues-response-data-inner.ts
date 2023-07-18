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
import { MyLeaguesResponseDataInnerSport } from './my-leagues-response-data-inner-sport';

/**
 * 
 * @export
 * @interface MyLeaguesResponseDataInner
 */
export interface MyLeaguesResponseDataInner {
    /**
     * 
     * @type {number}
     * @memberof MyLeaguesResponseDataInner
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof MyLeaguesResponseDataInner
     */
    'sport_id'?: number;
    /**
     * 
     * @type {number}
     * @memberof MyLeaguesResponseDataInner
     */
    'country_id'?: number;
    /**
     * 
     * @type {string}
     * @memberof MyLeaguesResponseDataInner
     */
    'name'?: string;
    /**
     * 
     * @type {boolean}
     * @memberof MyLeaguesResponseDataInner
     */
    'active'?: boolean;
    /**
     * 
     * @type {string}
     * @memberof MyLeaguesResponseDataInner
     */
    'short_code'?: string | null;
    /**
     * 
     * @type {string}
     * @memberof MyLeaguesResponseDataInner
     */
    'image_path'?: string;
    /**
     * 
     * @type {string}
     * @memberof MyLeaguesResponseDataInner
     */
    'type'?: string;
    /**
     * 
     * @type {string}
     * @memberof MyLeaguesResponseDataInner
     */
    'sub_type'?: string;
    /**
     * 
     * @type {string}
     * @memberof MyLeaguesResponseDataInner
     */
    'last_played_at'?: string | null;
    /**
     * 
     * @type {number}
     * @memberof MyLeaguesResponseDataInner
     */
    'category'?: number;
    /**
     * 
     * @type {boolean}
     * @memberof MyLeaguesResponseDataInner
     */
    'has_jerseys'?: boolean;
    /**
     * 
     * @type {MyLeaguesResponseDataInnerSport}
     * @memberof MyLeaguesResponseDataInner
     */
    'sport'?: MyLeaguesResponseDataInnerSport;
}
