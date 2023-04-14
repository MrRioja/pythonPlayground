// Problem: https://www.hackerrank.com/challenges/migratory-birds/problem
// Given an array of bird sightings where every element represents a bird type id, determine the id of the most
// frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
// Example: There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.

export function migratoryBirds(arr) {
  let total_per_items = new Map();
  arr.forEach((element) => {
    total_per_items.set(element, (total_per_items.get(element) || 0) + 1);
  });

  let max_frequency = 0;
  for (const [, frequency] of total_per_items) {
    if (frequency > max_frequency) {
      max_frequency = frequency;
    }
  }

  let min_item_with_max_frequency = Infinity;
  for (const [item, frequency] of total_per_items) {
    if (item < min_item_with_max_frequency && frequency == max_frequency) {
      min_item_with_max_frequency = item;
    }
  }

  return min_item_with_max_frequency;
}
