// Problem: https://leetcode.com/problems/intersection-of-two-arrays/
// Given two integer arrays nums1 and nums2, return an array of their intersection.
// Each element in the result must be unique and you may return the result in any order.
// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2]

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
function intersection(nums1, nums2) {
  let intersectionNums = [];

  nums1.forEach((num1) => {
    nums2.forEach((num2) => {
      if (num1 == num2 && !intersectionNums.includes(num1)) {
        intersectionNums.push(num1);
      }
    });
  });

  return intersectionNums;
}

const nums1 = [4, 9, 5];
const nums2 = [9, 4, 9, 8, 4];

console.log(intersection(nums1, nums2));
