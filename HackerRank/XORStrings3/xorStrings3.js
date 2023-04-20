// Problem: https://www.hackerrank.com/challenges/three-month-preparation-kit-strings-xor/problem
// In this challenge, the task is to debug the existing code to successfully execute all provided test files.
// Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.
// Debug the given function strings_xor to find the XOR of the two given strings appropriately.
// Note: You can modify at most three lines in the given code and you cannot add or remove lines to the code.
// To restore the original code, click on the icon to the right of the language selector.

export function stringsXOR(s, t) {
  let res = "";

  s.split("").map((item, index) => {
    if (item == t.charAt(index)) {
      res += "0";
    } else {
      res += "1";
    }
  });

  return res;
}
