import { describe, expect, it } from "vitest";

import { intersection } from "./intersectionofTwoArrays";

describe("Intersection of two arrays", () => {
  it.each([{ nums1: [4, 9, 5], nums2: [9, 4, 9, 8, 4], expected: [4, 9] }])(
    "should be able to find the intersection between two arrays",
    ({ nums1, nums2, expected }) => {
      expect(intersection(nums1, nums2)).toEqual(expected);
    }
  );
});
