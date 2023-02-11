# Problem: https://www.hackerrank.com/challenges/sparse-arrays/problem?h_r=internal-search
# There is a collection of input strings and a collection of query strings. For each query string,
# determine how many times it occurs in the list of input strings. Return an array of the results.
# Ex: strings = ['ab', 'ab', 'abc']
# queries = ['ab', 'abc', 'bc']
# There are 2 instances of 'ab', 1 of 'abc' and 0 of 'bc'. For each query, add an element to the return array, results = [2, 1, 0].

# Other solution:
# from collections import Counter


# def matching_strings(strings, queries):

#     strings_count = Counter(strings)
#     return [strings_count[x] for x in queries]

# def matching_strings(strings, queries):
#     return [
#         strings.count(query)
#         for query in queries
#     ]


def matching_strings(strings, queries):
    total_per_item = {
        query: 0
        for query in queries
    }
    results = []

    for query in queries:
        if total_per_item[query] > 0:
            results.append(total_per_item[query])

            continue

        for string in strings:
            if query == string:
                total_per_item[query] += 1

        results.append(total_per_item[query])

    return results


queries = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']
strings = ['13', 'abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj',
           'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', '5']


print(matching_strings(strings, queries))
