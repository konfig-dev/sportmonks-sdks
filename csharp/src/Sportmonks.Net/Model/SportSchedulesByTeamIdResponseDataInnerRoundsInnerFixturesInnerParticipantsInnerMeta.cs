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
    /// SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInnerMeta
    /// </summary>
    [DataContract(Name = "SportSchedulesByTeamIdResponse_data_inner_rounds_inner_fixtures_inner_participants_inner_meta")]
    public partial class SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInnerMeta : IEquatable<SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInnerMeta>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInnerMeta" /> class.
        /// </summary>
        /// <param name="location">location.</param>
        public SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInnerMeta(string location = default(string))
        {
            this.Location = location;
        }

        /// <summary>
        /// Gets or Sets Location
        /// </summary>
        [DataMember(Name = "location", EmitDefaultValue = false)]
        public string Location { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInnerMeta {\n");
            sb.Append("  Location: ").Append(Location).Append("\n");
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
            return this.Equals(input as SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInnerMeta);
        }

        /// <summary>
        /// Returns true if SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInnerMeta instances are equal
        /// </summary>
        /// <param name="input">Instance of SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInnerMeta to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInnerParticipantsInnerMeta input)
        {
            if (input == null)
            {
                return false;
            }
            return 
                (
                    this.Location == input.Location ||
                    (this.Location != null &&
                    this.Location.Equals(input.Location))
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
                if (this.Location != null)
                {
                    hashCode = (hashCode * 59) + this.Location.GetHashCode();
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
