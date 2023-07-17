/*
 * SportMonks
 *
 * Surpass the competition with superior sports data
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://konfigthis.com
 */


using System;

namespace Sportmonks.Net.Client
{
    /// <summary>
    /// Generic ClientException that occurs even in case of successful response
    /// </summary>
    public class ClientException : Exception
    {

        /// <summary>
        /// Response object that caused the exception
        /// </summary>
        public IApiResponse Response { get; set; }

        /// <summary>
        /// Initializes a new instance of the <see cref="ClientException"/> class.
        /// </summary>
        public ClientException(IApiResponse response, Exception innerException) : base("Error while deserialization response", innerException)
        {
            this.Response = response;
        }
    }

}
