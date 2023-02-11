# Problem: https://www.hackerrank.com/challenges/flipping-bits/problem?h_r=internal-search
# You will be given a list of 32 bit unsigned integers. Flip all the bits(1 -> 0 and 0 -> 1) and return the result as an unsigned integer.
# Example: 9(base 10) -> 1001 (base 2)
# 00000000000000000000000000001001 = 9
# 11111111111111111111111111110110 = 4294967286
# Return 4294967286

def flipping_bits(n):
    n_binary = ''
    quotient = n

    while quotient >= 2:
        n_binary += str(quotient % 2)
        quotient = quotient//2

    n_binary += str(quotient)
    n_binary = n_binary[::-1].zfill(32)

    n_binary_inverted = [0 if n == '1' else 1 for n in n_binary]
    result = [n*(2**(len(n_binary_inverted)-index))
              for index, n in enumerate(n_binary_inverted, 1)]

    return sum(result)
