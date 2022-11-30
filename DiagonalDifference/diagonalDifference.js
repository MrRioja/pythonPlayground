// Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
// Given a square matrix, calculate the absolute difference between the sums of its diagonals.
// For example, the square matrix arr is shown below:
// 1 2 3
// 4 5 6
// 9 8 9
// The left-to-right diagonal = 1 + 5 + 9 = 15.
// The right to left diagonal = 3 + 5 + 9 = 17.
// Their absolute difference is | 15 - 17| = 2.

function getDiagonalDifference(array) {
  let leftToRight = getSumDiagonalLeftRight(array);
  let rightToLeft = getSumDiagonalRightLeft(array);
  let difference = leftToRight - rightToLeft;

  return Math.abs(difference);
}

function getSumDiagonalLeftRight(array) {
  let sumDiagonal = 0;

  for (let index = 0; index < array.length; index++) {
    const element = array[index][index];
    sumDiagonal += element;
  }

  return sumDiagonal;
}

function getSumDiagonalRightLeft(array) {
  let sumDiagonal = 0;

  for (let index = 0; index < array.length; index++) {
    const element = array[index][array.length - 1 - index];
    sumDiagonal += element;
  }

  return sumDiagonal;
}

const array = [
  [11, 2, 4],
  [4, 5, 6],
  [10, 8, -12],
];

console.log(getDiagonalDifference(array));
