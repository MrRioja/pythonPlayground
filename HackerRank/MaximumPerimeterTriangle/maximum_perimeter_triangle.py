# Problem: https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
# Given an array of stick lengths, use 3 of them to construct a non-degenerate triangle with the maximum possible perimeter.
# Return an array of the lengths of its sides as 3 integers in non-decreasing order.
# If there are several valid triangles having the maximum perimeter:
# - Choose the one with the longest maximum side.
# - If more than one has that maximum, choose from them the one with the longest minimum side.
# - If more than one has that maximum as well, print any one them.
# If no non-degenerate triangle exists, return [-1].
# Example: sticks = [1, 2, 3, 4, 5, 10]
# The triplet(1, 2, 3) will not form a triangle. Neither will(4, 5, 10) or (2, 3, 5), so the problem is reduced to
# (2, 3, 4) and (3, 4, 5). The longer perimeter is 3 + 4 + 5 = 12.


from itertools import combinations


def maximum_perimeter_triangle(sticks):

    max_perimeter = 0
    possibles_triangles = []
    sorted_sticks = sorted(sticks)

    for a, b, c in combinations(sorted_sticks, 3):
        if a != 0 and b != 0 and c != 0 and ((a + b) > c):
            if (a + b + c) > max_perimeter:
                max_perimeter = a + b + c
                possibles_triangles.clear()
                possibles_triangles.append([a, b, c])
            elif (a + b + c) == max_perimeter:
                possibles_triangles.append([a, b, c])

    if len(possibles_triangles) > 0:
        return possibles_triangles[0]
    else:
        return [-1]
