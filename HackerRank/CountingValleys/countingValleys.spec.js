import { describe, expect, it } from "vitest";

import { countingValleys } from "./countingValleys";

describe("Counting Valleys", () => {
  it.each([
    { steps: 0, path: "UDDDUDUU", expected: 1 },
    {
      steps: 0,
      path: "DDUUDDUDUUUD",
      expected: 2,
    },
  ])(
    "should be able to count the number of valleys traversed",
    ({ steps, path, expected }) => {
      expect(countingValleys(steps, path)).toEqual(expected);
    }
  );
});
