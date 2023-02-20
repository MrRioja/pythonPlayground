import { describe, expect, it } from "vitest";

import { swapCase } from "./swapCase";

describe("SwapCase", () => {
  it.each([{ s: "Www.HackerRank.com", expected: "wWW.hACKERrANK.COM" }])(
    "should be able to convert all lowercase letters to uppercase letters and vice versa",
    ({ s, expected }) => {
      expect(swapCase(s)).toEqual(expected);
    }
  );
});
