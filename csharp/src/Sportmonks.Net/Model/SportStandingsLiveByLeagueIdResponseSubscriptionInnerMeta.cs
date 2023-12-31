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
    /// SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta
    /// </summary>
    [DataContract(Name = "SportStandingsLiveByLeagueIdResponse_subscription_inner_meta")]
    public partial class SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta : IEquatable<SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta" /> class.
        /// </summary>
        /// <param name="trialEndsAt">trialEndsAt.</param>
        /// <param name="endsAt">endsAt.</param>
        public SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta(string trialEndsAt = default(string), string endsAt = default(string))
        {
            this.TrialEndsAt = trialEndsAt;
            this.EndsAt = endsAt;
        }

        /// <summary>
        /// Gets or Sets TrialEndsAt
        /// </summary>
        [DataMember(Name = "trial_ends_at", EmitDefaultValue = true)]
        public string TrialEndsAt { get; set; }

        /// <summary>
        /// Gets or Sets EndsAt
        /// </summary>
        [DataMember(Name = "ends_at", EmitDefaultValue = true)]
        public string EndsAt { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta {\n");
            sb.Append("  TrialEndsAt: ").Append(TrialEndsAt).Append("\n");
            sb.Append("  EndsAt: ").Append(EndsAt).Append("\n");
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
            return this.Equals(input as SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta);
        }

        /// <summary>
        /// Returns true if SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta instances are equal
        /// </summary>
        /// <param name="input">Instance of SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportStandingsLiveByLeagueIdResponseSubscriptionInnerMeta input)
        {
            if (input == null)
            {
                return false;
            }
            return 
                (
                    this.TrialEndsAt == input.TrialEndsAt ||
                    (this.TrialEndsAt != null &&
                    this.TrialEndsAt.Equals(input.TrialEndsAt))
                ) && 
                (
                    this.EndsAt == input.EndsAt ||
                    (this.EndsAt != null &&
                    this.EndsAt.Equals(input.EndsAt))
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
                if (this.TrialEndsAt != null)
                {
                    hashCode = (hashCode * 59) + this.TrialEndsAt.GetHashCode();
                }
                if (this.EndsAt != null)
                {
                    hashCode = (hashCode * 59) + this.EndsAt.GetHashCode();
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
