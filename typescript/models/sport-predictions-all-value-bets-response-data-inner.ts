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
import { SportPredictionsAllValueBetsResponseDataInnerPredictions } from './sport-predictions-all-value-bets-response-data-inner-predictions';

/**
 * 
 * @export
 * @interface SportPredictionsAllValueBetsResponseDataInner
 */
export interface SportPredictionsAllValueBetsResponseDataInner {
    /**
     * 
     * @type {number}
     * @memberof SportPredictionsAllValueBetsResponseDataInner
     */
    'id'?: number;
    /**
     * 
     * @type {number}
     * @memberof SportPredictionsAllValueBetsResponseDataInner
     */
    'fixture_id'?: number;
    /**
     * 
     * @type {SportPredictionsAllValueBetsResponseDataInnerPredictions}
     * @memberof SportPredictionsAllValueBetsResponseDataInner
     */
    'predictions'?: SportPredictionsAllValueBetsResponseDataInnerPredictions;
    /**
     * 
     * @type {number}
     * @memberof SportPredictionsAllValueBetsResponseDataInner
     */
    'type_id'?: number;
}

