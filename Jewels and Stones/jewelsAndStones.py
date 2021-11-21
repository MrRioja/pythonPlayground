# Problem: https://leetcode.com/problems/jewels-and-stones/
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
# Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

jewels = "aA"
stones = "aAAbbbb"


# jewels = "z"
# stones = "ZZ"


def numJewelsInStones(jewels: str, stones: str) -> int:
    numJewels = 0

    for stone in stones:
        for jewel in jewels:
            if stone == jewel:
                numJewels += 1

    return numJewels


print(numJewelsInStones(jewels, stones))
