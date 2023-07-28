import { describe, expect, it } from "vitest";

import { pageCount } from "./drawingBook";

describe("Drawing Book", () => {
  it.each([
    { n: 6, p: 2, expected: 1 },
    { n: 5, p: 4, expected: 0 },
    { n: 6, p: 5, expected: 1 },
  ])(
    "should be able to find the minimum number of pages to turn",
    ({ n, p, expected }) => {
      expect(pageCount(n, p)).toEqual(expected);
    }
  );
});
