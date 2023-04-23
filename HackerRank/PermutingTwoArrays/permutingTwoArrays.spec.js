import { describe, expect, it } from "vitest";

import { twoArrays } from "./permutingTwoArrays";

describe("PermutingTwoArrays", () => {
  it.each([
    { k: 10, a: [2, 1, 3], b: [7, 8, 9], expected: "YES" },
    { k: 5, a: [1, 2, 2, 1], b: [3, 3, 3, 4], expected: "NO" },
    { k: 10, a: [7, 6, 8, 4, 2], b: [5, 2, 6, 3, 1], expected: "NO" },
  ])(
    "should be able to find some permutation satisfying the relation exists",
    ({ k, a, b, expected }) => {
      expect(twoArrays(k, a, b)).toEqual(expected);
    }
  );
});
