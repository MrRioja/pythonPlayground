// Problem: https://www.hackerrank.com/challenges/time-conversion/problem
// Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
// Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
// - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

export function timeConversion(s) {
  let hours = s.split(":")[0];
  let minutes = s.split(":")[1];
  let seconds = s.split(":")[2].slice(0, 2);
  let turn = s.split(":")[2].slice(2, 4);
  let convertedHour = "";

  if (turn === "AM") {
    if (parseInt(hours) === 12) {
      convertedHour = "00";
    } else {
      convertedHour = hours;
    }
  } else {
    if (parseInt(hours) === 12) {
      convertedHour = hours;
    } else {
      hours = parseInt(hours) + 12;
      convertedHour = hours;
    }
  }

  return convertedHour + ":" + minutes + ":" + seconds;
}
