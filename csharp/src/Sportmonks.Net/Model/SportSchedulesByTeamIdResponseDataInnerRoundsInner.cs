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
    /// SportSchedulesByTeamIdResponseDataInnerRoundsInner
    /// </summary>
    [DataContract(Name = "SportSchedulesByTeamIdResponse_data_inner_rounds_inner")]
    public partial class SportSchedulesByTeamIdResponseDataInnerRoundsInner : IEquatable<SportSchedulesByTeamIdResponseDataInnerRoundsInner>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportSchedulesByTeamIdResponseDataInnerRoundsInner" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="sportId">sportId.</param>
        /// <param name="leagueId">leagueId.</param>
        /// <param name="seasonId">seasonId.</param>
        /// <param name="stageId">stageId.</param>
        /// <param name="name">name.</param>
        /// <param name="finished">finished.</param>
        /// <param name="isCurrent">isCurrent.</param>
        /// <param name="startingAt">startingAt.</param>
        /// <param name="endingAt">endingAt.</param>
        /// <param name="fixtures">fixtures.</param>
        public SportSchedulesByTeamIdResponseDataInnerRoundsInner(decimal id = default(decimal), decimal sportId = default(decimal), decimal leagueId = default(decimal), decimal seasonId = default(decimal), decimal stageId = default(decimal), string name = default(string), bool finished = default(bool), bool isCurrent = default(bool), string startingAt = default(string), string endingAt = default(string), List<SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner> fixtures = default(List<SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner>))
        {
            this.Id = id;
            this.SportId = sportId;
            this.LeagueId = leagueId;
            this.SeasonId = seasonId;
            this.StageId = stageId;
            this.Name = name;
            this.Finished = finished;
            this.IsCurrent = isCurrent;
            this.StartingAt = startingAt;
            this.EndingAt = endingAt;
            this.Fixtures = fixtures;
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
        /// Gets or Sets LeagueId
        /// </summary>
        [DataMember(Name = "league_id", EmitDefaultValue = false)]
        public decimal LeagueId { get; set; }

        /// <summary>
        /// Gets or Sets SeasonId
        /// </summary>
        [DataMember(Name = "season_id", EmitDefaultValue = false)]
        public decimal SeasonId { get; set; }

        /// <summary>
        /// Gets or Sets StageId
        /// </summary>
        [DataMember(Name = "stage_id", EmitDefaultValue = false)]
        public decimal StageId { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name = "name", EmitDefaultValue = false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets Finished
        /// </summary>
        [DataMember(Name = "finished", EmitDefaultValue = true)]
        public bool Finished { get; set; }

        /// <summary>
        /// Gets or Sets IsCurrent
        /// </summary>
        [DataMember(Name = "is_current", EmitDefaultValue = true)]
        public bool IsCurrent { get; set; }

        /// <summary>
        /// Gets or Sets StartingAt
        /// </summary>
        [DataMember(Name = "starting_at", EmitDefaultValue = false)]
        public string StartingAt { get; set; }

        /// <summary>
        /// Gets or Sets EndingAt
        /// </summary>
        [DataMember(Name = "ending_at", EmitDefaultValue = false)]
        public string EndingAt { get; set; }

        /// <summary>
        /// Gets or Sets Fixtures
        /// </summary>
        [DataMember(Name = "fixtures", EmitDefaultValue = false)]
        public List<SportSchedulesByTeamIdResponseDataInnerRoundsInnerFixturesInner> Fixtures { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportSchedulesByTeamIdResponseDataInnerRoundsInner {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  SportId: ").Append(SportId).Append("\n");
            sb.Append("  LeagueId: ").Append(LeagueId).Append("\n");
            sb.Append("  SeasonId: ").Append(SeasonId).Append("\n");
            sb.Append("  StageId: ").Append(StageId).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  Finished: ").Append(Finished).Append("\n");
            sb.Append("  IsCurrent: ").Append(IsCurrent).Append("\n");
            sb.Append("  StartingAt: ").Append(StartingAt).Append("\n");
            sb.Append("  EndingAt: ").Append(EndingAt).Append("\n");
            sb.Append("  Fixtures: ").Append(Fixtures).Append("\n");
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
            return this.Equals(input as SportSchedulesByTeamIdResponseDataInnerRoundsInner);
        }

        /// <summary>
        /// Returns true if SportSchedulesByTeamIdResponseDataInnerRoundsInner instances are equal
        /// </summary>
        /// <param name="input">Instance of SportSchedulesByTeamIdResponseDataInnerRoundsInner to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportSchedulesByTeamIdResponseDataInnerRoundsInner input)
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
                    this.LeagueId == input.LeagueId ||
                    this.LeagueId.Equals(input.LeagueId)
                ) && 
                (
                    this.SeasonId == input.SeasonId ||
                    this.SeasonId.Equals(input.SeasonId)
                ) && 
                (
                    this.StageId == input.StageId ||
                    this.StageId.Equals(input.StageId)
                ) && 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.Finished == input.Finished ||
                    this.Finished.Equals(input.Finished)
                ) && 
                (
                    this.IsCurrent == input.IsCurrent ||
                    this.IsCurrent.Equals(input.IsCurrent)
                ) && 
                (
                    this.StartingAt == input.StartingAt ||
                    (this.StartingAt != null &&
                    this.StartingAt.Equals(input.StartingAt))
                ) && 
                (
                    this.EndingAt == input.EndingAt ||
                    (this.EndingAt != null &&
                    this.EndingAt.Equals(input.EndingAt))
                ) && 
                (
                    this.Fixtures == input.Fixtures ||
                    this.Fixtures != null &&
                    input.Fixtures != null &&
                    this.Fixtures.SequenceEqual(input.Fixtures)
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
                hashCode = (hashCode * 59) + this.LeagueId.GetHashCode();
                hashCode = (hashCode * 59) + this.SeasonId.GetHashCode();
                hashCode = (hashCode * 59) + this.StageId.GetHashCode();
                if (this.Name != null)
                {
                    hashCode = (hashCode * 59) + this.Name.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.Finished.GetHashCode();
                hashCode = (hashCode * 59) + this.IsCurrent.GetHashCode();
                if (this.StartingAt != null)
                {
                    hashCode = (hashCode * 59) + this.StartingAt.GetHashCode();
                }
                if (this.EndingAt != null)
                {
                    hashCode = (hashCode * 59) + this.EndingAt.GetHashCode();
                }
                if (this.Fixtures != null)
                {
                    hashCode = (hashCode * 59) + this.Fixtures.GetHashCode();
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
