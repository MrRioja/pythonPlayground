import { describe, expect, it } from "vitest";

import { getDiagonalDifference } from "./diagonalDifference";

describe("Diagonal difference", () => {
  it.each([
    {
      arr: [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9],
      ],
      expected: 2,
    },
  ])(
    "should be able to get a diagonal difference of an array",
    ({ arr, expected }) => {
      expect(getDiagonalDifference(arr)).toEqual(expected);
    }
  );
});
