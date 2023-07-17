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
    /// SportVenuesAllResponseDataInner
    /// </summary>
    [DataContract(Name = "SportVenuesAllResponse_data_inner")]
    public partial class SportVenuesAllResponseDataInner : IEquatable<SportVenuesAllResponseDataInner>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportVenuesAllResponseDataInner" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="countryId">countryId.</param>
        /// <param name="cityId">cityId.</param>
        /// <param name="name">name.</param>
        /// <param name="address">address.</param>
        /// <param name="zipcode">zipcode.</param>
        /// <param name="latitude">latitude.</param>
        /// <param name="longitude">longitude.</param>
        /// <param name="capacity">capacity.</param>
        /// <param name="imagePath">imagePath.</param>
        /// <param name="cityName">cityName.</param>
        /// <param name="surface">surface.</param>
        /// <param name="nationalTeam">nationalTeam.</param>
        public SportVenuesAllResponseDataInner(decimal id = default(decimal), SportVenuesAllResponseDataInnerCountryId countryId = default(SportVenuesAllResponseDataInnerCountryId), SportVenuesAllResponseDataInnerCityId cityId = default(SportVenuesAllResponseDataInnerCityId), string name = default(string), string address = default(string), string zipcode = default(string), string latitude = default(string), string longitude = default(string), SportVenuesAllResponseDataInnerCapacity capacity = default(SportVenuesAllResponseDataInnerCapacity), string imagePath = default(string), string cityName = default(string), string surface = default(string), bool nationalTeam = default(bool))
        {
            this.Id = id;
            this.CountryId = countryId;
            this.CityId = cityId;
            this.Name = name;
            this.Address = address;
            this.Zipcode = zipcode;
            this.Latitude = latitude;
            this.Longitude = longitude;
            this.Capacity = capacity;
            this.ImagePath = imagePath;
            this.CityName = cityName;
            this.Surface = surface;
            this.NationalTeam = nationalTeam;
        }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public decimal Id { get; set; }

        /// <summary>
        /// Gets or Sets CountryId
        /// </summary>
        [DataMember(Name = "country_id", EmitDefaultValue = false)]
        public SportVenuesAllResponseDataInnerCountryId CountryId { get; set; }

        /// <summary>
        /// Gets or Sets CityId
        /// </summary>
        [DataMember(Name = "city_id", EmitDefaultValue = false)]
        public SportVenuesAllResponseDataInnerCityId CityId { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name = "name", EmitDefaultValue = false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets Address
        /// </summary>
        [DataMember(Name = "address", EmitDefaultValue = true)]
        public string Address { get; set; }

        /// <summary>
        /// Gets or Sets Zipcode
        /// </summary>
        [DataMember(Name = "zipcode", EmitDefaultValue = true)]
        public string Zipcode { get; set; }

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
        /// Gets or Sets Capacity
        /// </summary>
        [DataMember(Name = "capacity", EmitDefaultValue = false)]
        public SportVenuesAllResponseDataInnerCapacity Capacity { get; set; }

        /// <summary>
        /// Gets or Sets ImagePath
        /// </summary>
        [DataMember(Name = "image_path", EmitDefaultValue = true)]
        public string ImagePath { get; set; }

        /// <summary>
        /// Gets or Sets CityName
        /// </summary>
        [DataMember(Name = "city_name", EmitDefaultValue = false)]
        public string CityName { get; set; }

        /// <summary>
        /// Gets or Sets Surface
        /// </summary>
        [DataMember(Name = "surface", EmitDefaultValue = true)]
        public string Surface { get; set; }

        /// <summary>
        /// Gets or Sets NationalTeam
        /// </summary>
        [DataMember(Name = "national_team", EmitDefaultValue = true)]
        public bool NationalTeam { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportVenuesAllResponseDataInner {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  CountryId: ").Append(CountryId).Append("\n");
            sb.Append("  CityId: ").Append(CityId).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Address: ").Append(Address).Append("\n");
            sb.Append("  Zipcode: ").Append(Zipcode).Append("\n");
            sb.Append("  Latitude: ").Append(Latitude).Append("\n");
            sb.Append("  Longitude: ").Append(Longitude).Append("\n");
            sb.Append("  Capacity: ").Append(Capacity).Append("\n");
            sb.Append("  ImagePath: ").Append(ImagePath).Append("\n");
            sb.Append("  CityName: ").Append(CityName).Append("\n");
            sb.Append("  Surface: ").Append(Surface).Append("\n");
            sb.Append("  NationalTeam: ").Append(NationalTeam).Append("\n");
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
            return this.Equals(input as SportVenuesAllResponseDataInner);
        }

        /// <summary>
        /// Returns true if SportVenuesAllResponseDataInner instances are equal
        /// </summary>
        /// <param name="input">Instance of SportVenuesAllResponseDataInner to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportVenuesAllResponseDataInner input)
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
                    this.CountryId == input.CountryId ||
                    (this.CountryId != null &&
                    this.CountryId.Equals(input.CountryId))
                ) && 
                (
                    this.CityId == input.CityId ||
                    (this.CityId != null &&
                    this.CityId.Equals(input.CityId))
                ) && 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.Address == input.Address ||
                    (this.Address != null &&
                    this.Address.Equals(input.Address))
                ) && 
                (
                    this.Zipcode == input.Zipcode ||
                    (this.Zipcode != null &&
                    this.Zipcode.Equals(input.Zipcode))
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
                    this.Capacity == input.Capacity ||
                    (this.Capacity != null &&
                    this.Capacity.Equals(input.Capacity))
                ) && 
                (
                    this.ImagePath == input.ImagePath ||
                    (this.ImagePath != null &&
                    this.ImagePath.Equals(input.ImagePath))
                ) && 
                (
                    this.CityName == input.CityName ||
                    (this.CityName != null &&
                    this.CityName.Equals(input.CityName))
                ) && 
                (
                    this.Surface == input.Surface ||
                    (this.Surface != null &&
                    this.Surface.Equals(input.Surface))
                ) && 
                (
                    this.NationalTeam == input.NationalTeam ||
                    this.NationalTeam.Equals(input.NationalTeam)
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
                if (this.CountryId != null)
                {
                    hashCode = (hashCode * 59) + this.CountryId.GetHashCode();
                }
                if (this.CityId != null)
                {
                    hashCode = (hashCode * 59) + this.CityId.GetHashCode();
                }
                if (this.Name != null)
                {
                    hashCode = (hashCode * 59) + this.Name.GetHashCode();
                }
                if (this.Address != null)
                {
                    hashCode = (hashCode * 59) + this.Address.GetHashCode();
                }
                if (this.Zipcode != null)
                {
                    hashCode = (hashCode * 59) + this.Zipcode.GetHashCode();
                }
                if (this.Latitude != null)
                {
                    hashCode = (hashCode * 59) + this.Latitude.GetHashCode();
                }
                if (this.Longitude != null)
                {
                    hashCode = (hashCode * 59) + this.Longitude.GetHashCode();
                }
                if (this.Capacity != null)
                {
                    hashCode = (hashCode * 59) + this.Capacity.GetHashCode();
                }
                if (this.ImagePath != null)
                {
                    hashCode = (hashCode * 59) + this.ImagePath.GetHashCode();
                }
                if (this.CityName != null)
                {
                    hashCode = (hashCode * 59) + this.CityName.GetHashCode();
                }
                if (this.Surface != null)
                {
                    hashCode = (hashCode * 59) + this.Surface.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.NationalTeam.GetHashCode();
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