// Problem: https://www.hackerrank.com/challenges/sparse-arrays/problem?h_r=internal-search
// There is a collection of input strings and a collection of query strings. For each query string,
// determine how many times it occurs in the list of input strings. Return an array of the results.
// Ex: strings = ['ab', 'ab', 'abc']
// queries = ['ab', 'abc', 'bc']
// There are 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. For each query, add an element to the return array, results = [2, 1, 0].

// Other solution:
// function matchingStrings(strings, queries) {
//   return queries.map((q) => strings.filter((s) => s === q).length);
// }

export function matchingStrings(strings, queries) {
  const total_per_item = {};
  const results = [];

  for (const query of queries) {
    if (query in total_per_item) {
      results.push(total_per_item[query]);

      continue;
    } else {
      total_per_item[query] = 0;
    }

    for (const string of strings) {
      if (query === string) {
        total_per_item[query]++;
      }
    }

    results.push(total_per_item[query]);
  }

  return results;
}
