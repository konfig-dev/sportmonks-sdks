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
    public interface ITypesApiSync : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// All
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>TypesAllResponse</returns>
        TypesAllResponse All(string version, int operationIndex = 0);

        /// <summary>
        /// All
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of TypesAllResponse</returns>
        ApiResponse<TypesAllResponse> AllWithHttpInfo(string version, int operationIndex = 0);
        /// <summary>
        /// By ID
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="typeId">The ID of the type you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>TypesGetByIdResponse</returns>
        TypesGetByIdResponse GetById(string version, int typeId, int operationIndex = 0);

        /// <summary>
        /// By ID
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="typeId">The ID of the type you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of TypesGetByIdResponse</returns>
        ApiResponse<TypesGetByIdResponse> GetByIdWithHttpInfo(string version, int typeId, int operationIndex = 0);
        #endregion Synchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface ITypesApiAsync : IApiAccessor
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
        /// <returns>Task of TypesAllResponse</returns>
        System.Threading.Tasks.Task<TypesAllResponse> AllAsync(string version, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));

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
        /// <returns>Task of ApiResponse (TypesAllResponse)</returns>
        System.Threading.Tasks.Task<ApiResponse<TypesAllResponse>> AllWithHttpInfoAsync(string version, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));
        /// <summary>
        /// By ID
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="typeId">The ID of the type you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of TypesGetByIdResponse</returns>
        System.Threading.Tasks.Task<TypesGetByIdResponse> GetByIdAsync(string version, int typeId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));

        /// <summary>
        /// By ID
        /// </summary>
        /// <remarks>
        /// 
        /// </remarks>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="typeId">The ID of the type you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (TypesGetByIdResponse)</returns>
        System.Threading.Tasks.Task<ApiResponse<TypesGetByIdResponse>> GetByIdWithHttpInfoAsync(string version, int typeId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken));
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public interface ITypesApi : ITypesApiSync, ITypesApiAsync
    {

    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
    public partial class TypesApi : ITypesApi
    {
        private Sportmonks.Net.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="TypesApi"/> class.
        /// </summary>
        /// <returns></returns>
        public TypesApi() : this((string)null)
        {
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="TypesApi"/> class.
        /// </summary>
        /// <returns></returns>
        public TypesApi(string basePath)
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
        /// Initializes a new instance of the <see cref="TypesApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public TypesApi(Sportmonks.Net.Client.Configuration configuration)
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
        /// Initializes a new instance of the <see cref="TypesApi"/> class
        /// using a Configuration object and client instance.
        /// </summary>
        /// <param name="client">The client interface for synchronous API access.</param>
        /// <param name="asyncClient">The client interface for asynchronous API access.</param>
        /// <param name="configuration">The configuration object.</param>
        public TypesApi(Sportmonks.Net.Client.ISynchronousClient client, Sportmonks.Net.Client.IAsynchronousClient asyncClient, Sportmonks.Net.Client.IReadableConfiguration configuration)
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
        /// <returns>TypesAllResponse</returns>
        public TypesAllResponse All(string version, int operationIndex = 0)
        {
            Sportmonks.Net.Client.ApiResponse<TypesAllResponse> localVarResponse = AllWithHttpInfo(version);
            return localVarResponse.Data;
        }

        /// <summary>
        /// All 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of TypesAllResponse</returns>
        public Sportmonks.Net.Client.ApiResponse<TypesAllResponse> AllWithHttpInfo(string version, int operationIndex = 0)
        {
            // verify the required parameter 'version' is set
            if (version == null)
            {
                throw new Sportmonks.Net.Client.ApiException(400, "Missing required parameter 'version' when calling TypesApi->All");
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

            localVarRequestOptions.Operation = "TypesApi.All";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required

            // make the HTTP request
            var localVarResponse = this.Client.Get<TypesAllResponse>("/{version}/core/types", localVarRequestOptions, this.Configuration);
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
        /// <returns>Task of TypesAllResponse</returns>
        public async System.Threading.Tasks.Task<TypesAllResponse> AllAsync(string version, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            Sportmonks.Net.Client.ApiResponse<TypesAllResponse> localVarResponse = await AllWithHttpInfoAsync(version, operationIndex, cancellationToken).ConfigureAwait(false);
            return localVarResponse.Data;
        }

        /// <summary>
        /// All 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (TypesAllResponse)</returns>
        public async System.Threading.Tasks.Task<Sportmonks.Net.Client.ApiResponse<TypesAllResponse>> AllWithHttpInfoAsync(string version, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            // verify the required parameter 'version' is set
            if (version == null)
            {
                throw new Sportmonks.Net.Client.ApiException(400, "Missing required parameter 'version' when calling TypesApi->All");
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

            localVarRequestOptions.Operation = "TypesApi.All";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required

            // make the HTTP request
            var localVarResponse = await this.AsynchronousClient.GetAsync<TypesAllResponse>("/{version}/core/types", localVarRequestOptions, this.Configuration, cancellationToken).ConfigureAwait(false);

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
        /// <param name="typeId">The ID of the type you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>TypesGetByIdResponse</returns>
        public TypesGetByIdResponse GetById(string version, int typeId, int operationIndex = 0)
        {
            Sportmonks.Net.Client.ApiResponse<TypesGetByIdResponse> localVarResponse = GetByIdWithHttpInfo(version, typeId);
            return localVarResponse.Data;
        }

        /// <summary>
        /// By ID 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="typeId">The ID of the type you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <returns>ApiResponse of TypesGetByIdResponse</returns>
        public Sportmonks.Net.Client.ApiResponse<TypesGetByIdResponse> GetByIdWithHttpInfo(string version, int typeId, int operationIndex = 0)
        {
            // verify the required parameter 'version' is set
            if (version == null)
            {
                throw new Sportmonks.Net.Client.ApiException(400, "Missing required parameter 'version' when calling TypesApi->GetById");
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
            localVarRequestOptions.PathParameters.Add("typeId", Sportmonks.Net.Client.ClientUtils.ParameterToString(typeId)); // path parameter

            localVarRequestOptions.Operation = "TypesApi.GetById";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required

            // make the HTTP request
            var localVarResponse = this.Client.Get<TypesGetByIdResponse>("/{version}/core/types/{typeId}", localVarRequestOptions, this.Configuration);
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
        /// <param name="typeId">The ID of the type you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of TypesGetByIdResponse</returns>
        public async System.Threading.Tasks.Task<TypesGetByIdResponse> GetByIdAsync(string version, int typeId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            Sportmonks.Net.Client.ApiResponse<TypesGetByIdResponse> localVarResponse = await GetByIdWithHttpInfoAsync(version, typeId, operationIndex, cancellationToken).ConfigureAwait(false);
            return localVarResponse.Data;
        }

        /// <summary>
        /// By ID 
        /// </summary>
        /// <exception cref="Sportmonks.Net.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="version">The version of the API.</param>
        /// <param name="typeId">The ID of the type you want to retrieve</param>
        /// <param name="operationIndex">Index associated with the operation.</param>
        /// <param name="cancellationToken">Cancellation Token to cancel the request.</param>
        /// <returns>Task of ApiResponse (TypesGetByIdResponse)</returns>
        public async System.Threading.Tasks.Task<Sportmonks.Net.Client.ApiResponse<TypesGetByIdResponse>> GetByIdWithHttpInfoAsync(string version, int typeId, int operationIndex = 0, System.Threading.CancellationToken cancellationToken = default(System.Threading.CancellationToken))
        {
            // verify the required parameter 'version' is set
            if (version == null)
            {
                throw new Sportmonks.Net.Client.ApiException(400, "Missing required parameter 'version' when calling TypesApi->GetById");
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
            localVarRequestOptions.PathParameters.Add("typeId", Sportmonks.Net.Client.ClientUtils.ParameterToString(typeId)); // path parameter

            localVarRequestOptions.Operation = "TypesApi.GetById";
            localVarRequestOptions.OperationIndex = operationIndex;

            // authentication (apikeyAuth) required

            // make the HTTP request
            var localVarResponse = await this.AsynchronousClient.GetAsync<TypesGetByIdResponse>("/{version}/core/types/{typeId}", localVarRequestOptions, this.Configuration, cancellationToken).ConfigureAwait(false);

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