import { describe, expect, it } from "vitest";

import { birthday } from "./subarrayDivision2";

describe("Sub Array Division 2", () => {
  it.each([
    { arr: [4], d: 4, m: 1, expected: 1 },
    { arr: [1, 2, 1, 3, 2], d: 3, m: 2, expected: 2 },
    { arr: [1, 1, 1, 1, 1, 1], d: 3, m: 2, expected: 0 },
  ])(
    "should be able to determine how many ways the chocolate can be divide",
    ({ arr, d, m, expected }) => {
      expect(birthday(arr, d, m)).toEqual(expected);
    }
  );
});
