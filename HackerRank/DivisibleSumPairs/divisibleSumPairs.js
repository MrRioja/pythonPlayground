// Problem: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
// Given an array of integers and a positive integer k, determine the number of(i, j) pairs where
// i < j and arr[i] + arr[j] is divisible by k.
// Example: arr = [1, 2, 3, 4, 5, 6], k = 5
// Three pairs meet the criteria: [1, 4], [2, 3] and [4, 6].

export function divisibleSumPairs(n, k, ar) {
  let count = 0;

  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (ar[i] < ar[j] && (ar[i] + ar[j]) % k == 0) {
        console.log(ar[i], ar[j]);
        count += 1;
      }
    }
  }

  return count;
}
