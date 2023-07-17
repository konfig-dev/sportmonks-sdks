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
    /// CountriesSearchResponseDataInner
    /// </summary>
    [DataContract(Name = "CountriesSearchResponse_data_inner")]
    public partial class CountriesSearchResponseDataInner : IEquatable<CountriesSearchResponseDataInner>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="CountriesSearchResponseDataInner" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="continentId">continentId.</param>
        /// <param name="name">name.</param>
        /// <param name="officialName">officialName.</param>
        /// <param name="fifaName">fifaName.</param>
        /// <param name="iso2">iso2.</param>
        /// <param name="iso3">iso3.</param>
        /// <param name="latitude">latitude.</param>
        /// <param name="longitude">longitude.</param>
        /// <param name="borders">borders.</param>
        /// <param name="imagePath">imagePath.</param>
        public CountriesSearchResponseDataInner(decimal id = default(decimal), decimal continentId = default(decimal), string name = default(string), string officialName = default(string), string fifaName = default(string), string iso2 = default(string), string iso3 = default(string), string latitude = default(string), string longitude = default(string), List<string> borders = default(List<string>), string imagePath = default(string))
        {
            this.Id = id;
            this.ContinentId = continentId;
            this.Name = name;
            this.OfficialName = officialName;
            this.FifaName = fifaName;
            this.Iso2 = iso2;
            this.Iso3 = iso3;
            this.Latitude = latitude;
            this.Longitude = longitude;
            this.Borders = borders;
            this.ImagePath = imagePath;
        }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public decimal Id { get; set; }

        /// <summary>
        /// Gets or Sets ContinentId
        /// </summary>
        [DataMember(Name = "continent_id", EmitDefaultValue = false)]
        public decimal ContinentId { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name = "name", EmitDefaultValue = false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets OfficialName
        /// </summary>
        [DataMember(Name = "official_name", EmitDefaultValue = false)]
        public string OfficialName { get; set; }

        /// <summary>
        /// Gets or Sets FifaName
        /// </summary>
        [DataMember(Name = "fifa_name", EmitDefaultValue = false)]
        public string FifaName { get; set; }

        /// <summary>
        /// Gets or Sets Iso2
        /// </summary>
        [DataMember(Name = "iso2", EmitDefaultValue = false)]
        public string Iso2 { get; set; }

        /// <summary>
        /// Gets or Sets Iso3
        /// </summary>
        [DataMember(Name = "iso3", EmitDefaultValue = false)]
        public string Iso3 { get; set; }

        /// <summary>
        /// Gets or Sets Latitude
        /// </summary>
        [DataMember(Name = "latitude", EmitDefaultValue = false)]
        public string Latitude { get; set; }

        /// <summary>
        /// Gets or Sets Longitude
        /// </summary>
        [DataMember(Name = "longitude", EmitDefaultValue = false)]
        public string Longitude { get; set; }

        /// <summary>
        /// Gets or Sets Borders
        /// </summary>
        [DataMember(Name = "borders", EmitDefaultValue = false)]
        public List<string> Borders { get; set; }

        /// <summary>
        /// Gets or Sets ImagePath
        /// </summary>
        [DataMember(Name = "image_path", EmitDefaultValue = false)]
        public string ImagePath { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class CountriesSearchResponseDataInner {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  ContinentId: ").Append(ContinentId).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  OfficialName: ").Append(OfficialName).Append("\n");
            sb.Append("  FifaName: ").Append(FifaName).Append("\n");
            sb.Append("  Iso2: ").Append(Iso2).Append("\n");
            sb.Append("  Iso3: ").Append(Iso3).Append("\n");
            sb.Append("  Latitude: ").Append(Latitude).Append("\n");
            sb.Append("  Longitude: ").Append(Longitude).Append("\n");
            sb.Append("  Borders: ").Append(Borders).Append("\n");
            sb.Append("  ImagePath: ").Append(ImagePath).Append("\n");
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
            return this.Equals(input as CountriesSearchResponseDataInner);
        }

        /// <summary>
        /// Returns true if CountriesSearchResponseDataInner instances are equal
        /// </summary>
        /// <param name="input">Instance of CountriesSearchResponseDataInner to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(CountriesSearchResponseDataInner input)
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
                    this.ContinentId == input.ContinentId ||
                    this.ContinentId.Equals(input.ContinentId)
                ) && 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.OfficialName == input.OfficialName ||
                    (this.OfficialName != null &&
                    this.OfficialName.Equals(input.OfficialName))
                ) && 
                (
                    this.FifaName == input.FifaName ||
                    (this.FifaName != null &&
                    this.FifaName.Equals(input.FifaName))
                ) && 
                (
                    this.Iso2 == input.Iso2 ||
                    (this.Iso2 != null &&
                    this.Iso2.Equals(input.Iso2))
                ) && 
                (
                    this.Iso3 == input.Iso3 ||
                    (this.Iso3 != null &&
                    this.Iso3.Equals(input.Iso3))
                ) && 
                (
                    this.Latitude == input.Latitude ||
                    (this.Latitude != null &&
                    this.Latitude.Equals(input.Latitude))
                ) && 
                (
                    this.Longitude == input.Longitude ||
                    (this.Longitude != null &&
                    this.Longitude.Equals(input.Longitude))
                ) && 
                (
                    this.Borders == input.Borders ||
                    this.Borders != null &&
                    input.Borders != null &&
                    this.Borders.SequenceEqual(input.Borders)
                ) && 
                (
                    this.ImagePath == input.ImagePath ||
                    (this.ImagePath != null &&
                    this.ImagePath.Equals(input.ImagePath))
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
                hashCode = (hashCode * 59) + this.ContinentId.GetHashCode();
                if (this.Name != null)
                {
                    hashCode = (hashCode * 59) + this.Name.GetHashCode();
                }
                if (this.OfficialName != null)
                {
                    hashCode = (hashCode * 59) + this.OfficialName.GetHashCode();
                }
                if (this.FifaName != null)
                {
                    hashCode = (hashCode * 59) + this.FifaName.GetHashCode();
                }
                if (this.Iso2 != null)
                {
                    hashCode = (hashCode * 59) + this.Iso2.GetHashCode();
                }
                if (this.Iso3 != null)
                {
                    hashCode = (hashCode * 59) + this.Iso3.GetHashCode();
                }
                if (this.Latitude != null)
                {
                    hashCode = (hashCode * 59) + this.Latitude.GetHashCode();
                }
                if (this.Longitude != null)
                {
                    hashCode = (hashCode * 59) + this.Longitude.GetHashCode();
                }
                if (this.Borders != null)
                {
                    hashCode = (hashCode * 59) + this.Borders.GetHashCode();
                }
                if (this.ImagePath != null)
                {
                    hashCode = (hashCode * 59) + this.ImagePath.GetHashCode();
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
