# Problem: https://leetcode.com/problems/shuffle-string/
# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"


from typing import List


def restore_string(s: str, indices: List[int]) -> str:
    unscrambled_word = ''

    for index in range(len(s)):
        unscrambled_word += s[indices.index(index)]

    return unscrambled_word


s = "aaiougrt"
indices = [4, 0, 2, 6, 7, 3, 1, 5]

print(restore_string(s, indices))
