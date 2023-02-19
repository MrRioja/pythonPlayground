import { describe, expect, it } from "vitest";

import { camelCase } from "./camelCase";

describe("Camel Case", () => {
  it.each([
    { string: "oneTwoThree", expected: 3 },
    { string: "saveChangesInTheEditor", expected: 5 },
  ])("should be able to count words in a string", ({ string, expected }) => {
    expect(camelCase(string)).toEqual(expected);
  });
});
