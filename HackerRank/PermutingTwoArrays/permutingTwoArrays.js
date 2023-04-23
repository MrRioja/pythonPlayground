// Problem: https://www.hackerrank.com/challenges/two-arrays/problem
// There are two n-element arrays of integers, A and B. Permute them into some A' and B' such that the relation
// A'[i] + B'[i] >= K holds for all i where 0 <= i < n. There will be Q queries consisting of A, B, and K.
// For each query, return YES if some permutation A', B' satisfying the relation exists. Otherwise, return NO.
// Example:
//     A = [0, 1]
//     B = [0, 2]
//     K = 1
// A valid A', B' is A' = [1, 0] and B' = [0, 2]: 1+0 >= 1 and 0+2 >= 1. Return YES.

export function twoArrays(k, a, b) {
  const a_sorted = a.sort((a, b) => a - b);
  const b_reversed_sorted = b.sort((a, b) => b - a);

  for (let index = 0; index < a.length; index++) {
    if (a_sorted[index] + b_reversed_sorted[index] < k) {
      return "NO";
    }
  }

  return "YES";
}
