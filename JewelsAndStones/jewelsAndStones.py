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
    jewels = set(jewels)

    for stone in stones:
        if stone in jewels:
            numJewels += 1

    return numJewels


print(numJewelsInStones(jewels, stones))


# se vc fosse criar testes unitários em pytest para Intersection of Two Arrays e shuffleString, quais seriam?
# consegue escrever em python alguns exemplos simples?
