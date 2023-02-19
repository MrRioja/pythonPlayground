import { describe, expect, it } from "vitest";

import { breakingRecords } from "./breakingTheRecords";

describe("Breaking the records", () => {
  it.each([
    { scores: [10, 5, 20, 20, 4, 5, 2, 25, 1], expected: [2, 4] },
    { scores: [3, 4, 21, 36, 10, 28, 35, 5, 24, 42], expected: [4, 0] },
  ])(
    "should be able to determine the number of times Maria breaks her records for most and least points scored during the season",
    ({ scores, expected }) => {
      expect(breakingRecords(scores)).toEqual(expected);
    }
  );
});
