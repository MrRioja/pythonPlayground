# Problem: https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem
# Camel Case is a naming style common in many programming languages. In Java, method and variable names typically
# start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread).
# Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).
# Your task is to write a program that creates or splits Camel Case variable, method, and class names.
# Each line of the input file will begin with an operation (S or C) followed by a semi-colon followed by M, C, or V
# followed by a semi-colon followed by the words you'll need to operate on.
# The operation will either be S (split) or C (combine)
# M indicates method, C indicates class, and V indicates variable
# In the case of a split operation, the words will be a camel case method, class or variable name that you need to split
#  into a space-delimited list of words starting with a lowercase letter.
# In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase letters that
# you need to combine into the appropriate camel case String. Methods should end with an empty set of parentheses to
# differentiate them from variable names.

import re

word = input('Type something: ')


def camel_case(word):
    [operation, typeValue, value] = word.split(';')

    if operation == 'S':
        allMatch = re.findall('[A-Z]', value)

        for match in allMatch:
            value = value.replace(match, ' ' + match.lower())

        return value.replace('()', '').strip()
    else:
        allMatch = re.findall('\s\w', value)

        for match in allMatch:
            value = value.replace(match, match.strip().upper())

        if typeValue == 'V':
            return value
        elif typeValue == 'M':
            return value + '()'
        else:
            return value.replace(value[0], value[0].upper(), 1)
