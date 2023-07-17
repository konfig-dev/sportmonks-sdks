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
    public interface IContinentsApiSync : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// All
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ContinentsAllResponse</returns>
        ContinentsAllResponse All(string version, int operationIndex = 0);

        /// <summary>
        /// All
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of ContinentsAllResponse</returns>
        ApiResponse<ContinentsAllResponse> AllWithHttpInfo(string version, int operationIndex = 0);
        /// <summary>
        /// By ID
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="continentId">The ID of the continent you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ContinentsGetByIdResponse</returns>
        ContinentsGetByIdResponse GetById(string version, int continentId, int operationIndex = 0);

        /// <summary>
        /// By ID
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="continentId">The ID of the continent you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of ContinentsGetByIdResponse</returns>
        ApiResponse<ContinentsGetByIdResponse> GetByIdWithHttpInfo(string version, int continentId, int operationIndex = 0);
        #endregion Synchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface IContinentsApiAsync : IApiAccessor
    {
        #region Asynchronous Operations
        /// <summary>
        /// All
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ContinentsAllResponse</returns>
        System.Threading.Tasks.Task<ContinentsAllResponse> AllAsync(string version, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));

        /// <summary>
        /// All
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (ContinentsAllResponse)</returns>
        System.Threading.Tasks.Task<ApiResponse<ContinentsAllResponse>> AllWithHttpInfoAsync(string version, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));
        /// <summary>
        /// By ID
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="continentId">The ID of the continent you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ContinentsGetByIdResponse</returns>
        System.Threading.Tasks.Task<ContinentsGetByIdResponse> GetByIdAsync(string version, int continentId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));

        /// <summary>
        /// By ID
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="continentId">The ID of the continent you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (ContinentsGetByIdResponse)</returns>
        System.Threading.Tasks.Task<ApiResponse<ContinentsGetByIdResponse>> GetByIdWithHttpInfoAsync(string version, int continentId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface IContinentsApi : IContinentsApiSync, IContinentsApiAsync
    {

    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public partial class ContinentsApi : IContinentsApi
    {
        private Sportmonks.Net.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="ContinentsApi"/> class.
        /// </summary>
        /// <returns></returns>
        public ContinentsApi() : this((string)null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="ContinentsApi"/> class.
        /// </summary>
        /// <returns></returns>
        public ContinentsApi(string basePath)
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
        /// Initializes a new instance of the <see cref="ContinentsApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public ContinentsApi(Sportmonks.Net.Client.Configuration configuration)
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
        /// Initializes a new instance of the <see cref="ContinentsApi"/> class
        /// using a Configuration object and client instance.
        /// </summary>
        /// <param name="client">The client interface for synchronous API access.</param>
        /// <param name="asyncClient">The client interface for asynchronous API access.</param>
        /// <param name="configuration">The configuration object.</param>
        public ContinentsApi(Sportmonks.Net.Client.ISynchronousClient client, Sportmonks.Net.Client.IAsynchronousClient asyncClient, Sportmonks.Net.Client.IReadableConfiguration configuration)
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
        /// <param name="version">The version of the API.</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ContinentsAllResponse</returns>
        public ContinentsAllResponse All(string version, int operationIndex = 0)
        {
            Sportmonks.Net.Client.ApiResponse<ContinentsAllResponse> localVarResponse = AllWithHttpInfo(version);
            return localVarResponse.Data;
        }

        /// <summary>
        /// All 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of ContinentsAllResponse</returns>
        public Sportmonks.Net.Client.ApiResponse<ContinentsAllResponse> AllWithHttpInfo(string version, int operationIndex = 0)
        {
            // verify the required parameter 'version' is set
            if (version == null)
            {
                throw new Sportmonks.Net.Client.ApiException(400, "Missing required parameter 'version' when calling ContinentsApi->All");
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

            localVarRequestOptions.PathParameters.Add("version", Sportmonks.Net.Client.ClientUtils.ParameterToString(version)); // path parameter

            localVarRequestOptions.Operation = "ContinentsApi.All";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required

            // make the HTTP request
            var localVarResponse = this.Client.Get<ContinentsAllResponse>("/{version}/core/continents", localVarRequestOptions, this.Configuration);
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
        /// <param name="version">The version of the API.</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ContinentsAllResponse</returns>
        public async System.Threading.Tasks.Task<ContinentsAllResponse> AllAsync(string version, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            Sportmonks.Net.Client.ApiResponse<ContinentsAllResponse> localVarResponse = await AllWithHttpInfoAsync(version, operationIndex, cancellationToken).ConfigureAwait(false);
            return localVarResponse.Data;
        }

        /// <summary>
        /// All 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (ContinentsAllResponse)</returns>
        public async System.Threading.Tasks.Task<Sportmonks.Net.Client.ApiResponse<ContinentsAllResponse>> AllWithHttpInfoAsync(string version, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            // verify the required parameter 'version' is set
            if (version == null)
            {
                throw new Sportmonks.Net.Client.ApiException(400, "Missing required parameter 'version' when calling ContinentsApi->All");
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

            localVarRequestOptions.PathParameters.Add("version", Sportmonks.Net.Client.ClientUtils.ParameterToString(version)); // path parameter

            localVarRequestOptions.Operation = "ContinentsApi.All";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required

            // make the HTTP request
            var localVarResponse = await this.AsynchronousClient.GetAsync<ContinentsAllResponse>("/{version}/core/continents", localVarRequestOptions, this.Configuration, cancellationToken).ConfigureAwait(false);

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
        /// <param name="version">The version of the API.</param>
        /// <param name="continentId">The ID of the continent you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ContinentsGetByIdResponse</returns>
        public ContinentsGetByIdResponse GetById(string version, int continentId, int operationIndex = 0)
        {
            Sportmonks.Net.Client.ApiResponse<ContinentsGetByIdResponse> localVarResponse = GetByIdWithHttpInfo(version, continentId);
            return localVarResponse.Data;
        }

        /// <summary>
        /// By ID 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="continentId">The ID of the continent you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of ContinentsGetByIdResponse</returns>
        public Sportmonks.Net.Client.ApiResponse<ContinentsGetByIdResponse> GetByIdWithHttpInfo(string version, int continentId, int operationIndex = 0)
        {
            // verify the required parameter 'version' is set
            if (version == null)
            {
                throw new Sportmonks.Net.Client.ApiException(400, "Missing required parameter 'version' when calling ContinentsApi->GetById");
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

            localVarRequestOptions.PathParameters.Add("version", Sportmonks.Net.Client.ClientUtils.ParameterToString(version)); // path parameter
            localVarRequestOptions.PathParameters.Add("continentId", Sportmonks.Net.Client.ClientUtils.ParameterToString(continentId)); // path parameter

            localVarRequestOptions.Operation = "ContinentsApi.GetById";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required

            // make the HTTP request
            var localVarResponse = this.Client.Get<ContinentsGetByIdResponse>("/{version}/core/continents/{continentId}", localVarRequestOptions, this.Configuration);
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
        /// <param name="version">The version of the API.</param>
        /// <param name="continentId">The ID of the continent you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ContinentsGetByIdResponse</returns>
        public async System.Threading.Tasks.Task<ContinentsGetByIdResponse> GetByIdAsync(string version, int continentId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            Sportmonks.Net.Client.ApiResponse<ContinentsGetByIdResponse> localVarResponse = await GetByIdWithHttpInfoAsync(version, continentId, operationIndex, cancellationToken).ConfigureAwait(false);
            return localVarResponse.Data;
        }

        /// <summary>
        /// By ID 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="continentId">The ID of the continent you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (ContinentsGetByIdResponse)</returns>
        public async System.Threading.Tasks.Task<Sportmonks.Net.Client.ApiResponse<ContinentsGetByIdResponse>> GetByIdWithHttpInfoAsync(string version, int continentId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            // verify the required parameter 'version' is set
            if (version == null)
            {
                throw new Sportmonks.Net.Client.ApiException(400, "Missing required parameter 'version' when calling ContinentsApi->GetById");
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

            localVarRequestOptions.PathParameters.Add("version", Sportmonks.Net.Client.ClientUtils.ParameterToString(version)); // path parameter
            localVarRequestOptions.PathParameters.Add("continentId", Sportmonks.Net.Client.ClientUtils.ParameterToString(continentId)); // path parameter

            localVarRequestOptions.Operation = "ContinentsApi.GetById";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required

            // make the HTTP request
            var localVarResponse = await this.AsynchronousClient.GetAsync<ContinentsGetByIdResponse>("/{version}/core/continents/{continentId}", localVarRequestOptions, this.Configuration, cancellationToken).ConfigureAwait(false);

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

    }
}
