import { describe, expect, it } from "vitest";

import { findZigZagSequence } from "./zigZagSequence";

describe("ZigZagSequence", () => {
  it.each([
    { a: [2, 3, 5, 1, 4], n: 5, expected: "1 2 5 4 3" },
    { a: [1, 2, 3, 4, 5, 6, 7], n: 7, expected: "1 2 3 7 6 5 4" },
    {
      n: 11,
      expected: "1 2 3 4 5 11 10 9 8 7 6",
      a: [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    },
  ])(
    "should be able to find the lexicographically smallest zig zag sequence of the given array",
    ({ a, n, expected }) => {
      expect(findZigZagSequence(a, n)).toEqual(expected);
    }
  );
});
