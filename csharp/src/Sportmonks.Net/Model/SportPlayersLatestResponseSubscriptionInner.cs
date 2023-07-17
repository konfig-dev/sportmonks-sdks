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
    /// SportPlayersLatestResponseSubscriptionInner
    /// </summary>
    [DataContract(Name = "SportPlayersLatestResponse_subscription_inner")]
    public partial class SportPlayersLatestResponseSubscriptionInner : IEquatable<SportPlayersLatestResponseSubscriptionInner>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportPlayersLatestResponseSubscriptionInner" /> class.
        /// </summary>
        /// <param name="meta">meta.</param>
        /// <param name="plans">plans.</param>
        /// <param name="addOns">addOns.</param>
        /// <param name="widgets">widgets.</param>
        public SportPlayersLatestResponseSubscriptionInner(List<string> meta = default(List<string>), List<SportPlayersLatestResponseSubscriptionInnerPlansInner> plans = default(List<SportPlayersLatestResponseSubscriptionInnerPlansInner>), List<string> addOns = default(List<string>), List<string> widgets = default(List<string>))
        {
            this.Meta = meta;
            this.Plans = plans;
            this.AddOns = addOns;
            this.Widgets = widgets;
        }

        /// <summary>
        /// Gets or Sets Meta
        /// </summary>
        [DataMember(Name = "meta", EmitDefaultValue = false)]
        public List<string> Meta { get; set; }

        /// <summary>
        /// Gets or Sets Plans
        /// </summary>
        [DataMember(Name = "plans", EmitDefaultValue = false)]
        public List<SportPlayersLatestResponseSubscriptionInnerPlansInner> Plans { get; set; }

        /// <summary>
        /// Gets or Sets AddOns
        /// </summary>
        [DataMember(Name = "add_ons", EmitDefaultValue = false)]
        public List<string> AddOns { get; set; }

        /// <summary>
        /// Gets or Sets Widgets
        /// </summary>
        [DataMember(Name = "widgets", EmitDefaultValue = false)]
        public List<string> Widgets { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportPlayersLatestResponseSubscriptionInner {\n");
            sb.Append("  Meta: ").Append(Meta).Append("\n");
            sb.Append("  Plans: ").Append(Plans).Append("\n");
            sb.Append("  AddOns: ").Append(AddOns).Append("\n");
            sb.Append("  Widgets: ").Append(Widgets).Append("\n");
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
            return this.Equals(input as SportPlayersLatestResponseSubscriptionInner);
        }

        /// <summary>
        /// Returns true if SportPlayersLatestResponseSubscriptionInner instances are equal
        /// </summary>
        /// <param name="input">Instance of SportPlayersLatestResponseSubscriptionInner to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportPlayersLatestResponseSubscriptionInner input)
        {
            if (input == null)
            {
                return false;
            }
            return 
                (
                    this.Meta == input.Meta ||
                    this.Meta != null &&
                    input.Meta != null &&
                    this.Meta.SequenceEqual(input.Meta)
                ) && 
                (
                    this.Plans == input.Plans ||
                    this.Plans != null &&
                    input.Plans != null &&
                    this.Plans.SequenceEqual(input.Plans)
                ) && 
                (
                    this.AddOns == input.AddOns ||
                    this.AddOns != null &&
                    input.AddOns != null &&
                    this.AddOns.SequenceEqual(input.AddOns)
                ) && 
                (
                    this.Widgets == input.Widgets ||
                    this.Widgets != null &&
                    input.Widgets != null &&
                    this.Widgets.SequenceEqual(input.Widgets)
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
                if (this.Meta != null)
                {
                    hashCode = (hashCode * 59) + this.Meta.GetHashCode();
                }
                if (this.Plans != null)
                {
                    hashCode = (hashCode * 59) + this.Plans.GetHashCode();
                }
                if (this.AddOns != null)
                {
                    hashCode = (hashCode * 59) + this.AddOns.GetHashCode();
                }
                if (this.Widgets != null)
                {
                    hashCode = (hashCode * 59) + this.Widgets.GetHashCode();
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
