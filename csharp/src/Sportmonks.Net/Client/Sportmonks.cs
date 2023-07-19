using Sportmonks.Net.Api;

namespace Sportmonks.Net.Client
{
    /// <summary>
    ///  SDK client
    /// </summary>
    public class Sportmonks
    {
        /// <summary>
        /// API instance
        /// </summary>
        public CitiesApi Cities { get; private set; }

        /// <summary>
        /// API instance
        /// </summary>
        public ContinentsApi Continents { get; private set; }

        /// <summary>
        /// API instance
        /// </summary>
        public CountriesApi Countries { get; private set; }

        /// <summary>
        /// API instance
        /// </summary>
        public MyApi My { get; private set; }

        /// <summary>
        /// API instance
        /// </summary>
        public OddsApi Odds { get; private set; }

        /// <summary>
        /// API instance
        /// </summary>
        public RegionsApi Regions { get; private set; }

        /// <summary>
        /// API instance
        /// </summary>
        public SportApi Sport { get; private set; }

        /// <summary>
        /// API instance
        /// </summary>
        public TypesApi Types { get; private set; }

        /// <summary>
        /// Configuration instance
        /// </summary>
        public readonly Configuration Configuration;


        /// <summary>
        /// Constructor
        /// </summary>
        public Sportmonks()
        {
            Configuration = new Configuration();
            init();
        }

        private void init()
        {
            Cities = new CitiesApi(Configuration);
            Continents = new ContinentsApi(Configuration);
            Countries = new CountriesApi(Configuration);
            My = new MyApi(Configuration);
            Odds = new OddsApi(Configuration);
            Regions = new RegionsApi(Configuration);
            Sport = new SportApi(Configuration);
            Types = new TypesApi(Configuration);
        }

        /// <summary>
        /// Setter for API Key
        /// </summary>
        public Sportmonks SetApiKey(string apiKey)
        {
            Configuration.ApiKey["Authorization"] = apiKey;
            init();
            return this;
        }

        /// <summary>
        /// Setter for "version" client state
        /// </summary>
        public Sportmonks SetVersion(string version)
        {
            Configuration.Version = version;
            init();
            return this;
        }

        /// <summary>
        /// Setter for "sport" client state
        /// </summary>
        public Sportmonks SetSport(string sport)
        {
            Configuration.Sport = sport;
            init();
            return this;
        }

    }

}
