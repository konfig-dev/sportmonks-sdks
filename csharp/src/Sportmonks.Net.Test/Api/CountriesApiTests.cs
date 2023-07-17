/*
 * SportMonks
 *
 * Surpass the competition with superior sports data
 *
 * The version of the OpenAPI document: 1.0.0
 * Generated by: https://konfigthis.com
 */

using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using Xunit;

using Sportmonks.Net.Client;
using Sportmonks.Net.Api;
// uncomment below to import models
//using Sportmonks.Net.Model;

namespace Sportmonks.Net.Test.Api
{
    /// <summary>
    ///  Class for testing CountriesApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Konfig (https://konfigthis.com).
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    public class CountriesApiTests : IDisposable
    {
        private CountriesApi instance;

        public CountriesApiTests()
        {
            instance = new CountriesApi();
        }

        public void Dispose()
        {
            // Cleanup when everything is done.
        }

        /// <summary>
        /// Test an instance of CountriesApi
        /// </summary>
        [Fact]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsType' CountriesApi
            //Assert.IsType<CountriesApi>(instance);
        }

        /// <summary>
        /// Test All
        /// </summary>
        [Fact]
        public void AllTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string version = null;
            //var response = instance.All(version);
            //Assert.IsType<CountriesAllResponse>(response);
        }

        /// <summary>
        /// Test GetById
        /// </summary>
        [Fact]
        public void GetByIdTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string version = null;
            //int countryId = null;
            //var response = instance.GetById(version, countryId);
            //Assert.IsType<CountriesGetByIdResponse>(response);
        }

        /// <summary>
        /// Test Search
        /// </summary>
        [Fact]
        public void SearchTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string version = null;
            //string name = null;
            //var response = instance.Search(version, name);
            //Assert.IsType<CountriesSearchResponse>(response);
        }
    }
}