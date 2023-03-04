# problem: https://www.hackerrank.com/challenges/pangrams/problem
# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram
# in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
# Example: s = "The quick brown fox jumps over the lazy dog"
# The string contains all letters in the English alphabet, so return pangram.

def pangrams(s):
    codes = list(range(65, 91)) + [32]
    english_alphabet = {chr(code) for code in codes}

    return 'pangram' if english_alphabet.issubset(s.upper()) else 'not pangram'
