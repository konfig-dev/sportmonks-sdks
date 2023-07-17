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
    /// SportFixturesAllResponseDataInner
    /// </summary>
    [DataContract(Name = "SportFixturesAllResponse_data_inner")]
    public partial class SportFixturesAllResponseDataInner : IEquatable<SportFixturesAllResponseDataInner>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportFixturesAllResponseDataInner" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="sportId">sportId.</param>
        /// <param name="leagueId">leagueId.</param>
        /// <param name="seasonId">seasonId.</param>
        /// <param name="stageId">stageId.</param>
        /// <param name="groupId">groupId.</param>
        /// <param name="aggregateId">aggregateId.</param>
        /// <param name="roundId">roundId.</param>
        /// <param name="stateId">stateId.</param>
        /// <param name="venueId">venueId.</param>
        /// <param name="name">name.</param>
        /// <param name="homeScore">homeScore.</param>
        /// <param name="awayScore">awayScore.</param>
        /// <param name="startingAt">startingAt.</param>
        /// <param name="resultInfo">resultInfo.</param>
        /// <param name="leg">leg.</param>
        /// <param name="details">details.</param>
        /// <param name="length">length.</param>
        /// <param name="placeholder">placeholder.</param>
        /// <param name="lastProcessedAt">lastProcessedAt.</param>
        /// <param name="startingAtTimestamp">startingAtTimestamp.</param>
        public SportFixturesAllResponseDataInner(decimal id = default(decimal), decimal sportId = default(decimal), decimal leagueId = default(decimal), decimal seasonId = default(decimal), decimal stageId = default(decimal), string groupId = default(string), string aggregateId = default(string), decimal roundId = default(decimal), decimal stateId = default(decimal), decimal venueId = default(decimal), string name = default(string), decimal homeScore = default(decimal), decimal awayScore = default(decimal), string startingAt = default(string), string resultInfo = default(string), string leg = default(string), string details = default(string), decimal length = default(decimal), bool placeholder = default(bool), string lastProcessedAt = default(string), decimal startingAtTimestamp = default(decimal))
        {
            this.Id = id;
            this.SportId = sportId;
            this.LeagueId = leagueId;
            this.SeasonId = seasonId;
            this.StageId = stageId;
            this.GroupId = groupId;
            this.AggregateId = aggregateId;
            this.RoundId = roundId;
            this.StateId = stateId;
            this.VenueId = venueId;
            this.Name = name;
            this.HomeScore = homeScore;
            this.AwayScore = awayScore;
            this.StartingAt = startingAt;
            this.ResultInfo = resultInfo;
            this.Leg = leg;
            this.Details = details;
            this.Length = length;
            this.Placeholder = placeholder;
            this.LastProcessedAt = lastProcessedAt;
            this.StartingAtTimestamp = startingAtTimestamp;
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
        /// Gets or Sets AggregateId
        /// </summary>
        [DataMember(Name = "aggregate_id", EmitDefaultValue = true)]
        public string AggregateId { get; set; }

        /// <summary>
        /// Gets or Sets RoundId
        /// </summary>
        [DataMember(Name = "round_id", EmitDefaultValue = false)]
        public decimal RoundId { get; set; }

        /// <summary>
        /// Gets or Sets StateId
        /// </summary>
        [DataMember(Name = "state_id", EmitDefaultValue = false)]
        public decimal StateId { get; set; }

        /// <summary>
        /// Gets or Sets VenueId
        /// </summary>
        [DataMember(Name = "venue_id", EmitDefaultValue = false)]
        public decimal VenueId { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name = "name", EmitDefaultValue = false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets HomeScore
        /// </summary>
        [DataMember(Name = "home_score", EmitDefaultValue = false)]
        public decimal HomeScore { get; set; }

        /// <summary>
        /// Gets or Sets AwayScore
        /// </summary>
        [DataMember(Name = "away_score", EmitDefaultValue = false)]
        public decimal AwayScore { get; set; }

        /// <summary>
        /// Gets or Sets StartingAt
        /// </summary>
        [DataMember(Name = "starting_at", EmitDefaultValue = false)]
        public string StartingAt { get; set; }

        /// <summary>
        /// Gets or Sets ResultInfo
        /// </summary>
        [DataMember(Name = "result_info", EmitDefaultValue = true)]
        public string ResultInfo { get; set; }

        /// <summary>
        /// Gets or Sets Leg
        /// </summary>
        [DataMember(Name = "leg", EmitDefaultValue = false)]
        public string Leg { get; set; }

        /// <summary>
        /// Gets or Sets Details
        /// </summary>
        [DataMember(Name = "details", EmitDefaultValue = true)]
        public string Details { get; set; }

        /// <summary>
        /// Gets or Sets Length
        /// </summary>
        [DataMember(Name = "length", EmitDefaultValue = false)]
        public decimal Length { get; set; }

        /// <summary>
        /// Gets or Sets Placeholder
        /// </summary>
        [DataMember(Name = "placeholder", EmitDefaultValue = true)]
        public bool Placeholder { get; set; }

        /// <summary>
        /// Gets or Sets LastProcessedAt
        /// </summary>
        [DataMember(Name = "last_processed_at", EmitDefaultValue = false)]
        public string LastProcessedAt { get; set; }

        /// <summary>
        /// Gets or Sets StartingAtTimestamp
        /// </summary>
        [DataMember(Name = "starting_at_timestamp", EmitDefaultValue = false)]
        public decimal StartingAtTimestamp { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportFixturesAllResponseDataInner {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  SportId: ").Append(SportId).Append("\n");
            sb.Append("  LeagueId: ").Append(LeagueId).Append("\n");
            sb.Append("  SeasonId: ").Append(SeasonId).Append("\n");
            sb.Append("  StageId: ").Append(StageId).Append("\n");
            sb.Append("  GroupId: ").Append(GroupId).Append("\n");
            sb.Append("  AggregateId: ").Append(AggregateId).Append("\n");
            sb.Append("  RoundId: ").Append(RoundId).Append("\n");
            sb.Append("  StateId: ").Append(StateId).Append("\n");
            sb.Append("  VenueId: ").Append(VenueId).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  HomeScore: ").Append(HomeScore).Append("\n");
            sb.Append("  AwayScore: ").Append(AwayScore).Append("\n");
            sb.Append("  StartingAt: ").Append(StartingAt).Append("\n");
            sb.Append("  ResultInfo: ").Append(ResultInfo).Append("\n");
            sb.Append("  Leg: ").Append(Leg).Append("\n");
            sb.Append("  Details: ").Append(Details).Append("\n");
            sb.Append("  Length: ").Append(Length).Append("\n");
            sb.Append("  Placeholder: ").Append(Placeholder).Append("\n");
            sb.Append("  LastProcessedAt: ").Append(LastProcessedAt).Append("\n");
            sb.Append("  StartingAtTimestamp: ").Append(StartingAtTimestamp).Append("\n");
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
            return this.Equals(input as SportFixturesAllResponseDataInner);
        }

        /// <summary>
        /// Returns true if SportFixturesAllResponseDataInner instances are equal
        /// </summary>
        /// <param name="input">Instance of SportFixturesAllResponseDataInner to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportFixturesAllResponseDataInner input)
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
                    this.AggregateId == input.AggregateId ||
                    (this.AggregateId != null &&
                    this.AggregateId.Equals(input.AggregateId))
                ) && 
                (
                    this.RoundId == input.RoundId ||
                    this.RoundId.Equals(input.RoundId)
                ) && 
                (
                    this.StateId == input.StateId ||
                    this.StateId.Equals(input.StateId)
                ) && 
                (
                    this.VenueId == input.VenueId ||
                    this.VenueId.Equals(input.VenueId)
                ) && 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.HomeScore == input.HomeScore ||
                    this.HomeScore.Equals(input.HomeScore)
                ) && 
                (
                    this.AwayScore == input.AwayScore ||
                    this.AwayScore.Equals(input.AwayScore)
                ) && 
                (
                    this.StartingAt == input.StartingAt ||
                    (this.StartingAt != null &&
                    this.StartingAt.Equals(input.StartingAt))
                ) && 
                (
                    this.ResultInfo == input.ResultInfo ||
                    (this.ResultInfo != null &&
                    this.ResultInfo.Equals(input.ResultInfo))
                ) && 
                (
                    this.Leg == input.Leg ||
                    (this.Leg != null &&
                    this.Leg.Equals(input.Leg))
                ) && 
                (
                    this.Details == input.Details ||
                    (this.Details != null &&
                    this.Details.Equals(input.Details))
                ) && 
                (
                    this.Length == input.Length ||
                    this.Length.Equals(input.Length)
                ) && 
                (
                    this.Placeholder == input.Placeholder ||
                    this.Placeholder.Equals(input.Placeholder)
                ) && 
                (
                    this.LastProcessedAt == input.LastProcessedAt ||
                    (this.LastProcessedAt != null &&
                    this.LastProcessedAt.Equals(input.LastProcessedAt))
                ) && 
                (
                    this.StartingAtTimestamp == input.StartingAtTimestamp ||
                    this.StartingAtTimestamp.Equals(input.StartingAtTimestamp)
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
                if (this.AggregateId != null)
                {
                    hashCode = (hashCode * 59) + this.AggregateId.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.RoundId.GetHashCode();
                hashCode = (hashCode * 59) + this.StateId.GetHashCode();
                hashCode = (hashCode * 59) + this.VenueId.GetHashCode();
                if (this.Name != null)
                {
                    hashCode = (hashCode * 59) + this.Name.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.HomeScore.GetHashCode();
                hashCode = (hashCode * 59) + this.AwayScore.GetHashCode();
                if (this.StartingAt != null)
                {
                    hashCode = (hashCode * 59) + this.StartingAt.GetHashCode();
                }
                if (this.ResultInfo != null)
                {
                    hashCode = (hashCode * 59) + this.ResultInfo.GetHashCode();
                }
                if (this.Leg != null)
                {
                    hashCode = (hashCode * 59) + this.Leg.GetHashCode();
                }
                if (this.Details != null)
                {
                    hashCode = (hashCode * 59) + this.Details.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.Length.GetHashCode();
                hashCode = (hashCode * 59) + this.Placeholder.GetHashCode();
                if (this.LastProcessedAt != null)
                {
                    hashCode = (hashCode * 59) + this.LastProcessedAt.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.StartingAtTimestamp.GetHashCode();
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
