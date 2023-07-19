import { Sportmonks } from "./index";

describe("sportmonks", () => {
  it("initialize client", async () => {
    const sportmonks = new Sportmonks({
      apiKey: process.env.SPORTMONKS_API_TOKEN,
      sport: "football",
      version: "v3",
    });

    const cities = await sportmonks.cities.all();
    console.log(cities.data);

    const coaches = await sportmonks.sport.coachesAll();
    console.log(coaches.data);

    const teams = await sportmonks.sport.teamsAll();
    const firstTeam = teams.data.data?.[0];
    const firstTeamId = firstTeam?.id;
    if (firstTeam === undefined || firstTeamId === undefined)
      throw Error("Could not find team ID");

    console.log(firstTeam);

    const squads = await sportmonks.sport.squadsByTeamId({
      teamId: firstTeamId,
    });
    console.log(squads.data);
  });
  it("seasons by team id", async () => {
    const sportmonks = new Sportmonks({
      // Defining the base path is optional and defaults to https://api.sportmonks.com
      // basePath: "https://api.sportmonks.com",
      version: "v3",
      sport: "football",
      apiKey: process.env.SPORTMONKS_API_TOKEN,
    });

    const teams = await sportmonks.sport.teamsAll();
    const firstTeam = teams.data.data?.[0];
    const firstTeamId = firstTeam?.id;
    if (firstTeam === undefined || firstTeamId === undefined)
      throw Error("Could not find team ID");

    const seasons = await sportmonks.sport.seasonsByTeamId({
      teamId: firstTeamId,
    });

    console.log(seasons.data);
  });
});
