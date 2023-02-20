import { describe, it, expect } from "vitest";

import { flippingBits } from "./flippingBits";

describe("Flipping bits", () => {
  it.each([
    { num: 0, expected: 4294967295 },
    { num: 1, expected: 4294967294 },
    { num: 9, expected: 4294967286 },
    { num: 2147483647, expected: 2147483648 },
  ])("should be able to flip bits", ({ num, expected }) => {
    expect(flippingBits(num)).toEqual(expected);
  });
});
