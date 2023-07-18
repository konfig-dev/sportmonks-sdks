import { Sportmonks } from "./index";

describe("sportmonks", () => {
  it("initialize client", async () => {
    const sportmonks = new Sportmonks();
    const cities = await sportmonks.cities.all();
  });
});
