# Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# You are in charge of the cake for a child's birthday.
# You have decided the cake will have one candle for each year of their total age.
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
# The maximum height candles are 4 units high.

candles = [4, 5, 1, 9, 10, 900, 30, 4, 4, 7, 4]


def birth_day_cake_candles(candles):
    tallest = max(int(candle) for candle in candles)
    total = 0

    for candle in candles:
        if candle == tallest:
            total += 1

    return total


birth_day_cake_candles(candles)
