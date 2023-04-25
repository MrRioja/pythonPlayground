// Problem: https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
// Given an array of stick lengths, use 3 of them to construct a non-degenerate triangle with the maximum possible perimeter.
// Return an array of the lengths of its sides as 3 integers in non-decreasing order.
// If there are several valid triangles having the maximum perimeter:
// - Choose the one with the longest maximum side.
// - If more than one has that maximum, choose from them the one with the longest minimum side.
// - If more than one has that maximum as well, print any one them.
// If no non-degenerate triangle exists, return [-1].
// Example: sticks = [1, 2, 3, 4, 5, 10]
// The triplet(1, 2, 3) will not form a triangle. Neither will(4, 5, 10) or (2, 3, 5), so the problem is reduced to
// (2, 3, 4) and (3, 4, 5). The longer perimeter is 3 + 5 + 5 = 12.

export function maximumPerimeterTriangle(sticks) {
  let max_perimeter = 0;
  let possibles_triangles = [];
  let sorted_sticks = sticks.sort((a, b) => a - b);

  for (let i = 2; i < sorted_sticks.length; i++) {
    let [a, b, c] = [
      sorted_sticks[i - 2],
      sorted_sticks[i - 1],
      sorted_sticks[i],
    ];

    if (a != 0 && b != 0 && c != 0 && a + b > c) {
      if (a + b + c > max_perimeter) {
        max_perimeter = a + b + c;
        possibles_triangles = [];
        possibles_triangles.push([a, b, c]);
      } else if (a + b + c == max_perimeter) {
        possibles_triangles.push([a, b, c]);
      }
    }
  }

  if (possibles_triangles.length > 0) {
    return possibles_triangles[0];
  } else {
    return [-1];
  }
}
