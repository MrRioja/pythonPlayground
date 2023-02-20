import { describe, expect, it } from "vitest";

import { marsExploration } from "./marsExploration";

describe("MarsExploration", () => {
  it.each([
    { s: "SOSTOT", expected: 2 },
    { s: "SOSSPSSQSSOR", expected: 3 },
  ])(
    "should be able to find how many characters were changed in transit",
    ({ s, expected }) => {
      expect(marsExploration(s)).toEqual(expected);
    }
  );
});
