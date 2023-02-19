import { describe, expect, it } from "vitest";

import { birthdayCakeCandles } from "./birthdayCakeCandles";

describe("Birthday Cakes Candles", () => {
  it.each([
    { candles: [4, 5, 1, 9, 10, 3, 30, 4, 4, 7, 4], expected: 1 },
    { candles: [3, 2, 1, 3], expected: 2 },
  ])(
    "should be able to get how many candles are tallest",
    ({ candles, expected }) => {
      expect(birthdayCakeCandles(candles)).toEqual(expected);
    }
  );
});
