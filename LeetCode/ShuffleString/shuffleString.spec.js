import { describe, expect, it } from "vitest";

import { restoreString } from "./shuffleString";

describe("Shuffle String", () => {
  it.each([
    { s: "codeleet", indices: [4, 5, 6, 7, 0, 2, 1, 3], expected: "leetcode" },
  ])(
    "should be able to return the shuffled string in the correct order",
    ({ s, indices, expected }) => {
      expect(restoreString(s, indices)).toEqual(expected);
    }
  );
});
