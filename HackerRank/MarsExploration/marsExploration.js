// Problem: https://www.hackerrank.com/challenges/mars-exploration/problem
// A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
// Letters in some of the SOS messages are altered by cosmic radiation during transmission.
// Given the signal received by Earth as a string, s, determine how many letters of the SOS message have been changed by radiation.
// Example: s = "SOSTOT"
// The original message was SOSSOS. Two of the message's characters were changed in transit.

export function marsExploration(s) {
  let changed_in_transit = 0;
  const splitted_string = s.split("");
  const expected_messages = s.length / 3;
  const expected_message = new Array(expected_messages)
    .fill("SOS")
    .flatMap((el) => el.split(""));

  for (let i = 0; i < splitted_string.length; i++) {
    if (splitted_string[i] != expected_message[i]) {
      changed_in_transit += 1;
    }
  }

  return changed_in_transit;
}
