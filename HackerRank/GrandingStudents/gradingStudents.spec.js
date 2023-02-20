import { describe, expect, it } from "vitest";

import { gradingStudents } from "./gradingStudents";

describe("Grading students", () => {
  it.each([
    {
      grades: [98, 84, 99, 29, 57, 100],
      expected: [100, 85, 100, 29, 57, 100],
    },
  ])("should be able to round grades", ({ grades, expected }) => {
    expect(gradingStudents(grades)).toEqual(expected);
  });
});
