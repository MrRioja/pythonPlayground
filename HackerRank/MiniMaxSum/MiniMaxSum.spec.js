import { describe, expect, it } from "vitest";

import { miniMaxSum } from "./MiniMaxSum";

describe("MiniMaxSum", () => {
  it.each([
    { arr: [1, 3, 5, 7, 9], expected: [16, 24] },
    { arr: [7, 69, 2, 221, 8974], expected: [299, 9271] },
  ])("should be able ", ({ arr, expected }) => {
    expect(miniMaxSum(arr)).toEqual(expected);
  });
});
