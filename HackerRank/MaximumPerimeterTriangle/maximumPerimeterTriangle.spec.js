import { describe, expect, it } from "vitest";

import { maximumPerimeterTriangle } from "./maximumPerimeterTriangle";

describe("Maximum Perimeter Triangle", () => {
  it.each([
    { sticks: [1, 2, 3], expected: [-1] },
    { sticks: [1, 1, 1, 3, 3], expected: [1, 3, 3] },
    { sticks: [1, 1, 1, 2, 3, 5], expected: [1, 1, 1] },
  ])(
    "should be able to construct a non-degenerate triangle with the maximum possible perimeter",
    ({ sticks, expected }) => {
      expect(maximumPerimeterTriangle(sticks)).toEqual(expected);
    }
  );
});
