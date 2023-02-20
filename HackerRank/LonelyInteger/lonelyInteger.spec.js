import { describe, expect, it } from "vitest";

import { lonelyInteger } from "./lonelyInteger";

describe("Lonely integer", () => {
  it.each([{ arr: [1, 2, 3, 4, 3, 2, 1], expected: 4 }])(
    "should be able to find the lonely integer in an array",
    ({ arr, expected }) => {
      expect(lonelyInteger(arr)).toEqual(expected);
    }
  );
});
