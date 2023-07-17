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
    ///  Class for testing MyApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Konfig (https://konfigthis.com).
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    public class MyApiTests : IDisposable
    {
        private MyApi instance;

        public MyApiTests()
        {
            instance = new MyApi();
        }

        public void Dispose()
        {
            // Cleanup when everything is done.
        }

        /// <summary>
        /// Test an instance of MyApi
        /// </summary>
        [Fact]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsType' MyApi
            //Assert.IsType<MyApi>(instance);
        }

        /// <summary>
        /// Test Enrichments
        /// </summary>
        [Fact]
        public void EnrichmentsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string version = null;
            //var response = instance.Enrichments(version);
            //Assert.IsType<MyEnrichmentsResponse>(response);
        }

        /// <summary>
        /// Test Leagues
        /// </summary>
        [Fact]
        public void LeaguesTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string version = null;
            //var response = instance.Leagues(version);
            //Assert.IsType<MyLeaguesResponse>(response);
        }

        /// <summary>
        /// Test Resources
        /// </summary>
        [Fact]
        public void ResourcesTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string version = null;
            //var response = instance.Resources(version);
            //Assert.IsType<MyResourcesResponse>(response);
        }
    }
}