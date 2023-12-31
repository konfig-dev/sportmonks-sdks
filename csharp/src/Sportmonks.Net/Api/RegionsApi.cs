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
    public interface IRegionsApiSync : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// All
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>RegionsAllResponse</returns>
        RegionsAllResponse All(string version = default(string), int operationIndex = 0);

        /// <summary>
        /// All
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of RegionsAllResponse</returns>
        ApiResponse<RegionsAllResponse> AllWithHttpInfo(string version = default(string), int operationIndex = 0);
        /// <summary>
        /// By ID
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="regionId">The ID of the region you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>RegionsGetByIdResponse</returns>
        RegionsGetByIdResponse GetById(int regionId, string version = default(string), int operationIndex = 0);

        /// <summary>
        /// By ID
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="regionId">The ID of the region you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of RegionsGetByIdResponse</returns>
        ApiResponse<RegionsGetByIdResponse> GetByIdWithHttpInfo(int regionId, string version = default(string), int operationIndex = 0);
        /// <summary>
        /// Search
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name you want to search on</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>RegionsSearchResponse</returns>
        RegionsSearchResponse Search(string name, string version = default(string), int operationIndex = 0);

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
        /// <returns>ApiResponse of RegionsSearchResponse</returns>
        ApiResponse<RegionsSearchResponse> SearchWithHttpInfo(string name, string version = default(string), int operationIndex = 0);
        #endregion Synchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface IRegionsApiAsync : IApiAccessor
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
        /// <returns>Task of RegionsAllResponse</returns>
        System.Threading.Tasks.Task<RegionsAllResponse> AllAsync(string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));

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
        /// <returns>Task of ApiResponse (RegionsAllResponse)</returns>
        System.Threading.Tasks.Task<ApiResponse<RegionsAllResponse>> AllWithHttpInfoAsync(string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));
        /// <summary>
        /// By ID
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="regionId">The ID of the region you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of RegionsGetByIdResponse</returns>
        System.Threading.Tasks.Task<RegionsGetByIdResponse> GetByIdAsync(int regionId, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));

        /// <summary>
        /// By ID
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="regionId">The ID of the region you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (RegionsGetByIdResponse)</returns>
        System.Threading.Tasks.Task<ApiResponse<RegionsGetByIdResponse>> GetByIdWithHttpInfoAsync(int regionId, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));
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
        /// <returns>Task of RegionsSearchResponse</returns>
        System.Threading.Tasks.Task<RegionsSearchResponse> SearchAsync(string name, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));

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
        /// <returns>Task of ApiResponse (RegionsSearchResponse)</returns>
        System.Threading.Tasks.Task<ApiResponse<RegionsSearchResponse>> SearchWithHttpInfoAsync(string name, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface IRegionsApi : IRegionsApiSync, IRegionsApiAsync
    {

    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public partial class RegionsApi : IRegionsApi
    {
        private Sportmonks.Net.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="RegionsApi"/> class.
        /// </summary>
        /// <returns></returns>
        public RegionsApi() : this((string)null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="RegionsApi"/> class.
        /// </summary>
        /// <returns></returns>
        public RegionsApi(string basePath)
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
        /// Initializes a new instance of the <see cref="RegionsApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public RegionsApi(Sportmonks.Net.Client.Configuration configuration)
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
        /// Initializes a new instance of the <see cref="RegionsApi"/> class
        /// using a Configuration object and client instance.
        /// </summary>
        /// <param name="client">The client interface for synchronous API access.</param>
        /// <param name="asyncClient">The client interface for asynchronous API access.</param>
        /// <param name="configuration">The configuration object.</param>
        public RegionsApi(Sportmonks.Net.Client.ISynchronousClient client, Sportmonks.Net.Client.IAsynchronousClient asyncClient, Sportmonks.Net.Client.IReadableConfiguration configuration)
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
        /// <returns>RegionsAllResponse</returns>
        public RegionsAllResponse All(string version = default(string), int operationIndex = 0)
        {
            Sportmonks.Net.Client.ApiResponse<RegionsAllResponse> localVarResponse = AllWithHttpInfo(version);
            return localVarResponse.Data;
        }

        /// <summary>
        /// All 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of RegionsAllResponse</returns>
        public Sportmonks.Net.Client.ApiResponse<RegionsAllResponse> AllWithHttpInfo(string version = default(string), int operationIndex = 0)
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

            localVarRequestOptions.Operation = "RegionsApi.All";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required
            if (!string.IsNullOrEmpty(this.Configuration.GetApiKeyWithPrefix("Authorization")))
            {
                localVarRequestOptions.HeaderParameters.Add("Authorization", this.Configuration.GetApiKeyWithPrefix("Authorization"));
            }

            // make the HTTP request
            var localVarResponse = this.Client.Get<RegionsAllResponse>("/{version}/core/regions", localVarRequestOptions, this.Configuration);
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
        /// <returns>Task of RegionsAllResponse</returns>
        public async System.Threading.Tasks.Task<RegionsAllResponse> AllAsync(string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            Sportmonks.Net.Client.ApiResponse<RegionsAllResponse> localVarResponse = await AllWithHttpInfoAsync(version, operationIndex, cancellationToken).ConfigureAwait(false);
            return localVarResponse.Data;
        }

        /// <summary>
        /// All 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (RegionsAllResponse)</returns>
        public async System.Threading.Tasks.Task<Sportmonks.Net.Client.ApiResponse<RegionsAllResponse>> AllWithHttpInfoAsync(string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
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

            localVarRequestOptions.Operation = "RegionsApi.All";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required
            if (!string.IsNullOrEmpty(this.Configuration.GetApiKeyWithPrefix("Authorization")))
            {
                localVarRequestOptions.HeaderParameters.Add("Authorization", this.Configuration.GetApiKeyWithPrefix("Authorization"));
            }

            // make the HTTP request
            var localVarResponse = await this.AsynchronousClient.GetAsync<RegionsAllResponse>("/{version}/core/regions", localVarRequestOptions, this.Configuration, cancellationToken).ConfigureAwait(false);

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
        /// <param name="regionId">The ID of the region you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>RegionsGetByIdResponse</returns>
        public RegionsGetByIdResponse GetById(int regionId, string version = default(string), int operationIndex = 0)
        {
            Sportmonks.Net.Client.ApiResponse<RegionsGetByIdResponse> localVarResponse = GetByIdWithHttpInfo(regionId, version);
            return localVarResponse.Data;
        }

        /// <summary>
        /// By ID 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="regionId">The ID of the region you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of RegionsGetByIdResponse</returns>
        public Sportmonks.Net.Client.ApiResponse<RegionsGetByIdResponse> GetByIdWithHttpInfo(int regionId, string version = default(string), int operationIndex = 0)
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
            localVarRequestOptions.PathParameters.Add("regionId", Sportmonks.Net.Client.ClientUtils.ParameterToString(regionId)); // path parameter

            localVarRequestOptions.Operation = "RegionsApi.GetById";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required
            if (!string.IsNullOrEmpty(this.Configuration.GetApiKeyWithPrefix("Authorization")))
            {
                localVarRequestOptions.HeaderParameters.Add("Authorization", this.Configuration.GetApiKeyWithPrefix("Authorization"));
            }

            // make the HTTP request
            var localVarResponse = this.Client.Get<RegionsGetByIdResponse>("/{version}/core/regions/{regionId}", localVarRequestOptions, this.Configuration);
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
        /// <param name="regionId">The ID of the region you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of RegionsGetByIdResponse</returns>
        public async System.Threading.Tasks.Task<RegionsGetByIdResponse> GetByIdAsync(int regionId, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            Sportmonks.Net.Client.ApiResponse<RegionsGetByIdResponse> localVarResponse = await GetByIdWithHttpInfoAsync(regionId, version, operationIndex, cancellationToken).ConfigureAwait(false);
            return localVarResponse.Data;
        }

        /// <summary>
        /// By ID 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="regionId">The ID of the region you want to retrieve.</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (RegionsGetByIdResponse)</returns>
        public async System.Threading.Tasks.Task<Sportmonks.Net.Client.ApiResponse<RegionsGetByIdResponse>> GetByIdWithHttpInfoAsync(int regionId, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
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
            localVarRequestOptions.PathParameters.Add("regionId", Sportmonks.Net.Client.ClientUtils.ParameterToString(regionId)); // path parameter

            localVarRequestOptions.Operation = "RegionsApi.GetById";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required
            if (!string.IsNullOrEmpty(this.Configuration.GetApiKeyWithPrefix("Authorization")))
            {
                localVarRequestOptions.HeaderParameters.Add("Authorization", this.Configuration.GetApiKeyWithPrefix("Authorization"));
            }

            // make the HTTP request
            var localVarResponse = await this.AsynchronousClient.GetAsync<RegionsGetByIdResponse>("/{version}/core/regions/{regionId}", localVarRequestOptions, this.Configuration, cancellationToken).ConfigureAwait(false);

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
        /// <returns>RegionsSearchResponse</returns>
        public RegionsSearchResponse Search(string name, string version = default(string), int operationIndex = 0)
        {
            Sportmonks.Net.Client.ApiResponse<RegionsSearchResponse> localVarResponse = SearchWithHttpInfo(name, version);
            return localVarResponse.Data;
        }

        /// <summary>
        /// Search 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="name">The name you want to search on</param>
        /// <param name="version">The version of the API. (optional)</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of RegionsSearchResponse</returns>
        public Sportmonks.Net.Client.ApiResponse<RegionsSearchResponse> SearchWithHttpInfo(string name, string version = default(string), int operationIndex = 0)
        {
            // verify the required parameter 'name' is set
            if (name == null)
            {
                throw new Sportmonks.Net.Client.ApiException(400, "Missing required parameter 'name' when calling RegionsApi->Search");
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

            localVarRequestOptions.Operation = "RegionsApi.Search";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required
            if (!string.IsNullOrEmpty(this.Configuration.GetApiKeyWithPrefix("Authorization")))
            {
                localVarRequestOptions.HeaderParameters.Add("Authorization", this.Configuration.GetApiKeyWithPrefix("Authorization"));
            }

            // make the HTTP request
            var localVarResponse = this.Client.Get<RegionsSearchResponse>("/{version}/core/regions/search/{name}", localVarRequestOptions, this.Configuration);
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
        /// <returns>Task of RegionsSearchResponse</returns>
        public async System.Threading.Tasks.Task<RegionsSearchResponse> SearchAsync(string name, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            Sportmonks.Net.Client.ApiResponse<RegionsSearchResponse> localVarResponse = await SearchWithHttpInfoAsync(name, version, operationIndex, cancellationToken).ConfigureAwait(false);
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
        /// <returns>Task of ApiResponse (RegionsSearchResponse)</returns>
        public async System.Threading.Tasks.Task<Sportmonks.Net.Client.ApiResponse<RegionsSearchResponse>> SearchWithHttpInfoAsync(string name, string version = default(string), int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            // verify the required parameter 'name' is set
            if (name == null)
            {
                throw new Sportmonks.Net.Client.ApiException(400, "Missing required parameter 'name' when calling RegionsApi->Search");
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

            localVarRequestOptions.Operation = "RegionsApi.Search";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required
            if (!string.IsNullOrEmpty(this.Configuration.GetApiKeyWithPrefix("Authorization")))
            {
                localVarRequestOptions.HeaderParameters.Add("Authorization", this.Configuration.GetApiKeyWithPrefix("Authorization"));
            }

            // make the HTTP request
            var localVarResponse = await this.AsynchronousClient.GetAsync<RegionsSearchResponse>("/{version}/core/regions/search/{name}", localVarRequestOptions, this.Configuration, cancellationToken).ConfigureAwait(false);

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
