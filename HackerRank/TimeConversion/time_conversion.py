# Problem: https://www.hackerrank.com/challenges/time-conversion/problem
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.


def time_conversion(s):
    hours = s.split(":")[0]
    minutes = s.split(":")[1]
    seconds = s.split(":")[2][0:2]
    turn = s.split(":")[2][2:4]
    converted_hour = ""

    if turn == "AM":
        if int(hours) == 12:
            converted_hour = "00"
        else:
            converted_hour = str(hours)
    else:
        if int(hours) == 12:
            converted_hour = str(hours)
        else:
            hours = int(hours) + 12
            converted_hour = str(hours)

    return converted_hour + ":" + minutes + ":" + seconds
