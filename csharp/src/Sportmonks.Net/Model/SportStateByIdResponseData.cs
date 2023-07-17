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
    /// SportStateByIdResponseData
    /// </summary>
    [DataContract(Name = "SportStateByIdResponse_data")]
    public partial class SportStateByIdResponseData : IEquatable<SportStateByIdResponseData>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="SportStateByIdResponseData" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="state">state.</param>
        /// <param name="name">name.</param>
        /// <param name="shortName">shortName.</param>
        /// <param name="developerName">developerName.</param>
        /// <param name="isLive">isLive.</param>
        /// <param name="isPending">isPending.</param>
        /// <param name="isPeriodEnd">isPeriodEnd.</param>
        /// <param name="isFinalState">isFinalState.</param>
        /// <param name="isCancelled">isCancelled.</param>
        /// <param name="isFinalStandingState">isFinalStandingState.</param>
        /// <param name="isCompleted">isCompleted.</param>
        /// <param name="typeId">typeId.</param>
        /// <param name="isDeleted">isDeleted.</param>
        /// <param name="isNotstarted">isNotstarted.</param>
        /// <param name="sectionsActive">sectionsActive.</param>
        /// <param name="scheduleOverrule">scheduleOverrule.</param>
        public SportStateByIdResponseData(decimal id = default(decimal), string state = default(string), string name = default(string), string shortName = default(string), string developerName = default(string), bool isLive = default(bool), bool isPending = default(bool), bool isPeriodEnd = default(bool), bool isFinalState = default(bool), bool isCancelled = default(bool), bool isFinalStandingState = default(bool), bool isCompleted = default(bool), string typeId = default(string), bool isDeleted = default(bool), bool isNotstarted = default(bool), bool sectionsActive = default(bool), bool scheduleOverrule = default(bool))
        {
            this.Id = id;
            this.State = state;
            this.Name = name;
            this.ShortName = shortName;
            this.DeveloperName = developerName;
            this.IsLive = isLive;
            this.IsPending = isPending;
            this.IsPeriodEnd = isPeriodEnd;
            this.IsFinalState = isFinalState;
            this.IsCancelled = isCancelled;
            this.IsFinalStandingState = isFinalStandingState;
            this.IsCompleted = isCompleted;
            this.TypeId = typeId;
            this.IsDeleted = isDeleted;
            this.IsNotstarted = isNotstarted;
            this.SectionsActive = sectionsActive;
            this.ScheduleOverrule = scheduleOverrule;
        }

        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name = "id", EmitDefaultValue = false)]
        public decimal Id { get; set; }

        /// <summary>
        /// Gets or Sets State
        /// </summary>
        [DataMember(Name = "state", EmitDefaultValue = false)]
        public string State { get; set; }

        /// <summary>
        /// Gets or Sets Name
        /// </summary>
        [DataMember(Name = "name", EmitDefaultValue = false)]
        public string Name { get; set; }

        /// <summary>
        /// Gets or Sets ShortName
        /// </summary>
        [DataMember(Name = "short_name", EmitDefaultValue = false)]
        public string ShortName { get; set; }

        /// <summary>
        /// Gets or Sets DeveloperName
        /// </summary>
        [DataMember(Name = "developer_name", EmitDefaultValue = false)]
        public string DeveloperName { get; set; }

        /// <summary>
        /// Gets or Sets IsLive
        /// </summary>
        [DataMember(Name = "is_live", EmitDefaultValue = true)]
        public bool IsLive { get; set; }

        /// <summary>
        /// Gets or Sets IsPending
        /// </summary>
        [DataMember(Name = "is_pending", EmitDefaultValue = true)]
        public bool IsPending { get; set; }

        /// <summary>
        /// Gets or Sets IsPeriodEnd
        /// </summary>
        [DataMember(Name = "is_period_end", EmitDefaultValue = true)]
        public bool IsPeriodEnd { get; set; }

        /// <summary>
        /// Gets or Sets IsFinalState
        /// </summary>
        [DataMember(Name = "is_final_state", EmitDefaultValue = true)]
        public bool IsFinalState { get; set; }

        /// <summary>
        /// Gets or Sets IsCancelled
        /// </summary>
        [DataMember(Name = "is_cancelled", EmitDefaultValue = true)]
        public bool IsCancelled { get; set; }

        /// <summary>
        /// Gets or Sets IsFinalStandingState
        /// </summary>
        [DataMember(Name = "is_final_standing_state", EmitDefaultValue = true)]
        public bool IsFinalStandingState { get; set; }

        /// <summary>
        /// Gets or Sets IsCompleted
        /// </summary>
        [DataMember(Name = "is_completed", EmitDefaultValue = true)]
        public bool IsCompleted { get; set; }

        /// <summary>
        /// Gets or Sets TypeId
        /// </summary>
        [DataMember(Name = "type_id", EmitDefaultValue = true)]
        public string TypeId { get; set; }

        /// <summary>
        /// Gets or Sets IsDeleted
        /// </summary>
        [DataMember(Name = "is_deleted", EmitDefaultValue = true)]
        public bool IsDeleted { get; set; }

        /// <summary>
        /// Gets or Sets IsNotstarted
        /// </summary>
        [DataMember(Name = "is_notstarted", EmitDefaultValue = true)]
        public bool IsNotstarted { get; set; }

        /// <summary>
        /// Gets or Sets SectionsActive
        /// </summary>
        [DataMember(Name = "sections_active", EmitDefaultValue = true)]
        public bool SectionsActive { get; set; }

        /// <summary>
        /// Gets or Sets ScheduleOverrule
        /// </summary>
        [DataMember(Name = "schedule_overrule", EmitDefaultValue = true)]
        public bool ScheduleOverrule { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append("class SportStateByIdResponseData {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  State: ").Append(State).Append("\n");
            sb.Append("  Name: ").Append(Name).Append("\n");
            sb.Append("  ShortName: ").Append(ShortName).Append("\n");
            sb.Append("  DeveloperName: ").Append(DeveloperName).Append("\n");
            sb.Append("  IsLive: ").Append(IsLive).Append("\n");
            sb.Append("  IsPending: ").Append(IsPending).Append("\n");
            sb.Append("  IsPeriodEnd: ").Append(IsPeriodEnd).Append("\n");
            sb.Append("  IsFinalState: ").Append(IsFinalState).Append("\n");
            sb.Append("  IsCancelled: ").Append(IsCancelled).Append("\n");
            sb.Append("  IsFinalStandingState: ").Append(IsFinalStandingState).Append("\n");
            sb.Append("  IsCompleted: ").Append(IsCompleted).Append("\n");
            sb.Append("  TypeId: ").Append(TypeId).Append("\n");
            sb.Append("  IsDeleted: ").Append(IsDeleted).Append("\n");
            sb.Append("  IsNotstarted: ").Append(IsNotstarted).Append("\n");
            sb.Append("  SectionsActive: ").Append(SectionsActive).Append("\n");
            sb.Append("  ScheduleOverrule: ").Append(ScheduleOverrule).Append("\n");
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
            return this.Equals(input as SportStateByIdResponseData);
        }

        /// <summary>
        /// Returns true if SportStateByIdResponseData instances are equal
        /// </summary>
        /// <param name="input">Instance of SportStateByIdResponseData to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(SportStateByIdResponseData input)
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
                    this.State == input.State ||
                    (this.State != null &&
                    this.State.Equals(input.State))
                ) && 
                (
                    this.Name == input.Name ||
                    (this.Name != null &&
                    this.Name.Equals(input.Name))
                ) && 
                (
                    this.ShortName == input.ShortName ||
                    (this.ShortName != null &&
                    this.ShortName.Equals(input.ShortName))
                ) && 
                (
                    this.DeveloperName == input.DeveloperName ||
                    (this.DeveloperName != null &&
                    this.DeveloperName.Equals(input.DeveloperName))
                ) && 
                (
                    this.IsLive == input.IsLive ||
                    this.IsLive.Equals(input.IsLive)
                ) && 
                (
                    this.IsPending == input.IsPending ||
                    this.IsPending.Equals(input.IsPending)
                ) && 
                (
                    this.IsPeriodEnd == input.IsPeriodEnd ||
                    this.IsPeriodEnd.Equals(input.IsPeriodEnd)
                ) && 
                (
                    this.IsFinalState == input.IsFinalState ||
                    this.IsFinalState.Equals(input.IsFinalState)
                ) && 
                (
                    this.IsCancelled == input.IsCancelled ||
                    this.IsCancelled.Equals(input.IsCancelled)
                ) && 
                (
                    this.IsFinalStandingState == input.IsFinalStandingState ||
                    this.IsFinalStandingState.Equals(input.IsFinalStandingState)
                ) && 
                (
                    this.IsCompleted == input.IsCompleted ||
                    this.IsCompleted.Equals(input.IsCompleted)
                ) && 
                (
                    this.TypeId == input.TypeId ||
                    (this.TypeId != null &&
                    this.TypeId.Equals(input.TypeId))
                ) && 
                (
                    this.IsDeleted == input.IsDeleted ||
                    this.IsDeleted.Equals(input.IsDeleted)
                ) && 
                (
                    this.IsNotstarted == input.IsNotstarted ||
                    this.IsNotstarted.Equals(input.IsNotstarted)
                ) && 
                (
                    this.SectionsActive == input.SectionsActive ||
                    this.SectionsActive.Equals(input.SectionsActive)
                ) && 
                (
                    this.ScheduleOverrule == input.ScheduleOverrule ||
                    this.ScheduleOverrule.Equals(input.ScheduleOverrule)
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
                if (this.State != null)
                {
                    hashCode = (hashCode * 59) + this.State.GetHashCode();
                }
                if (this.Name != null)
                {
                    hashCode = (hashCode * 59) + this.Name.GetHashCode();
                }
                if (this.ShortName != null)
                {
                    hashCode = (hashCode * 59) + this.ShortName.GetHashCode();
                }
                if (this.DeveloperName != null)
                {
                    hashCode = (hashCode * 59) + this.DeveloperName.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.IsLive.GetHashCode();
                hashCode = (hashCode * 59) + this.IsPending.GetHashCode();
                hashCode = (hashCode * 59) + this.IsPeriodEnd.GetHashCode();
                hashCode = (hashCode * 59) + this.IsFinalState.GetHashCode();
                hashCode = (hashCode * 59) + this.IsCancelled.GetHashCode();
                hashCode = (hashCode * 59) + this.IsFinalStandingState.GetHashCode();
                hashCode = (hashCode * 59) + this.IsCompleted.GetHashCode();
                if (this.TypeId != null)
                {
                    hashCode = (hashCode * 59) + this.TypeId.GetHashCode();
                }
                hashCode = (hashCode * 59) + this.IsDeleted.GetHashCode();
                hashCode = (hashCode * 59) + this.IsNotstarted.GetHashCode();
                hashCode = (hashCode * 59) + this.SectionsActive.GetHashCode();
                hashCode = (hashCode * 59) + this.ScheduleOverrule.GetHashCode();
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
