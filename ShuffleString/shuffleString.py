# Problem: https://leetcode.com/problems/shuffle-string/
# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"


from typing import List

s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

# s = "aaiougrt"
# indices = [4, 0, 2, 6, 7, 3, 1, 5]


def restoreString(s: str, indices: List[int]) -> str:
    unscrambledWord = ''

    for index in range(len(s)):
        unscrambledWord += s[indices.index(index)]

    return unscrambledWord


print(restoreString(s, indices))
