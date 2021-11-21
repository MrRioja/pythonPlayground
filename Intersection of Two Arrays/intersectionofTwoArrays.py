# Problem: https://leetcode.com/problems/intersection-of-two-arrays/
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

from typing import List


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    intersectionNums = []

    for num1 in nums1:
        for num2 in nums2:
            if num1 == num2 and num1 not in intersectionNums:
                intersectionNums.append(num1)

    return intersectionNums


print(intersection(nums1, nums2))
