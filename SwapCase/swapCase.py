# Problem: You are given a string and your task is to swap cases. In other words,
# convert all lowercase letters to uppercase letters and vice versa.
# Ex: Www.HackerRank.com => wWW.hACKERrANK.COM

import re


def swap_case(s):
    upper = re.compile('[A-Z]')

    return ''.join([
        w.lower()
        if re.match(upper, w) else w.upper() for w in s
    ])


print(swap_case('WwW.TeStE.cOm'))
