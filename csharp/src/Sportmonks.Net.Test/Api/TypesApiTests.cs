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
    ///  Class for testing TypesApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Konfig (https://konfigthis.com).
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    public class TypesApiTests : IDisposable
    {
        private TypesApi instance;

        public TypesApiTests()
        {
            instance = new TypesApi();
        }

        public void Dispose()
        {
            // Cleanup when everything is done.
        }

        /// <summary>
        /// Test an instance of TypesApi
        /// </summary>
        [Fact]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsType' TypesApi
            //Assert.IsType<TypesApi>(instance);
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
            //Assert.IsType<TypesAllResponse>(response);
        }

        /// <summary>
        /// Test GetById
        /// </summary>
        [Fact]
        public void GetByIdTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string version = null;
            //int typeId = null;
            //var response = instance.GetById(version, typeId);
            //Assert.IsType<TypesGetByIdResponse>(response);
        }
    }
}
