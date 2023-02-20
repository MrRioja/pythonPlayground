import { describe, expect, it } from "vitest";

import { kangaroo } from "./numberLineJumps";

describe("Number line jumps", () => {
  it.each([
    { x1: 0, v1: 2, x2: 5, v2: 3, expected: "NO" },
    { x1: 21, v1: 6, x2: 47, v2: 3, expected: "NO" },
    { x1: 0, v1: 3, x2: 4, v2: 2, expected: "YES" },
    { x1: 4523, v1: 8092, x2: 9419, v2: 8076, expected: "YES" },
  ])(
    "should be able to predict whether two kangaroos will be in the same place at the same time",
    ({ x1, v1, x2, v2, expected }) => {
      expect(kangaroo(x1, v1, x2, v2)).toEqual(expected);
    }
  );
});
