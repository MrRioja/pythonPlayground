# Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix arr is shown below:
# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal = 1 + 5 + 9 = 15.
# The right to left diagonal = 3 + 5 + 9 = 17.
# Their absolute difference is | 15 - 17| = 2.

array = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12],
]


def getDiagonalDifference(array):
    leftToRight = getSumDiagonalLeftRight(array)
    rightToLeft = getSumDiagonalRightLeft(array)
    difference = leftToRight - rightToLeft

    return abs(difference)


def getSumDiagonalLeftRight(array):
    sumDiagonal = 0
    counter = 0

    for index in array:
        element = array[counter][counter]
        sumDiagonal += element
        counter += 1

    return sumDiagonal


def getSumDiagonalRightLeft(array):
    sumDiagonal = 0
    counter = 0

    for index in array:
        element = array[counter][len(array) - 1 - counter]
        sumDiagonal += element
        counter += 1

    return sumDiagonal


print(getDiagonalDifference(array))
