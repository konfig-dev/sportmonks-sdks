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
    /// SportVenuesAllResponsePagination
    /// </summary>
    [DataContract(Name = "SportVenuesAllResponse_pagination")]
    public partial class SportVenuesAllResponsePagination : IEquatable<SportVenuesAllResponsePagination>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportVenuesAllResponsePagination" /> class.
        /// </summary>
        /// <param name="count">count.</param>
        /// <param name="perPage">perPage.</param>
        /// <param name="currentPage">currentPage.</param>
        /// <param name="nextPage">nextPage.</param>
        /// <param name="hasMore">hasMore.</param>
        public SportVenuesAllResponsePagination(decimal count = default(decimal), decimal perPage = default(decimal), decimal currentPage = default(decimal), string nextPage = default(string), bool hasMore = default(bool))
        {
            this.Count = count;
            this.PerPage = perPage;
            this.CurrentPage = currentPage;
            this.NextPage = nextPage;
            this.HasMore = hasMore;
        }

        /// <summary>
        /// Gets or Sets Count
        /// </summary>
        [DataMember(Name = "count", EmitDefaultValue = false)]
        public decimal Count { get; set; }

        /// <summary>
        /// Gets or Sets PerPage
        /// </summary>
        [DataMember(Name = "per_page", EmitDefaultValue = false)]
        public decimal PerPage { get; set; }

        /// <summary>
        /// Gets or Sets CurrentPage
        /// </summary>
        [DataMember(Name = "current_page", EmitDefaultValue = false)]
        public decimal CurrentPage { get; set; }

        /// <summary>
        /// Gets or Sets NextPage
        /// </summary>
        [DataMember(Name = "next_page", EmitDefaultValue = false)]
        public string NextPage { get; set; }

        /// <summary>
        /// Gets or Sets HasMore
        /// </summary>
        [DataMember(Name = "has_more", EmitDefaultValue = true)]
        public bool HasMore { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportVenuesAllResponsePagination {\n");
            sb.Append("  Count: ").Append(Count).Append("\n");
            sb.Append("  PerPage: ").Append(PerPage).Append("\n");
            sb.Append("  CurrentPage: ").Append(CurrentPage).Append("\n");
            sb.Append("  NextPage: ").Append(NextPage).Append("\n");
            sb.Append("  HasMore: ").Append(HasMore).Append("\n");
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
            return this.Equals(input as SportVenuesAllResponsePagination);
        }

        /// <summary>
        /// Returns true if SportVenuesAllResponsePagination instances are equal
        /// </summary>
        /// <param name="input">Instance of SportVenuesAllResponsePagination to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportVenuesAllResponsePagination input)
        {
            if (input == null)
            {
                return false;
            }
            return 
                (
                    this.Count == input.Count ||
                    this.Count.Equals(input.Count)
                ) && 
                (
                    this.PerPage == input.PerPage ||
                    this.PerPage.Equals(input.PerPage)
                ) && 
                (
                    this.CurrentPage == input.CurrentPage ||
                    this.CurrentPage.Equals(input.CurrentPage)
                ) && 
                (
                    this.NextPage == input.NextPage ||
                    (this.NextPage != null &&
                    this.NextPage.Equals(input.NextPage))
                ) && 
                (
                    this.HasMore == input.HasMore ||
                    this.HasMore.Equals(input.HasMore)
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
                hashCode = (hashCode * 59) + this.Count.GetHashCode();
                hashCode = (hashCode * 59) + this.PerPage.GetHashCode();
                hashCode = (hashCode * 59) + this.CurrentPage.GetHashCode();
                if (this.NextPage != null)
                {
                    hashCode = (hashCode * 59) + this.NextPage.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.HasMore.GetHashCode();
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
