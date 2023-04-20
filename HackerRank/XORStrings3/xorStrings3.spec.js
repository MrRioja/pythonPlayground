import { describe, expect, it } from "vitest";

import { stringsXOR } from "./xorStrings3";

describe("XOR Strings 3", () => {
  it.each([
    { firstString: "10101", secondString: "00101", expected: "10000" },
    { firstString: "10101", secondString: "01010", expected: "11111" },
  ])(
    "should be able to find the XOR of the two strings",
    ({ firstString, secondString, expected }) => {
      expect(stringsXOR(firstString, secondString)).toEqual(expected);
    }
  );
});
