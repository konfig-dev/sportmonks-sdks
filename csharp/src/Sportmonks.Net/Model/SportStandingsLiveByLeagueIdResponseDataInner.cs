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
    /// SportStandingsLiveByLeagueIdResponseDataInner
    /// </summary>
    [DataContract(Name = "SportStandingsLiveByLeagueIdResponse_data_inner")]
    public partial class SportStandingsLiveByLeagueIdResponseDataInner : IEquatable<SportStandingsLiveByLeagueIdResponseDataInner>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportStandingsLiveByLeagueIdResponseDataInner" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="sportId">sportId.</param>
        /// <param name="leagueId">leagueId.</param>
        /// <param name="seasonId">seasonId.</param>
        /// <param name="stageId">stageId.</param>
        /// <param name="groupId">groupId.</param>
        /// <param name="roundId">roundId.</param>
        /// <param name="participantId">participantId.</param>
        /// <param name="standingRuleId">standingRuleId.</param>
        /// <param name="position">position.</param>
        /// <param name="points">points.</param>
        /// <param name="result">result.</param>
        public SportStandingsLiveByLeagueIdResponseDataInner(decimal id = default(decimal), decimal sportId = default(decimal), decimal leagueId = default(decimal), decimal seasonId = default(decimal), decimal stageId = default(decimal), string groupId = default(string), decimal roundId = default(decimal), decimal participantId = default(decimal), decimal standingRuleId = default(decimal), decimal position = default(decimal), decimal points = default(decimal), string result = default(string))
        {
            this.Id = id;
            this.SportId = sportId;
            this.LeagueId = leagueId;
            this.SeasonId = seasonId;
            this.StageId = stageId;
            this.GroupId = groupId;
            this.RoundId = roundId;
            this.ParticipantId = participantId;
            this.StandingRuleId = standingRuleId;
            this.Position = position;
            this.Points = points;
            this.Result = result;
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
        /// Gets or Sets GroupId
        /// </summary>
        [DataMember(Name = "group_id", EmitDefaultValue = true)]
        public string GroupId { get; set; }

        /// <summary>
        /// Gets or Sets RoundId
        /// </summary>
        [DataMember(Name = "round_id", EmitDefaultValue = false)]
        public decimal RoundId { get; set; }

        /// <summary>
        /// Gets or Sets ParticipantId
        /// </summary>
        [DataMember(Name = "participant_id", EmitDefaultValue = false)]
        public decimal ParticipantId { get; set; }

        /// <summary>
        /// Gets or Sets StandingRuleId
        /// </summary>
        [DataMember(Name = "standing_rule_id", EmitDefaultValue = false)]
        public decimal StandingRuleId { get; set; }

        /// <summary>
        /// Gets or Sets Position
        /// </summary>
        [DataMember(Name = "position", EmitDefaultValue = false)]
        public decimal Position { get; set; }

        /// <summary>
        /// Gets or Sets Points
        /// </summary>
        [DataMember(Name = "points", EmitDefaultValue = false)]
        public decimal Points { get; set; }

        /// <summary>
        /// Gets or Sets Result
        /// </summary>
        [DataMember(Name = "result", EmitDefaultValue = false)]
        public string Result { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportStandingsLiveByLeagueIdResponseDataInner {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  SportId: ").Append(SportId).Append("\n");
            sb.Append("  LeagueId: ").Append(LeagueId).Append("\n");
            sb.Append("  SeasonId: ").Append(SeasonId).Append("\n");
            sb.Append("  StageId: ").Append(StageId).Append("\n");
            sb.Append("  GroupId: ").Append(GroupId).Append("\n");
            sb.Append("  RoundId: ").Append(RoundId).Append("\n");
            sb.Append("  ParticipantId: ").Append(ParticipantId).Append("\n");
            sb.Append("  StandingRuleId: ").Append(StandingRuleId).Append("\n");
            sb.Append("  Position: ").Append(Position).Append("\n");
            sb.Append("  Points: ").Append(Points).Append("\n");
            sb.Append("  Result: ").Append(Result).Append("\n");
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
            return this.Equals(input as SportStandingsLiveByLeagueIdResponseDataInner);
        }

        /// <summary>
        /// Returns true if SportStandingsLiveByLeagueIdResponseDataInner instances are equal
        /// </summary>
        /// <param name="input">Instance of SportStandingsLiveByLeagueIdResponseDataInner to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportStandingsLiveByLeagueIdResponseDataInner input)
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
                    this.GroupId == input.GroupId ||
                    (this.GroupId != null &&
                    this.GroupId.Equals(input.GroupId))
                ) && 
                (
                    this.RoundId == input.RoundId ||
                    this.RoundId.Equals(input.RoundId)
                ) && 
                (
                    this.ParticipantId == input.ParticipantId ||
                    this.ParticipantId.Equals(input.ParticipantId)
                ) && 
                (
                    this.StandingRuleId == input.StandingRuleId ||
                    this.StandingRuleId.Equals(input.StandingRuleId)
                ) && 
                (
                    this.Position == input.Position ||
                    this.Position.Equals(input.Position)
                ) && 
                (
                    this.Points == input.Points ||
                    this.Points.Equals(input.Points)
                ) && 
                (
                    this.Result == input.Result ||
                    (this.Result != null &&
                    this.Result.Equals(input.Result))
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
                if (this.GroupId != null)
                {
                    hashCode = (hashCode * 59) + this.GroupId.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.RoundId.GetHashCode();
                hashCode = (hashCode * 59) + this.ParticipantId.GetHashCode();
                hashCode = (hashCode * 59) + this.StandingRuleId.GetHashCode();
                hashCode = (hashCode * 59) + this.Position.GetHashCode();
                hashCode = (hashCode * 59) + this.Points.GetHashCode();
                if (this.Result != null)
                {
                    hashCode = (hashCode * 59) + this.Result.GetHashCode();
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
