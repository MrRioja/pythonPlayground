# Problem: https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?h_r=internal-search
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with 6 places after the decimal.
# Ex: arr = [1, 1, 0, -1, -1]
# There are n = 5 elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000.
# Results are printed as:
# 0.400000
# 0.400000
# 0.200000


def plus_minus(arr):
    positive = [num for num in arr if num > 0]
    negative = [num for num in arr if num < 0]
    zero = [num for num in arr if num == 0]

    print(
        f'{(len(positive)/len(arr)):.6f}',
        f'\n{len(negative)/len(arr):.6f}',
        f'\n{len(zero)/len(arr):.6f}'
    )


arr = [1, 1, 0, -1, -1]

plus_minus(arr)
