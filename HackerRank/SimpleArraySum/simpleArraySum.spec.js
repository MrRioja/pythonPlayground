import { describe, expect, it } from "vitest";

import { sumArrayElements } from "./simpleArraySum";

describe("Simple array sum", () => {
  it.each([
    {
      vector: [338, 65, 713, 595, 428, 610, 728, 573, 871, 868],
      expected: 5789,
    },
  ])(
    "should be able to find the sum of elements in an array",
    ({ vector, expected }) => {
      expect(sumArrayElements(vector)).toEqual(expected);
    }
  );
});
