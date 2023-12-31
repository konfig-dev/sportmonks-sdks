/*
 * SportMonks
 *
 * Surpass the competition with superior sports data
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://konfigthis.com
 */


using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.IO;
using System.Runtime.Serialization;
using System.Text;
using System.Text.RegularExpressions;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Linq;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Sportmonks.Net.Client.OpenAPIDateConverter;

namespace Sportmonks.Net.Model
{
    /// <summary>
    /// SportPredictionsByFixtureIdResponseDataInner
    /// </summary>
    [DataContract(Name = "SportPredictionsByFixtureIdResponse_data_inner")]
    public partial class SportPredictionsByFixtureIdResponseDataInner : IEquatable<SportPredictionsByFixtureIdResponseDataInner>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportPredictionsByFixtureIdResponseDataInner" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="fixtureId">fixtureId.</param>
        /// <param name="predictions">predictions.</param>
        /// <param name="typeId">typeId.</param>
        public SportPredictionsByFixtureIdResponseDataInner(decimal id = default(decimal), decimal fixtureId = default(decimal), SportPredictionsByFixtureIdResponseDataInnerPredictions predictions = default(SportPredictionsByFixtureIdResponseDataInnerPredictions), decimal typeId = default(decimal))
        {
            this.Id = id;
            this.FixtureId = fixtureId;
            this.Predictions = predictions;
            this.TypeId = typeId;
        }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public decimal Id { get; set; }

        /// <summary>
        /// Gets or Sets FixtureId
        /// </summary>
        [DataMember(Name = "fixture_id", EmitDefaultValue = false)]
        public decimal FixtureId { get; set; }

        /// <summary>
        /// Gets or Sets Predictions
        /// </summary>
        [DataMember(Name = "predictions", EmitDefaultValue = false)]
        public SportPredictionsByFixtureIdResponseDataInnerPredictions Predictions { get; set; }

        /// <summary>
        /// Gets or Sets TypeId
        /// </summary>
        [DataMember(Name = "type_id", EmitDefaultValue = false)]
        public decimal TypeId { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportPredictionsByFixtureIdResponseDataInner {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  FixtureId: ").Append(FixtureId).Append("\n");
            sb.Append("  Predictions: ").Append(Predictions).Append("\n");
            sb.Append("  TypeId: ").Append(TypeId).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return Newtonsoft.Json.JsonConvert.SerializeObject(this, Newtonsoft.Json.Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as SportPredictionsByFixtureIdResponseDataInner);
        }

        /// <summary>
        /// Returns true if SportPredictionsByFixtureIdResponseDataInner instances are equal
        /// </summary>
        /// <param name="input">Instance of SportPredictionsByFixtureIdResponseDataInner to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportPredictionsByFixtureIdResponseDataInner input)
        {
            if (input == null)
            {
                return false;
            }
            return 
                (
                    this.Id == input.Id ||
                    this.Id.Equals(input.Id)
                ) && 
                (
                    this.FixtureId == input.FixtureId ||
                    this.FixtureId.Equals(input.FixtureId)
                ) && 
                (
                    this.Predictions == input.Predictions ||
                    (this.Predictions != null &&
                    this.Predictions.Equals(input.Predictions))
                ) && 
                (
                    this.TypeId == input.TypeId ||
                    this.TypeId.Equals(input.TypeId)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                hashCode = (hashCode * 59) + this.Id.GetHashCode();
                hashCode = (hashCode * 59) + this.FixtureId.GetHashCode();
                if (this.Predictions != null)
                {
                    hashCode = (hashCode * 59) + this.Predictions.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.TypeId.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        public IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
