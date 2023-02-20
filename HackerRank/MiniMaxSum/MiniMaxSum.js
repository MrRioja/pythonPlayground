// Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=internal-search
// Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
// Then print the respective minimum and maximum values as a single line of two space-separated long integers.
// Ex: arr = [1, 3, 5, 7, 9]
// The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24.
// The function prints: 16 24

export function miniMaxSum(arr) {
  const sorted_arr = arr.sort((a, b) => a - b);
  const middle_numbers_sum = arr.reduce((acc, num, index, array) => {
    if (index !== 0 && index !== array.length - 1) {
      acc += num;
    }

    return acc;
  }, 0);
  const min_sum = middle_numbers_sum + sorted_arr[0];
  const max_sum = middle_numbers_sum + sorted_arr[sorted_arr.length - 1];

  return [min_sum, max_sum];
}
