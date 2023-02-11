# Problem: https://www.hackerrank.com/challenges/simple-array-sum/problem
# Given an array of integers, find the sum of its elements.
# For example, if the array ar=[1,2,3], so return 6.

vector = [338, 65, 713, 595, 428, 610, 728, 573, 871, 868]


def sum_array_elements(vector):
    total = 0

    for el in vector:
        total += el

    return total


sum_array_elements(vector)
