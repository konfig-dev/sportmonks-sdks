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
    /// SportCoachesByCountryIdResponseDataInner
    /// </summary>
    [DataContract(Name = "SportCoachesByCountryIdResponse_data_inner")]
    public partial class SportCoachesByCountryIdResponseDataInner : IEquatable<SportCoachesByCountryIdResponseDataInner>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportCoachesByCountryIdResponseDataInner" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="playerId">playerId.</param>
        /// <param name="sportId">sportId.</param>
        /// <param name="countryId">countryId.</param>
        /// <param name="nationalityId">nationalityId.</param>
        /// <param name="cityId">cityId.</param>
        /// <param name="commonName">commonName.</param>
        /// <param name="firstname">firstname.</param>
        /// <param name="lastname">lastname.</param>
        /// <param name="name">name.</param>
        /// <param name="displayName">displayName.</param>
        /// <param name="imagePath">imagePath.</param>
        /// <param name="height">height.</param>
        /// <param name="weight">weight.</param>
        /// <param name="dateOfBirth">dateOfBirth.</param>
        /// <param name="gender">gender.</param>
        public SportCoachesByCountryIdResponseDataInner(decimal id = default(decimal), decimal playerId = default(decimal), decimal sportId = default(decimal), decimal countryId = default(decimal), string nationalityId = default(string), string cityId = default(string), string commonName = default(string), string firstname = default(string), string lastname = default(string), string name = default(string), string displayName = default(string), string imagePath = default(string), SportCoachesByCountryIdResponseDataInnerHeight height = default(SportCoachesByCountryIdResponseDataInnerHeight), SportCoachesByCountryIdResponseDataInnerWeight weight = default(SportCoachesByCountryIdResponseDataInnerWeight), string dateOfBirth = default(string), string gender = default(string))
        {
            this.Id = id;
            this.PlayerId = playerId;
            this.SportId = sportId;
            this.CountryId = countryId;
            this.NationalityId = nationalityId;
            this.CityId = cityId;
            this.CommonName = commonName;
            this.Firstname = firstname;
            this.Lastname = lastname;
            this.Name = name;
            this.DisplayName = displayName;
            this.ImagePath = imagePath;
            this.Height = height;
            this.Weight = weight;
            this.DateOfBirth = dateOfBirth;
            this.Gender = gender;
        }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public decimal Id { get; set; }

        /// <summary>
        /// Gets or Sets PlayerId
        /// </summary>
        [DataMember(Name = "player_id", EmitDefaultValue = false)]
        public decimal PlayerId { get; set; }

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
        /// Gets or Sets NationalityId
        /// </summary>
        [DataMember(Name = "nationality_id", EmitDefaultValue = true)]
        public string NationalityId { get; set; }

        /// <summary>
        /// Gets or Sets CityId
        /// </summary>
        [DataMember(Name = "city_id", EmitDefaultValue = true)]
        public string CityId { get; set; }

        /// <summary>
        /// Gets or Sets CommonName
        /// </summary>
        [DataMember(Name = "common_name", EmitDefaultValue = false)]
        public string CommonName { get; set; }

        /// <summary>
        /// Gets or Sets Firstname
        /// </summary>
        [DataMember(Name = "firstname", EmitDefaultValue = false)]
        public string Firstname { get; set; }

        /// <summary>
        /// Gets or Sets Lastname
        /// </summary>
        [DataMember(Name = "lastname", EmitDefaultValue = false)]
        public string Lastname { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name = "name", EmitDefaultValue = false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets DisplayName
        /// </summary>
        [DataMember(Name = "display_name", EmitDefaultValue = true)]
        public string DisplayName { get; set; }

        /// <summary>
        /// Gets or Sets ImagePath
        /// </summary>
        [DataMember(Name = "image_path", EmitDefaultValue = false)]
        public string ImagePath { get; set; }

        /// <summary>
        /// Gets or Sets Height
        /// </summary>
        [DataMember(Name = "height", EmitDefaultValue = false)]
        public SportCoachesByCountryIdResponseDataInnerHeight Height { get; set; }

        /// <summary>
        /// Gets or Sets Weight
        /// </summary>
        [DataMember(Name = "weight", EmitDefaultValue = false)]
        public SportCoachesByCountryIdResponseDataInnerWeight Weight { get; set; }

        /// <summary>
        /// Gets or Sets DateOfBirth
        /// </summary>
        [DataMember(Name = "date_of_birth", EmitDefaultValue = true)]
        public string DateOfBirth { get; set; }

        /// <summary>
        /// Gets or Sets Gender
        /// </summary>
        [DataMember(Name = "gender", EmitDefaultValue = false)]
        public string Gender { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportCoachesByCountryIdResponseDataInner {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  PlayerId: ").Append(PlayerId).Append("\n");
            sb.Append("  SportId: ").Append(SportId).Append("\n");
            sb.Append("  CountryId: ").Append(CountryId).Append("\n");
            sb.Append("  NationalityId: ").Append(NationalityId).Append("\n");
            sb.Append("  CityId: ").Append(CityId).Append("\n");
            sb.Append("  CommonName: ").Append(CommonName).Append("\n");
            sb.Append("  Firstname: ").Append(Firstname).Append("\n");
            sb.Append("  Lastname: ").Append(Lastname).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  DisplayName: ").Append(DisplayName).Append("\n");
            sb.Append("  ImagePath: ").Append(ImagePath).Append("\n");
            sb.Append("  Height: ").Append(Height).Append("\n");
            sb.Append("  Weight: ").Append(Weight).Append("\n");
            sb.Append("  DateOfBirth: ").Append(DateOfBirth).Append("\n");
            sb.Append("  Gender: ").Append(Gender).Append("\n");
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
            return this.Equals(input as SportCoachesByCountryIdResponseDataInner);
        }

        /// <summary>
        /// Returns true if SportCoachesByCountryIdResponseDataInner instances are equal
        /// </summary>
        /// <param name="input">Instance of SportCoachesByCountryIdResponseDataInner to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportCoachesByCountryIdResponseDataInner input)
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
                    this.PlayerId == input.PlayerId ||
                    this.PlayerId.Equals(input.PlayerId)
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
                    this.NationalityId == input.NationalityId ||
                    (this.NationalityId != null &&
                    this.NationalityId.Equals(input.NationalityId))
                ) && 
                (
                    this.CityId == input.CityId ||
                    (this.CityId != null &&
                    this.CityId.Equals(input.CityId))
                ) && 
                (
                    this.CommonName == input.CommonName ||
                    (this.CommonName != null &&
                    this.CommonName.Equals(input.CommonName))
                ) && 
                (
                    this.Firstname == input.Firstname ||
                    (this.Firstname != null &&
                    this.Firstname.Equals(input.Firstname))
                ) && 
                (
                    this.Lastname == input.Lastname ||
                    (this.Lastname != null &&
                    this.Lastname.Equals(input.Lastname))
                ) && 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.DisplayName == input.DisplayName ||
                    (this.DisplayName != null &&
                    this.DisplayName.Equals(input.DisplayName))
                ) && 
                (
                    this.ImagePath == input.ImagePath ||
                    (this.ImagePath != null &&
                    this.ImagePath.Equals(input.ImagePath))
                ) && 
                (
                    this.Height == input.Height ||
                    (this.Height != null &&
                    this.Height.Equals(input.Height))
                ) && 
                (
                    this.Weight == input.Weight ||
                    (this.Weight != null &&
                    this.Weight.Equals(input.Weight))
                ) && 
                (
                    this.DateOfBirth == input.DateOfBirth ||
                    (this.DateOfBirth != null &&
                    this.DateOfBirth.Equals(input.DateOfBirth))
                ) && 
                (
                    this.Gender == input.Gender ||
                    (this.Gender != null &&
                    this.Gender.Equals(input.Gender))
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
                hashCode = (hashCode * 59) + this.PlayerId.GetHashCode();
                hashCode = (hashCode * 59) + this.SportId.GetHashCode();
                hashCode = (hashCode * 59) + this.CountryId.GetHashCode();
                if (this.NationalityId != null)
                {
                    hashCode = (hashCode * 59) + this.NationalityId.GetHashCode();
                }
                if (this.CityId != null)
                {
                    hashCode = (hashCode * 59) + this.CityId.GetHashCode();
                }
                if (this.CommonName != null)
                {
                    hashCode = (hashCode * 59) + this.CommonName.GetHashCode();
                }
                if (this.Firstname != null)
                {
                    hashCode = (hashCode * 59) + this.Firstname.GetHashCode();
                }
                if (this.Lastname != null)
                {
                    hashCode = (hashCode * 59) + this.Lastname.GetHashCode();
                }
                if (this.Name != null)
                {
                    hashCode = (hashCode * 59) + this.Name.GetHashCode();
                }
                if (this.DisplayName != null)
                {
                    hashCode = (hashCode * 59) + this.DisplayName.GetHashCode();
                }
                if (this.ImagePath != null)
                {
                    hashCode = (hashCode * 59) + this.ImagePath.GetHashCode();
                }
                if (this.Height != null)
                {
                    hashCode = (hashCode * 59) + this.Height.GetHashCode();
                }
                if (this.Weight != null)
                {
                    hashCode = (hashCode * 59) + this.Weight.GetHashCode();
                }
                if (this.DateOfBirth != null)
                {
                    hashCode = (hashCode * 59) + this.DateOfBirth.GetHashCode();
                }
                if (this.Gender != null)
                {
                    hashCode = (hashCode * 59) + this.Gender.GetHashCode();
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
