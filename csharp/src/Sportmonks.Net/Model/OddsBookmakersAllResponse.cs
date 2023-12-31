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
    /// OddsBookmakersAllResponse
    /// </summary>
    [DataContract(Name = "OddsBookmakersAllResponse")]
    public partial class OddsBookmakersAllResponse : IEquatable<OddsBookmakersAllResponse>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="OddsBookmakersAllResponse" /> class.
        /// </summary>
        /// <param name="data">data.</param>
        /// <param name="pagination">pagination.</param>
        /// <param name="subscription">subscription.</param>
        /// <param name="rateLimit">rateLimit.</param>
        /// <param name="timezone">timezone.</param>
        public OddsBookmakersAllResponse(List<OddsBookmakersAllResponseDataInner> data = default(List<OddsBookmakersAllResponseDataInner>), OddsBookmakersAllResponsePagination pagination = default(OddsBookmakersAllResponsePagination), List<OddsBookmakersAllResponseSubscriptionInner> subscription = default(List<OddsBookmakersAllResponseSubscriptionInner>), OddsBookmakersAllResponseRateLimit rateLimit = default(OddsBookmakersAllResponseRateLimit), string timezone = default(string))
        {
            this.Data = data;
            this.Pagination = pagination;
            this.Subscription = subscription;
            this.RateLimit = rateLimit;
            this.Timezone = timezone;
        }

        /// <summary>
        /// Gets or Sets Data
        /// </summary>
        [DataMember(Name = "data", EmitDefaultValue = false)]
        public List<OddsBookmakersAllResponseDataInner> Data { get; set; }

        /// <summary>
        /// Gets or Sets Pagination
        /// </summary>
        [DataMember(Name = "pagination", EmitDefaultValue = false)]
        public OddsBookmakersAllResponsePagination Pagination { get; set; }

        /// <summary>
        /// Gets or Sets Subscription
        /// </summary>
        [DataMember(Name = "subscription", EmitDefaultValue = false)]
        public List<OddsBookmakersAllResponseSubscriptionInner> Subscription { get; set; }

        /// <summary>
        /// Gets or Sets RateLimit
        /// </summary>
        [DataMember(Name = "rate_limit", EmitDefaultValue = false)]
        public OddsBookmakersAllResponseRateLimit RateLimit { get; set; }

        /// <summary>
        /// Gets or Sets Timezone
        /// </summary>
        [DataMember(Name = "timezone", EmitDefaultValue = false)]
        public string Timezone { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class OddsBookmakersAllResponse {\n");
            sb.Append("  Data: ").Append(Data).Append("\n");
            sb.Append("  Pagination: ").Append(Pagination).Append("\n");
            sb.Append("  Subscription: ").Append(Subscription).Append("\n");
            sb.Append("  RateLimit: ").Append(RateLimit).Append("\n");
            sb.Append("  Timezone: ").Append(Timezone).Append("\n");
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
            return this.Equals(input as OddsBookmakersAllResponse);
        }

        /// <summary>
        /// Returns true if OddsBookmakersAllResponse instances are equal
        /// </summary>
        /// <param name="input">Instance of OddsBookmakersAllResponse to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(OddsBookmakersAllResponse input)
        {
            if (input == null)
            {
                return false;
            }
            return 
                (
                    this.Data == input.Data ||
                    this.Data != null &&
                    input.Data != null &&
                    this.Data.SequenceEqual(input.Data)
                ) && 
                (
                    this.Pagination == input.Pagination ||
                    (this.Pagination != null &&
                    this.Pagination.Equals(input.Pagination))
                ) && 
                (
                    this.Subscription == input.Subscription ||
                    this.Subscription != null &&
                    input.Subscription != null &&
                    this.Subscription.SequenceEqual(input.Subscription)
                ) && 
                (
                    this.RateLimit == input.RateLimit ||
                    (this.RateLimit != null &&
                    this.RateLimit.Equals(input.RateLimit))
                ) && 
                (
                    this.Timezone == input.Timezone ||
                    (this.Timezone != null &&
                    this.Timezone.Equals(input.Timezone))
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
                if (this.Data != null)
                {
                    hashCode = (hashCode * 59) + this.Data.GetHashCode();
                }
                if (this.Pagination != null)
                {
                    hashCode = (hashCode * 59) + this.Pagination.GetHashCode();
                }
                if (this.Subscription != null)
                {
                    hashCode = (hashCode * 59) + this.Subscription.GetHashCode();
                }
                if (this.RateLimit != null)
                {
                    hashCode = (hashCode * 59) + this.RateLimit.GetHashCode();
                }
                if (this.Timezone != null)
                {
                    hashCode = (hashCode * 59) + this.Timezone.GetHashCode();
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
