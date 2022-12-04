// Problem: https://leetcode.com/problems/jewels-and-stones/
// You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
// Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
// Letters are case sensitive, so "a" is considered a different type of stone from "A".
// Input: jewels = "aA", stones = "aAAbbbb"
// Output: 3

/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
function numJewelsInStones(jewels, stones) {
  let numJewels = 0;

  for (const stone of stones) {
    for (const jewel of jewels) {
      if (stone == jewel) {
        numJewels += 1;
      }
    }
  }

  return numJewels;
}

const jewels = "z";
const stones = "ZZ";

console.log(numJewelsInStones(jewels, stones));
