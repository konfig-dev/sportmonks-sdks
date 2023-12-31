/*
 * SportMonks
 *
 * Surpass the competition with superior sports data
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://konfigthis.com
 */


using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Net;
using System.Net.Mime;
using Sportmonks.Net.Client;
using Sportmonks.Net.Model;

namespace Sportmonks.Net.Api
{

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface ICountriesApiSync : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// All
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>CountriesAllResponse</returns>
        CountriesAllResponse All(string version = default(string), int operationIndex = 0);

        /// <summary>
        /// All
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of CountriesAllResponse</returns>
        ApiResponse<CountriesAllResponse> AllWithHttpInfo(string version = default(string), int operationIndex = 0);
        /// <summary>
        /// By ID
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="countryId">The ID of the country you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>CountriesGetByIdResponse</returns>
        CountriesGetByIdResponse GetById(int countryId, string version = default(string), int operationIndex = 0);

        /// <summary>
        /// By ID
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="countryId">The ID of the country you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of CountriesGetByIdResponse</returns>
        ApiResponse<CountriesGetByIdResponse> GetByIdWithHttpInfo(int countryId, string version = default(string), int operationIndex = 0);
        /// <summary>
        /// Search
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name you want to search on</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>CountriesSearchResponse</returns>
        CountriesSearchResponse Search(string name, string version = default(string), int operationIndex = 0);

        /// <summary>
        /// Search
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name you want to search on</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of CountriesSearchResponse</returns>
        ApiResponse<CountriesSearchResponse> SearchWithHttpInfo(string name, string version = default(string), int operationIndex = 0);
        #endregion Synchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface ICountriesApiAsync : IApiAccessor
    {
        #region Asynchronous Operations
        /// <summary>
        /// All
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of CountriesAllResponse</returns>
        System.Threading.Tasks.Task<CountriesAllResponse> AllAsync(string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));

        /// <summary>
        /// All
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (CountriesAllResponse)</returns>
        System.Threading.Tasks.Task<ApiResponse<CountriesAllResponse>> AllWithHttpInfoAsync(string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));
        /// <summary>
        /// By ID
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="countryId">The ID of the country you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of CountriesGetByIdResponse</returns>
        System.Threading.Tasks.Task<CountriesGetByIdResponse> GetByIdAsync(int countryId, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));

        /// <summary>
        /// By ID
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="countryId">The ID of the country you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (CountriesGetByIdResponse)</returns>
        System.Threading.Tasks.Task<ApiResponse<CountriesGetByIdResponse>> GetByIdWithHttpInfoAsync(int countryId, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));
        /// <summary>
        /// Search
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name you want to search on</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of CountriesSearchResponse</returns>
        System.Threading.Tasks.Task<CountriesSearchResponse> SearchAsync(string name, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));

        /// <summary>
        /// Search
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name you want to search on</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (CountriesSearchResponse)</returns>
        System.Threading.Tasks.Task<ApiResponse<CountriesSearchResponse>> SearchWithHttpInfoAsync(string name, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface ICountriesApi : ICountriesApiSync, ICountriesApiAsync
    {

    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public partial class CountriesApi : ICountriesApi
    {
        private Sportmonks.Net.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="CountriesApi"/> class.
        /// </summary>
        /// <returns></returns>
        public CountriesApi() : this((string)null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CountriesApi"/> class.
        /// </summary>
        /// <returns></returns>
        public CountriesApi(string basePath)
        {
            this.Configuration = Sportmonks.Net.Client.Configuration.MergeConfigurations(
                Sportmonks.Net.Client.GlobalConfiguration.Instance,
                new Sportmonks.Net.Client.Configuration { BasePath = basePath }
            );
            this.Client = new Sportmonks.Net.Client.ApiClient(this.Configuration);
            this.AsynchronousClient = new Sportmonks.Net.Client.ApiClient(this.Configuration);
            this.ExceptionFactory = Sportmonks.Net.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CountriesApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public CountriesApi(Sportmonks.Net.Client.Configuration configuration)
        {
            if (configuration == null) throw new ArgumentNullException("configuration");

            this.Configuration = Sportmonks.Net.Client.Configuration.MergeConfigurations(
                Sportmonks.Net.Client.GlobalConfiguration.Instance,
                configuration
            );
            this.Client = new Sportmonks.Net.Client.ApiClient(this.Configuration);
            this.AsynchronousClient = new Sportmonks.Net.Client.ApiClient(this.Configuration);
            this.ExceptionFactory = Sportmonks.Net.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="CountriesApi"/> class
        /// using a Configuration object and client instance.
        /// </summary>
        /// <param name="client">The client interface for synchronous API access.</param>
        /// <param name="asyncClient">The client interface for asynchronous API access.</param>
        /// <param name="configuration">The configuration object.</param>
        public CountriesApi(Sportmonks.Net.Client.ISynchronousClient client, Sportmonks.Net.Client.IAsynchronousClient asyncClient, Sportmonks.Net.Client.IReadableConfiguration configuration)
        {
            if (client == null) throw new ArgumentNullException("client");
            if (asyncClient == null) throw new ArgumentNullException("asyncClient");
            if (configuration == null) throw new ArgumentNullException("configuration");

            this.Client = client;
            this.AsynchronousClient = asyncClient;
            this.Configuration = configuration;
            this.ExceptionFactory = Sportmonks.Net.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// The client for accessing this underlying API asynchronously.
        /// </summary>
        public Sportmonks.Net.Client.IAsynchronousClient AsynchronousClient { get; set; }

        /// <summary>
        /// The client for accessing this underlying API synchronously.
        /// </summary>
        public Sportmonks.Net.Client.ISynchronousClient Client { get; set; }

        /// <summary>
        /// Gets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        public string GetBasePath()
        {
            return this.Configuration.BasePath;
        }

        /// <summary>
        /// Gets or sets the configuration object
        /// </summary>
        /// <value>An instance of the Configuration</value>
        public Sportmonks.Net.Client.IReadableConfiguration Configuration { get; set; }

        /// <summary>
        /// Provides a factory method hook for the creation of exceptions.
        /// </summary>
        public Sportmonks.Net.Client.ExceptionFactory ExceptionFactory
        {
            get
            {
                if (_exceptionFactory != null && _exceptionFactory.GetInvocationList().Length > 1)
                {
                    throw new InvalidOperationException("Multicast delegate for ExceptionFactory is unsupported.");
                }
                return _exceptionFactory;
            }
            set { _exceptionFactory = value; }
        }

        /// <summary>
        /// All 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>CountriesAllResponse</returns>
        public CountriesAllResponse All(string version = default(string), int operationIndex = 0)
        {
            Sportmonks.Net.Client.ApiResponse<CountriesAllResponse> localVarResponse = AllWithHttpInfo(version);
            return localVarResponse.Data;
        }

        /// <summary>
        /// All 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of CountriesAllResponse</returns>
        public Sportmonks.Net.Client.ApiResponse<CountriesAllResponse> AllWithHttpInfo(string version = default(string), int operationIndex = 0)
        {
            Sportmonks.Net.Client.RequestOptions localVarRequestOptions = new Sportmonks.Net.Client.RequestOptions();

            string[] _contentTypes = new string[] {
            };

            // to determine the Accept header
            string[] _accepts = new string[] {
                "application/json"
            };

            var localVarContentType = Sportmonks.Net.Client.ClientUtils.SelectHeaderContentType(_contentTypes);
            if (localVarContentType != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Content-Type", localVarContentType);
            }

            var localVarAccept = Sportmonks.Net.Client.ClientUtils.SelectHeaderAccept(_accepts);
            if (localVarAccept != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Accept", localVarAccept);
            }

            if (version != null)
            {
                localVarRequestOptions.PathParameters.Add("version", Sportmonks.Net.Client.ClientUtils.ParameterToString(version)); // path parameter
            }

            localVarRequestOptions.Operation = "CountriesApi.All";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required
            if (!string.IsNullOrEmpty(this.Configuration.GetApiKeyWithPrefix("Authorization")))
            {
                localVarRequestOptions.HeaderParameters.Add("Authorization", this.Configuration.GetApiKeyWithPrefix("Authorization"));
            }

            // make the HTTP request
            var localVarResponse = this.Client.Get<CountriesAllResponse>("/{version}/core/countries", localVarRequestOptions, this.Configuration);
            if (this.ExceptionFactory != null)
            {
                Exception _exception = this.ExceptionFactory("All", localVarResponse);
                if (_exception != null)
                {
                    throw _exception;
                }
            }

            return localVarResponse;
        }

        /// <summary>
        /// All 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of CountriesAllResponse</returns>
        public async System.Threading.Tasks.Task<CountriesAllResponse> AllAsync(string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            Sportmonks.Net.Client.ApiResponse<CountriesAllResponse> localVarResponse = await AllWithHttpInfoAsync(version, operationIndex, cancellationToken).ConfigureAwait(false);
            return localVarResponse.Data;
        }

        /// <summary>
        /// All 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (CountriesAllResponse)</returns>
        public async System.Threading.Tasks.Task<Sportmonks.Net.Client.ApiResponse<CountriesAllResponse>> AllWithHttpInfoAsync(string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {

            Sportmonks.Net.Client.RequestOptions localVarRequestOptions = new Sportmonks.Net.Client.RequestOptions();

            string[] _contentTypes = new string[] {
            };

            // to determine the Accept header
            string[] _accepts = new string[] {
                "application/json"
            };

            var localVarContentType = Sportmonks.Net.Client.ClientUtils.SelectHeaderContentType(_contentTypes);
            if (localVarContentType != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Content-Type", localVarContentType);
            }

            var localVarAccept = Sportmonks.Net.Client.ClientUtils.SelectHeaderAccept(_accepts);
            if (localVarAccept != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Accept", localVarAccept);
            }

            if (version != null)
            {
                localVarRequestOptions.PathParameters.Add("version", Sportmonks.Net.Client.ClientUtils.ParameterToString(version)); // path parameter
            }

            localVarRequestOptions.Operation = "CountriesApi.All";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required
            if (!string.IsNullOrEmpty(this.Configuration.GetApiKeyWithPrefix("Authorization")))
            {
                localVarRequestOptions.HeaderParameters.Add("Authorization", this.Configuration.GetApiKeyWithPrefix("Authorization"));
            }

            // make the HTTP request
            var localVarResponse = await this.AsynchronousClient.GetAsync<CountriesAllResponse>("/{version}/core/countries", localVarRequestOptions, this.Configuration, cancellationToken).ConfigureAwait(false);

            if (this.ExceptionFactory != null)
            {
                Exception _exception = this.ExceptionFactory("All", localVarResponse);
                if (_exception != null)
                {
                    throw _exception;
                }
            }

            return localVarResponse;
        }

        /// <summary>
        /// By ID 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="countryId">The ID of the country you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>CountriesGetByIdResponse</returns>
        public CountriesGetByIdResponse GetById(int countryId, string version = default(string), int operationIndex = 0)
        {
            Sportmonks.Net.Client.ApiResponse<CountriesGetByIdResponse> localVarResponse = GetByIdWithHttpInfo(countryId, version);
            return localVarResponse.Data;
        }

        /// <summary>
        /// By ID 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="countryId">The ID of the country you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of CountriesGetByIdResponse</returns>
        public Sportmonks.Net.Client.ApiResponse<CountriesGetByIdResponse> GetByIdWithHttpInfo(int countryId, string version = default(string), int operationIndex = 0)
        {
            Sportmonks.Net.Client.RequestOptions localVarRequestOptions = new Sportmonks.Net.Client.RequestOptions();

            string[] _contentTypes = new string[] {
            };

            // to determine the Accept header
            string[] _accepts = new string[] {
                "application/json"
            };

            var localVarContentType = Sportmonks.Net.Client.ClientUtils.SelectHeaderContentType(_contentTypes);
            if (localVarContentType != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Content-Type", localVarContentType);
            }

            var localVarAccept = Sportmonks.Net.Client.ClientUtils.SelectHeaderAccept(_accepts);
            if (localVarAccept != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Accept", localVarAccept);
            }

            if (version != null)
            {
                localVarRequestOptions.PathParameters.Add("version", Sportmonks.Net.Client.ClientUtils.ParameterToString(version)); // path parameter
            }
            localVarRequestOptions.PathParameters.Add("countryId", Sportmonks.Net.Client.ClientUtils.ParameterToString(countryId)); // path parameter

            localVarRequestOptions.Operation = "CountriesApi.GetById";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required
            if (!string.IsNullOrEmpty(this.Configuration.GetApiKeyWithPrefix("Authorization")))
            {
                localVarRequestOptions.HeaderParameters.Add("Authorization", this.Configuration.GetApiKeyWithPrefix("Authorization"));
            }

            // make the HTTP request
            var localVarResponse = this.Client.Get<CountriesGetByIdResponse>("/{version}/core/countries/{countryId}", localVarRequestOptions, this.Configuration);
            if (this.ExceptionFactory != null)
            {
                Exception _exception = this.ExceptionFactory("GetById", localVarResponse);
                if (_exception != null)
                {
                    throw _exception;
                }
            }

            return localVarResponse;
        }

        /// <summary>
        /// By ID 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="countryId">The ID of the country you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of CountriesGetByIdResponse</returns>
        public async System.Threading.Tasks.Task<CountriesGetByIdResponse> GetByIdAsync(int countryId, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            Sportmonks.Net.Client.ApiResponse<CountriesGetByIdResponse> localVarResponse = await GetByIdWithHttpInfoAsync(countryId, version, operationIndex, cancellationToken).ConfigureAwait(false);
            return localVarResponse.Data;
        }

        /// <summary>
        /// By ID 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="countryId">The ID of the country you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (CountriesGetByIdResponse)</returns>
        public async System.Threading.Tasks.Task<Sportmonks.Net.Client.ApiResponse<CountriesGetByIdResponse>> GetByIdWithHttpInfoAsync(int countryId, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {

            Sportmonks.Net.Client.RequestOptions localVarRequestOptions = new Sportmonks.Net.Client.RequestOptions();

            string[] _contentTypes = new string[] {
            };

            // to determine the Accept header
            string[] _accepts = new string[] {
                "application/json"
            };

            var localVarContentType = Sportmonks.Net.Client.ClientUtils.SelectHeaderContentType(_contentTypes);
            if (localVarContentType != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Content-Type", localVarContentType);
            }

            var localVarAccept = Sportmonks.Net.Client.ClientUtils.SelectHeaderAccept(_accepts);
            if (localVarAccept != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Accept", localVarAccept);
            }

            if (version != null)
            {
                localVarRequestOptions.PathParameters.Add("version", Sportmonks.Net.Client.ClientUtils.ParameterToString(version)); // path parameter
            }
            localVarRequestOptions.PathParameters.Add("countryId", Sportmonks.Net.Client.ClientUtils.ParameterToString(countryId)); // path parameter

            localVarRequestOptions.Operation = "CountriesApi.GetById";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required
            if (!string.IsNullOrEmpty(this.Configuration.GetApiKeyWithPrefix("Authorization")))
            {
                localVarRequestOptions.HeaderParameters.Add("Authorization", this.Configuration.GetApiKeyWithPrefix("Authorization"));
            }

            // make the HTTP request
            var localVarResponse = await this.AsynchronousClient.GetAsync<CountriesGetByIdResponse>("/{version}/core/countries/{countryId}", localVarRequestOptions, this.Configuration, cancellationToken).ConfigureAwait(false);

            if (this.ExceptionFactory != null)
            {
                Exception _exception = this.ExceptionFactory("GetById", localVarResponse);
                if (_exception != null)
                {
                    throw _exception;
                }
            }

            return localVarResponse;
        }

        /// <summary>
        /// Search 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name you want to search on</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>CountriesSearchResponse</returns>
        public CountriesSearchResponse Search(string name, string version = default(string), int operationIndex = 0)
        {
            Sportmonks.Net.Client.ApiResponse<CountriesSearchResponse> localVarResponse = SearchWithHttpInfo(name, version);
            return localVarResponse.Data;
        }

        /// <summary>
        /// Search 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name you want to search on</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of CountriesSearchResponse</returns>
        public Sportmonks.Net.Client.ApiResponse<CountriesSearchResponse> SearchWithHttpInfo(string name, string version = default(string), int operationIndex = 0)
        {
            // verify the required parameter 'name' is set
            if (name == null)
            {
                throw new Sportmonks.Net.Client.ApiException(400, "Missing required parameter 'name' when calling CountriesApi->Search");
            }

            Sportmonks.Net.Client.RequestOptions localVarRequestOptions = new Sportmonks.Net.Client.RequestOptions();

            string[] _contentTypes = new string[] {
            };

            // to determine the Accept header
            string[] _accepts = new string[] {
                "application/json"
            };

            var localVarContentType = Sportmonks.Net.Client.ClientUtils.SelectHeaderContentType(_contentTypes);
            if (localVarContentType != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Content-Type", localVarContentType);
            }

            var localVarAccept = Sportmonks.Net.Client.ClientUtils.SelectHeaderAccept(_accepts);
            if (localVarAccept != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Accept", localVarAccept);
            }

            if (version != null)
            {
                localVarRequestOptions.PathParameters.Add("version", Sportmonks.Net.Client.ClientUtils.ParameterToString(version)); // path parameter
            }
            localVarRequestOptions.PathParameters.Add("name", Sportmonks.Net.Client.ClientUtils.ParameterToString(name)); // path parameter

            localVarRequestOptions.Operation = "CountriesApi.Search";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required
            if (!string.IsNullOrEmpty(this.Configuration.GetApiKeyWithPrefix("Authorization")))
            {
                localVarRequestOptions.HeaderParameters.Add("Authorization", this.Configuration.GetApiKeyWithPrefix("Authorization"));
            }

            // make the HTTP request
            var localVarResponse = this.Client.Get<CountriesSearchResponse>("/{version}/core/countries/search/{name}", localVarRequestOptions, this.Configuration);
            if (this.ExceptionFactory != null)
            {
                Exception _exception = this.ExceptionFactory("Search", localVarResponse);
                if (_exception != null)
                {
                    throw _exception;
                }
            }

            return localVarResponse;
        }

        /// <summary>
        /// Search 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name you want to search on</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of CountriesSearchResponse</returns>
        public async System.Threading.Tasks.Task<CountriesSearchResponse> SearchAsync(string name, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            Sportmonks.Net.Client.ApiResponse<CountriesSearchResponse> localVarResponse = await SearchWithHttpInfoAsync(name, version, operationIndex, cancellationToken).ConfigureAwait(false);
            return localVarResponse.Data;
        }

        /// <summary>
        /// Search 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name you want to search on</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (CountriesSearchResponse)</returns>
        public async System.Threading.Tasks.Task<Sportmonks.Net.Client.ApiResponse<CountriesSearchResponse>> SearchWithHttpInfoAsync(string name, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            // verify the required parameter 'name' is set
            if (name == null)
            {
                throw new Sportmonks.Net.Client.ApiException(400, "Missing required parameter 'name' when calling CountriesApi->Search");
            }


            Sportmonks.Net.Client.RequestOptions localVarRequestOptions = new Sportmonks.Net.Client.RequestOptions();

            string[] _contentTypes = new string[] {
            };

            // to determine the Accept header
            string[] _accepts = new string[] {
                "application/json"
            };

            var localVarContentType = Sportmonks.Net.Client.ClientUtils.SelectHeaderContentType(_contentTypes);
            if (localVarContentType != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Content-Type", localVarContentType);
            }

            var localVarAccept = Sportmonks.Net.Client.ClientUtils.SelectHeaderAccept(_accepts);
            if (localVarAccept != null)
            {
                localVarRequestOptions.HeaderParameters.Add("Accept", localVarAccept);
            }

            if (version != null)
            {
                localVarRequestOptions.PathParameters.Add("version", Sportmonks.Net.Client.ClientUtils.ParameterToString(version)); // path parameter
            }
            localVarRequestOptions.PathParameters.Add("name", Sportmonks.Net.Client.ClientUtils.ParameterToString(name)); // path parameter

            localVarRequestOptions.Operation = "CountriesApi.Search";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required
            if (!string.IsNullOrEmpty(this.Configuration.GetApiKeyWithPrefix("Authorization")))
            {
                localVarRequestOptions.HeaderParameters.Add("Authorization", this.Configuration.GetApiKeyWithPrefix("Authorization"));
            }

            // make the HTTP request
            var localVarResponse = await this.AsynchronousClient.GetAsync<CountriesSearchResponse>("/{version}/core/countries/search/{name}", localVarRequestOptions, this.Configuration, cancellationToken).ConfigureAwait(false);

            if (this.ExceptionFactory != null)
            {
                Exception _exception = this.ExceptionFactory("Search", localVarResponse);
                if (_exception != null)
                {
                    throw _exception;
                }
            }

            return localVarResponse;
        }

    }
}
