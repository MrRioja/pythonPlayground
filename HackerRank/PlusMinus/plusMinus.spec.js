import { describe, expect, it } from "vitest";

import { plusMinus } from "./plusMinus";

describe("PlusMinus", () => {
  it.each([
    {
      nums: [-4, 3, -9, 0, 4, 1],
      expected: ["0.500000", "0.333333", "0.166667"],
    },
  ])(
    "should be able to calculate the ratios of its elements that are positive, negative, and zero",
    ({ nums, expected }) => {
      expect(plusMinus(nums)).toEqual(expected);
    }
  );
});
