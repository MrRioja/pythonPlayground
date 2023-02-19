import { describe, expect, it } from "vitest";

import { divisibleSumPairs } from "./divisibleSumPairs";

describe("Divisible sum pairs", () => {
  it.each([{ n: 6, k: 3, arr: [1, 3, 2, 6, 1, 2], expected: 4 }])(
    "should be able to find pairs that satisfy the criteria",
    ({ n, k, arr, expected }) => {
      expect(divisibleSumPairs(n, k, arr)).toEqual(expected);
    }
  );
});
