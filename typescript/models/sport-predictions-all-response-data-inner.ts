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
import { SportPredictionsAllResponseDataInnerPredictions } from './sport-predictions-all-response-data-inner-predictions';

/**
 * 
 * @export
 * @interface SportPredictionsAllResponseDataInner
 */
export interface SportPredictionsAllResponseDataInner {
    /**
     * 
     * @type {number}
     * @memberof SportPredictionsAllResponseDataInner
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportPredictionsAllResponseDataInner
     */
    'fixture_id'?: number;
    /**
     * 
     * @type {SportPredictionsAllResponseDataInnerPredictions}
     * @memberof SportPredictionsAllResponseDataInner
     */
    'predictions'?: SportPredictionsAllResponseDataInnerPredictions;
    /**
     * 
     * @type {number}
     * @memberof SportPredictionsAllResponseDataInner
     */
    'type_id'?: number;
}

