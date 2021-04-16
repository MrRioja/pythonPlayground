// Problem: https://www.hackerrank.com/challenges/simple-array-sum/problem
// Given an array of integers, find the sum of its elements.
// For example, if the array ar=[1,2,3], so return 6.

var vector = [338, 65, 713, 595, 428, 610, 728, 573, 871, 868];

function sumArrayElements(vector) {
  let total = 0;

  vector.forEach((el) => (total = total + el));

  return total;
}

sumArrayElements(vector);
