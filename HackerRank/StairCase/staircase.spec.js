import { describe, expect, it } from "vitest";

import { staircase } from "./staircase";

describe("Stair case", () => {
  it.each([
    { num: 3, expected: "  #\n ##\n###" },
    { num: 4, expected: "   #\n  ##\n ###\n####" },
  ])("should be able to build a ladder of size N", ({ num, expected }) => {
    expect(staircase(num)).toEqual(expected);
  });
});
