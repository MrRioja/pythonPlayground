# Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=internal-search
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# Ex: arr = [1, 3, 5, 7, 9]
# The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24.
# The function prints: 16 24


def mini_max_sum(arr):
    sorted_arr = sorted(arr)
    middle_numbers_sum = sum(sorted_arr[1:-1])
    min_sum = middle_numbers_sum + sorted_arr[0]
    max_sum = middle_numbers_sum + sorted_arr[-1]

    print(min_sum, max_sum)


arr = [7, 69, 2, 221, 8974]

mini_max_sum(arr)
