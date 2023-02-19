// Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
// You are in charge of the cake for a child's birthday.
// You have decided the cake will have one candle for each year of their total age.
// They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
// The maximum height candles are 4 units high.

export function birthdayCakeCandles(candles) {
  let tallest = Math.max(...candles);
  let total = 0;

  candles.forEach((candle) => {
    if (candle === tallest) {
      total += 1;
    }
  });

  return total;
}
