import { describe, expect, it } from "vitest";

import { timeConversion } from "./timeConversion";

describe("TimeConversion", () => {
  it.each([
    { hour: "07:05:45PM", expected: "19:05:45" },
    { hour: "12:37:58AM", expected: "00:37:58" },
  ])(
    "should be able to convert an hour AM/PM to military (24-hour) time",
    ({ hour, expected }) => {
      expect(timeConversion(hour)).toEqual(expected);
    }
  );
});
