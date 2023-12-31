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
    /// SportRivalsAllResponseRateLimit
    /// </summary>
    [DataContract(Name = "SportRivalsAllResponse_rate_limit")]
    public partial class SportRivalsAllResponseRateLimit : IEquatable<SportRivalsAllResponseRateLimit>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportRivalsAllResponseRateLimit" /> class.
        /// </summary>
        /// <param name="resetsInSeconds">resetsInSeconds.</param>
        /// <param name="remaining">remaining.</param>
        /// <param name="requestedEntity">requestedEntity.</param>
        public SportRivalsAllResponseRateLimit(decimal resetsInSeconds = default(decimal), decimal remaining = default(decimal), string requestedEntity = default(string))
        {
            this.ResetsInSeconds = resetsInSeconds;
            this.Remaining = remaining;
            this.RequestedEntity = requestedEntity;
        }

        /// <summary>
        /// Gets or Sets ResetsInSeconds
        /// </summary>
        [DataMember(Name = "resets_in_seconds", EmitDefaultValue = false)]
        public decimal ResetsInSeconds { get; set; }

        /// <summary>
        /// Gets or Sets Remaining
        /// </summary>
        [DataMember(Name = "remaining", EmitDefaultValue = false)]
        public decimal Remaining { get; set; }

        /// <summary>
        /// Gets or Sets RequestedEntity
        /// </summary>
        [DataMember(Name = "requested_entity", EmitDefaultValue = false)]
        public string RequestedEntity { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportRivalsAllResponseRateLimit {\n");
            sb.Append("  ResetsInSeconds: ").Append(ResetsInSeconds).Append("\n");
            sb.Append("  Remaining: ").Append(Remaining).Append("\n");
            sb.Append("  RequestedEntity: ").Append(RequestedEntity).Append("\n");
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
            return this.Equals(input as SportRivalsAllResponseRateLimit);
        }

        /// <summary>
        /// Returns true if SportRivalsAllResponseRateLimit instances are equal
        /// </summary>
        /// <param name="input">Instance of SportRivalsAllResponseRateLimit to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportRivalsAllResponseRateLimit input)
        {
            if (input == null)
            {
                return false;
            }
            return 
                (
                    this.ResetsInSeconds == input.ResetsInSeconds ||
                    this.ResetsInSeconds.Equals(input.ResetsInSeconds)
                ) && 
                (
                    this.Remaining == input.Remaining ||
                    this.Remaining.Equals(input.Remaining)
                ) && 
                (
                    this.RequestedEntity == input.RequestedEntity ||
                    (this.RequestedEntity != null &&
                    this.RequestedEntity.Equals(input.RequestedEntity))
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
                hashCode = (hashCode * 59) + this.ResetsInSeconds.GetHashCode();
                hashCode = (hashCode * 59) + this.Remaining.GetHashCode();
                if (this.RequestedEntity != null)
                {
                    hashCode = (hashCode * 59) + this.RequestedEntity.GetHashCode();
                }
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
