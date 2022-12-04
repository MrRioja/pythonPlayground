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

    if (turn == "AM"):
        if (int(hours) == 12):
            converted_hour = "00:" + minutes + ":" + seconds
        else:
            converted_hour = str(hours) + ":" + minutes + ":" + seconds
    else:
        if (int(hours) == 12):
            converted_hour = str(hours) + ":" + minutes + ":" + seconds
        else:
            hours = int(hours) + 12
            converted_hour = str(hours) + ":" + minutes + ":" + seconds

    return converted_hour


print(time_conversion("07:05:45PM"))  # 19:05:45
print(time_conversion("12:37:58AM"))  # 00:37:58
print(time_conversion("08:37:58PM"))  # 20:37:58
print(time_conversion("07:45:18AM"))  # 07:45:18
