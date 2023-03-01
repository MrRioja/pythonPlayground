# Problem: https://www.hackerrank.com/challenges/counting-valleys/problem
# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps steps,
# for every step it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and end at sea level,
# and each step up or down represents a 1 unit change in altitude. We define the following terms:
# - A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending
#   with a step down to sea level.
# - A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending
#   with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
# Example: steps == 8 path == [DDUUUUDD]
# The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high.
# Finally, the hiker returns to sea level and ends the hike.


def level_sea():
    level = 0
    valley = 0

    def change_level(step):
        nonlocal level, valley
        level += 1 if step == 'U' else -1
        valley += 1 if (level == 0 and step == 'U') else 0

        return valley
    return change_level


def counting_valleys(steps, path):

    counter_valleys = level_sea()
    total_valleys = [
        counter_valleys(step)
        for step in path
    ]

    return total_valleys[-1]
