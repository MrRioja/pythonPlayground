# Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix arr is shown below:
# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal = 1 + 5 + 9 = 15.
# The right to left diagonal = 3 + 5 + 9 = 17.
# Their absolute difference is | 15 - 17| = 2.

def get_diagonal_difference(array):
    left_to_right = get_sum_diagonal_left_right(array)
    right_to_left = get_sum_diagonal_right_left(array)
    difference = left_to_right - right_to_left

    return abs(difference)


def get_sum_diagonal_left_right(array):
    sum_diagonal = 0
    counter = 0

    for _ in array:
        element = array[counter][counter]
        sum_diagonal += element
        counter += 1

    return sum_diagonal


def get_sum_diagonal_right_left(array):
    sum_diagonal = 0
    counter = 0

    for _ in array:
        element = array[counter][len(array) - 1 - counter]
        sum_diagonal += element
        counter += 1

    return sum_diagonal
