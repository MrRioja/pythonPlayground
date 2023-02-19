import { describe, expect, it } from "vitest";

import { numJewelsInStones } from "./jewelsAndStones";

describe("Jewels and Stones", () => {
  it.each([
    { jewels: "z", stones: "ZZ", expected: 0 },
    { jewels: "aA", stones: "aAAbbbb", expected: 3 },
  ])(
    "should be able to find how many of the stones you have are also jewels",
    ({ jewels, stones, expected }) => {
      expect(numJewelsInStones(jewels, stones)).toEqual(expected);
    }
  );
});
