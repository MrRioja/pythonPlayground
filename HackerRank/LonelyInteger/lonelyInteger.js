// Problem: https://www.hackerrank.com/challenges/three-month-preparation-kit-lonely-integer/problem?h_r=internal-search
// Given an array of integers, where all elements but one occur twice, find the unique element.
// Ex: a = [1, 2, 3, 4, 3, 2, 1]. The unique element is 4.

export function lonelyInteger(a) {
  const lonelyIntegers = a.filter((element) => {
    if (
      a.findIndex((num) => num === element) ===
      a.findLastIndex((num) => num === element)
    ) {
      return true;
    }
  });

  return lonelyIntegers[0];
}
