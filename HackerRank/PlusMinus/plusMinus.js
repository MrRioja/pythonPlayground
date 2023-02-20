// Problem: https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?h_r=internal-search
// Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
// Print the decimal value of each fraction on a new line with 6 places after the decimal.
// Ex: arr = [1, 1, 0, -1, -1]
// There are n = 5 elements, two positive, two negative and one zero. Their ratios are 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000.
// Results are printed as:
// 0.400000
// 0.400000
// 0.200000

export function plusMinus(arr) {
  const positive = arr.filter((num) => num > 0);
  const negative = arr.filter((num) => num < 0);
  const zero = arr.filter((num) => num === 0);

  return [
    `${(positive.length / arr.length).toFixed(6)}`,
    `${(negative.length / arr.length).toFixed(6)}`,
    `${(zero.length / arr.length).toFixed(6)}`,
  ];
}
