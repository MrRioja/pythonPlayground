// Problem: https://leetcode.com/problems/shuffle-string/
// Given a string s and an integer array indices of the same length.
// The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
// Return the shuffled string.
// Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
// Output: "leetcode"

/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
export function restoreString(s, indices) {
  let unscrambledWord = "";

  for (let index = 0; index < s.length; index++) {
    unscrambledWord += s[indices.indexOf(index)];
  }

  return unscrambledWord;
}
