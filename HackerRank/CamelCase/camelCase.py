# Problem: https://www.hackerrank.com/challenges/camelcase/problem
# There is a sequence of words in CamelCase as a string of letters, S, having the following properties:
# * It is a concatenation of one or more words consisting of English letters.
# * All letters in the first word are lowercase.
# * For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
# Given , determine the number of words in S.
# Ex: oneTwoThree, has three words.

import re


def camel_case(s):
    words = len(re.findall("[A-Z]", s))

    return words + 1


print(camel_case("saveChangesInTheEditor"))
