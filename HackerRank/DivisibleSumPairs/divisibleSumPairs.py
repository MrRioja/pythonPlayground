# Problem: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# Given an array of integers and a positive integer k, determine the number of(i, j) pairs where
# i < j and arr[i] + arr[j] is divisible by k.
# Example: arr = [1, 2, 3, 4, 5, 6], k = 5
# Three pairs meet the criteria: [1, 4], [2, 3] and [4, 6].

def divisible_sum_pairs(n, k, ar):

    count = 0

    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                print(ar[i], ar[j])
                count += 1

    return count


n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]
print(divisible_sum_pairs(n, k, ar))
