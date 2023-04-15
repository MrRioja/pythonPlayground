import { describe, expect, it } from "vitest";

import { sockMerchant } from "./salesByMatch";

describe("SalesByMatch", () => {
  it.each([
    { length: 7, array: [1, 2, 1, 2, 1, 3, 2], expected: 2 },
    { length: 9, array: [10, 20, 20, 10, 10, 30, 50, 10, 20], expected: 3 },
  ])(
    "should be able to determine how many pairs of socks with matching colors there are",
    ({ length, array, expected }) => {
      expect(sockMerchant(length, array)).toEqual(expected);
    }
  );
});
