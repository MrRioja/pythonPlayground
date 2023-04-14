# Problem: https://www.hackerrank.com/challenges/migratory-birds/problem
# Given an array of bird sightings where every element represents a bird type id, determine the id of the most
# frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
# Example: There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.

from collections import Counter


def migratory_birds(arr):
    total_per_items = Counter(arr)
    [(_, max_frequency)] = total_per_items.most_common(1)
    items_with_max_frequency = sorted([
        num for num, total in total_per_items.most_common() if total == max_frequency])

    return items_with_max_frequency[0]
