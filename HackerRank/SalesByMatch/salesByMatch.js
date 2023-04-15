// Problem: https://www.hackerrank.com/challenges/sock-merchant/problem
// There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock,
// determine how many pairs of socks with matching colors there are.
// Example: n=7, ar=[1,2,1,2,1,3,2]
// There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color.
// The number of pairs is 2.

export function sockMerchant(_, ar) {
  let pairs = 0;

  let total_per_items = new Map();
  ar.forEach((element) => {
    total_per_items.set(element, (total_per_items.get(element) || 0) + 1);
  });

  for (const total of total_per_items.values()) {
    pairs += total > 1 ? Math.floor(total / 2) : 0;
  }

  return pairs;
}
