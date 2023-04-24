//  Problem: https://www.hackerrank.com/challenges/three-month-preparation-kit-the-birthday-bar/problem
//  Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
//  Lily decides to share a contiguous segment of the bar selected such that:
//  - The length of the segment matches Ron's birth month, and,
//  - The sum of the integers on the squares is equal to his birth day.
//  Determine how many ways she can divide the chocolate.
//  Example:
//    d = 4
//    m = 2
//    s = [2,2,1,3,2]
//  Lily wants to find segments summing to Ron's birth day, d=4 with a length equalling his birth month, m=2.
//  In this case, there are two segments meeting her criteria: [2,2] and [1,3].

export function birthday(s, d, m) {
  let n_ways = 0;

  for (let index = m - 1; index <= s.length; index++) {
    let total = s[index];

    for (let item = index - m + 1; item < index; item++) {
      total += s[item];
    }

    if (total == d) {
      n_ways += 1;
    }
  }

  return n_ways;
}
