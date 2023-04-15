// problem: https://www.hackerrank.com/challenges/pangrams/problem
// A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram
// in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
// Example: s = "The quick brown fox jumps over the lazy dog"
// The string contains all letters in the English alphabet, so return pangram.

export function pangrams(s) {
  const codes = Array.from({ length: 26 }, (_, i) => i + 65).concat([32]);
  const english_alphabet = new Set(
    codes.map((code) => String.fromCharCode(code))
  );

  const letters = new Set(
    s
      .toUpperCase()
      .split("")
      .filter((c) => english_alphabet.has(c))
  );

  return letters.size === english_alphabet.size ? "pangram" : "not pangram";
}
