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
    /// SportTeamsSearchResponseDataInner
    /// </summary>
    [DataContract(Name = "SportTeamsSearchResponse_data_inner")]
    public partial class SportTeamsSearchResponseDataInner : IEquatable<SportTeamsSearchResponseDataInner>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportTeamsSearchResponseDataInner" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="sportId">sportId.</param>
        /// <param name="countryId">countryId.</param>
        /// <param name="venueId">venueId.</param>
        /// <param name="gender">gender.</param>
        /// <param name="name">name.</param>
        /// <param name="shortCode">shortCode.</param>
        /// <param name="imagePath">imagePath.</param>
        /// <param name="founded">founded.</param>
        /// <param name="type">type.</param>
        /// <param name="placeholder">placeholder.</param>
        /// <param name="lastPlayedAt">lastPlayedAt.</param>
        public SportTeamsSearchResponseDataInner(decimal id = default(decimal), decimal sportId = default(decimal), decimal countryId = default(decimal), decimal venueId = default(decimal), string gender = default(string), string name = default(string), string shortCode = default(string), string imagePath = default(string), decimal founded = default(decimal), string type = default(string), bool placeholder = default(bool), string lastPlayedAt = default(string))
        {
            this.Id = id;
            this.SportId = sportId;
            this.CountryId = countryId;
            this.VenueId = venueId;
            this.Gender = gender;
            this.Name = name;
            this.ShortCode = shortCode;
            this.ImagePath = imagePath;
            this.Founded = founded;
            this.Type = type;
            this.Placeholder = placeholder;
            this.LastPlayedAt = lastPlayedAt;
        }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public decimal Id { get; set; }

        /// <summary>
        /// Gets or Sets SportId
        /// </summary>
        [DataMember(Name = "sport_id", EmitDefaultValue = false)]
        public decimal SportId { get; set; }

        /// <summary>
        /// Gets or Sets CountryId
        /// </summary>
        [DataMember(Name = "country_id", EmitDefaultValue = false)]
        public decimal CountryId { get; set; }

        /// <summary>
        /// Gets or Sets VenueId
        /// </summary>
        [DataMember(Name = "venue_id", EmitDefaultValue = false)]
        public decimal VenueId { get; set; }

        /// <summary>
        /// Gets or Sets Gender
        /// </summary>
        [DataMember(Name = "gender", EmitDefaultValue = false)]
        public string Gender { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name = "name", EmitDefaultValue = false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets ShortCode
        /// </summary>
        [DataMember(Name = "short_code", EmitDefaultValue = false)]
        public string ShortCode { get; set; }

        /// <summary>
        /// Gets or Sets ImagePath
        /// </summary>
        [DataMember(Name = "image_path", EmitDefaultValue = false)]
        public string ImagePath { get; set; }

        /// <summary>
        /// Gets or Sets Founded
        /// </summary>
        [DataMember(Name = "founded", EmitDefaultValue = false)]
        public decimal Founded { get; set; }

        /// <summary>
        /// Gets or Sets Type
        /// </summary>
        [DataMember(Name = "type", EmitDefaultValue = false)]
        public string Type { get; set; }

        /// <summary>
        /// Gets or Sets Placeholder
        /// </summary>
        [DataMember(Name = "placeholder", EmitDefaultValue = true)]
        public bool Placeholder { get; set; }

        /// <summary>
        /// Gets or Sets LastPlayedAt
        /// </summary>
        [DataMember(Name = "last_played_at", EmitDefaultValue = false)]
        public string LastPlayedAt { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportTeamsSearchResponseDataInner {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  SportId: ").Append(SportId).Append("\n");
            sb.Append("  CountryId: ").Append(CountryId).Append("\n");
            sb.Append("  VenueId: ").Append(VenueId).Append("\n");
            sb.Append("  Gender: ").Append(Gender).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  ShortCode: ").Append(ShortCode).Append("\n");
            sb.Append("  ImagePath: ").Append(ImagePath).Append("\n");
            sb.Append("  Founded: ").Append(Founded).Append("\n");
            sb.Append("  Type: ").Append(Type).Append("\n");
            sb.Append("  Placeholder: ").Append(Placeholder).Append("\n");
            sb.Append("  LastPlayedAt: ").Append(LastPlayedAt).Append("\n");
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
            return this.Equals(input as SportTeamsSearchResponseDataInner);
        }

        /// <summary>
        /// Returns true if SportTeamsSearchResponseDataInner instances are equal
        /// </summary>
        /// <param name="input">Instance of SportTeamsSearchResponseDataInner to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportTeamsSearchResponseDataInner input)
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
                    this.SportId == input.SportId ||
                    this.SportId.Equals(input.SportId)
                ) && 
                (
                    this.CountryId == input.CountryId ||
                    this.CountryId.Equals(input.CountryId)
                ) && 
                (
                    this.VenueId == input.VenueId ||
                    this.VenueId.Equals(input.VenueId)
                ) && 
                (
                    this.Gender == input.Gender ||
                    (this.Gender != null &&
                    this.Gender.Equals(input.Gender))
                ) && 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.ShortCode == input.ShortCode ||
                    (this.ShortCode != null &&
                    this.ShortCode.Equals(input.ShortCode))
                ) && 
                (
                    this.ImagePath == input.ImagePath ||
                    (this.ImagePath != null &&
                    this.ImagePath.Equals(input.ImagePath))
                ) && 
                (
                    this.Founded == input.Founded ||
                    this.Founded.Equals(input.Founded)
                ) && 
                (
                    this.Type == input.Type ||
                    (this.Type != null &&
                    this.Type.Equals(input.Type))
                ) && 
                (
                    this.Placeholder == input.Placeholder ||
                    this.Placeholder.Equals(input.Placeholder)
                ) && 
                (
                    this.LastPlayedAt == input.LastPlayedAt ||
                    (this.LastPlayedAt != null &&
                    this.LastPlayedAt.Equals(input.LastPlayedAt))
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
                hashCode = (hashCode * 59) + this.SportId.GetHashCode();
                hashCode = (hashCode * 59) + this.CountryId.GetHashCode();
                hashCode = (hashCode * 59) + this.VenueId.GetHashCode();
                if (this.Gender != null)
                {
                    hashCode = (hashCode * 59) + this.Gender.GetHashCode();
                }
                if (this.Name != null)
                {
                    hashCode = (hashCode * 59) + this.Name.GetHashCode();
                }
                if (this.ShortCode != null)
                {
                    hashCode = (hashCode * 59) + this.ShortCode.GetHashCode();
                }
                if (this.ImagePath != null)
                {
                    hashCode = (hashCode * 59) + this.ImagePath.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.Founded.GetHashCode();
                if (this.Type != null)
                {
                    hashCode = (hashCode * 59) + this.Type.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.Placeholder.GetHashCode();
                if (this.LastPlayedAt != null)
                {
                    hashCode = (hashCode * 59) + this.LastPlayedAt.GetHashCode();
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
