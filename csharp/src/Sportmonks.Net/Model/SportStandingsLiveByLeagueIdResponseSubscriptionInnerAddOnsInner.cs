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
    /// SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner
    /// </summary>
    [DataContract(Name = "SportStandingsLiveByLeagueIdResponse_subscription_inner_add_ons_inner")]
    public partial class SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner : IEquatable<SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner" /> class.
        /// </summary>
        /// <param name="addOn">addOn.</param>
        /// <param name="sport">sport.</param>
        /// <param name="category">category.</param>
        public SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner(string addOn = default(string), string sport = default(string), string category = default(string))
        {
            this.AddOn = addOn;
            this.Sport = sport;
            this.Category = category;
        }

        /// <summary>
        /// Gets or Sets AddOn
        /// </summary>
        [DataMember(Name = "add_on", EmitDefaultValue = false)]
        public string AddOn { get; set; }

        /// <summary>
        /// Gets or Sets Sport
        /// </summary>
        [DataMember(Name = "sport", EmitDefaultValue = false)]
        public string Sport { get; set; }

        /// <summary>
        /// Gets or Sets Category
        /// </summary>
        [DataMember(Name = "category", EmitDefaultValue = false)]
        public string Category { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner {\n");
            sb.Append("  AddOn: ").Append(AddOn).Append("\n");
            sb.Append("  Sport: ").Append(Sport).Append("\n");
            sb.Append("  Category: ").Append(Category).Append("\n");
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
            return this.Equals(input as SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner);
        }

        /// <summary>
        /// Returns true if SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner instances are equal
        /// </summary>
        /// <param name="input">Instance of SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportStandingsLiveByLeagueIdResponseSubscriptionInnerAddOnsInner input)
        {
            if (input == null)
            {
                return false;
            }
            return 
                (
                    this.AddOn == input.AddOn ||
                    (this.AddOn != null &&
                    this.AddOn.Equals(input.AddOn))
                ) && 
                (
                    this.Sport == input.Sport ||
                    (this.Sport != null &&
                    this.Sport.Equals(input.Sport))
                ) && 
                (
                    this.Category == input.Category ||
                    (this.Category != null &&
                    this.Category.Equals(input.Category))
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
                if (this.AddOn != null)
                {
                    hashCode = (hashCode * 59) + this.AddOn.GetHashCode();
                }
                if (this.Sport != null)
                {
                    hashCode = (hashCode * 59) + this.Sport.GetHashCode();
                }
                if (this.Category != null)
                {
                    hashCode = (hashCode * 59) + this.Category.GetHashCode();
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
