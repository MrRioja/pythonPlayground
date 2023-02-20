import { describe, expect, it } from "vitest";

import { matchingStrings } from "./sparseArrays";

describe("SparseArrays", () => {
  it.each([
    {
      queries: ["abcde", "sdaklfj", "asdjf", "na", "basdn"],
      strings: [
        "13",
        "abcde",
        "sdaklfj",
        "asdjf",
        "na",
        "basdn",
        "sdaklfj",
        "asdjf",
        "na",
        "asdjf",
        "na",
        "basdn",
        "sdaklfj",
        "asdjf",
        "5",
      ],
      expected: [1, 3, 4, 3, 2],
    },
    {
      queries: ["ab", "abc", "ab"],
      strings: ["ab", "ab", "abc"],
      expected: [2, 1, 2],
    },
  ])(
    "should be able to determine how many times each query string occurs in the list of input strings",
    ({ strings, queries, expected }) => {
      expect(matchingStrings(strings, queries)).toEqual(expected);
    }
  );
});
