# Problem: https://www.hackerrank.com/challenges/mars-exploration/problem
# A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
# Letters in some of the SOS messages are altered by cosmic radiation during transmission.
# Given the signal received by Earth as a string, S, determine how many letters of the SOS message have been changed by radiation.
# Example: s = "SOSTOT"
# The original message was SOSSOS. Two of the message's characters were changed in transit.

def mars_exploration(s: str):
    expected_messages = int(len(s) / 3)
    expected_message = 'SOS' * expected_messages
    changed_in_transit = 0

    for i in range(len(s)):
        if s[i] != expected_message[i]:
            changed_in_transit += 1

    return changed_in_transit
