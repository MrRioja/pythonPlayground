import { describe, expect, it } from "vitest";

import { migratoryBirds } from "./MigratoryBirds";

describe("MigratoryBirds", () => {
  it.each([
    { arr: [1, 1, 2, 2, 3], expected: 1 },
    { arr: [1, 4, 4, 4, 5, 3], expected: 4 },
    { arr: [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4], expected: 3 },
  ])(
    "should be able to find the smallest number most often",
    ({ arr, expected }) => {
      expect(migratoryBirds(arr)).toEqual(expected);
    }
  );
});
