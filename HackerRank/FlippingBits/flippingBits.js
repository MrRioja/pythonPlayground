// Problem: https://www.hackerrank.com/challenges/flipping-bits/problem?h_r=internal-search
// You will be given a list of 32 bit unsigned integers. Flip all the bits(1 -> 0 and 0 -> 1) and return the result as an unsigned integer.
// Example: 9(base 10) -> 1001 (base 2)
// 00000000000000000000000000001001 = 9
// 11111111111111111111111111110110 = 4294967286
// Return 4294967286

function flippingBits(n) {
  let n_binary = "";
  let n_binary_inverted = "";
  let quotient = n;

  while (quotient >= 2) {
    n_binary += String(quotient % 2);
    quotient = Math.floor(quotient / 2);
  }

  n_binary += String(quotient);
  n_binary = n_binary.split("").reverse().join("").padStart(32, "0");

  for (const num of n_binary) {
    n_binary_inverted += num === "0" ? "1" : "0";
  }

  let result = n_binary_inverted
    .split("")
    .reduce(
      (acc, num, index) => acc + Number(num) * 2 ** (32 - (index + 1)),
      0
    );

  return result;
}

console.log(flippingBits(2147483647));
console.log(flippingBits(1));
console.log(flippingBits(0));
