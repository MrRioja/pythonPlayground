# Problem: https://www.hackerrank.com/challenges/three-month-preparation-kit-lonely-integer/problem?h_r=internal-search
# Given an array of integers, where all elements but one occur twice, find the unique element.
# Ex: a = [1, 2, 3, 4, 3, 2, 1]. The unique element is 4.

from collections import Counter


def lonely_integer(a):
    int_count = Counter(a)

    return [x for (x, y) in int_count.items() if y == 1][0]
