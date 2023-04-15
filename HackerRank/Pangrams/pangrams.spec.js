import { describe, expect, it } from "vitest";

import { pangrams } from "./pangrams";

describe("Pangrams", () => {
  it.each([
    {
      sentence: "We promptly judged antique ivory buckles for the next prize",
      expected: "pangram",
    },
    {
      sentence: "We promptly judged antique ivory buckles for the prize",
      expected: "not pangram",
    },
  ])(
    "should be able to determine if a sentence is a pangram in the English alphabet",
    ({ sentence, expected }) => {
      expect(pangrams(sentence)).toEqual(expected);
    }
  );
});
