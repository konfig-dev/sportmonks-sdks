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
    ///  Class for testing RegionsApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Konfig (https://konfigthis.com).
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    public class RegionsApiTests : IDisposable
    {
        private RegionsApi instance;

        public RegionsApiTests()
        {
            instance = new RegionsApi();
        }

        public void Dispose()
        {
            // Cleanup when everything is done.
        }

        /// <summary>
        /// Test an instance of RegionsApi
        /// </summary>
        [Fact]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsType' RegionsApi
            //Assert.IsType<RegionsApi>(instance);
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
            //Assert.IsType<RegionsAllResponse>(response);
        }

        /// <summary>
        /// Test GetById
        /// </summary>
        [Fact]
        public void GetByIdTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string version = null;
            //int regionId = null;
            //var response = instance.GetById(version, regionId);
            //Assert.IsType<RegionsGetByIdResponse>(response);
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
            //Assert.IsType<RegionsSearchResponse>(response);
        }
    }
}
