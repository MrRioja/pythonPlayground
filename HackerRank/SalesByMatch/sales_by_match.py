# Problem: https://www.hackerrank.com/challenges/sock-merchant/problem
# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.
# Example: n=7, ar=[1,2,1,2,1,3,2]
# There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color.
# The number of pairs is 2.

from collections import Counter


def sock_merchant(_, ar):
    pairs = 0

    for total in list(Counter(ar).values()):
        pairs += total // 2 if total > 1 else 0

    return pairs
