# Problem: https://leetcode.com/problems/jewels-and-stones/
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
# Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3


def num_jewels_in_stones(jewels: str, stones: str) -> int:
    num_jewels = 0
    jewels = set(jewels)

    for stone in stones:
        if stone in jewels:
            num_jewels += 1

    return num_jewels


jewels = "z"
stones = "ZZ"

print(num_jewels_in_stones(jewels, stones))
