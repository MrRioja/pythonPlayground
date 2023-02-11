# Problem: https://www.hackerrank.com/challenges/kangaroo/problem
# You are choreographing a circus show with various animals. For one act, you are given
# two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show.
# If it is possible, return YES, otherwise return NO.
# Ex:
# x1 = 2
# v1 = 1
# x2 = 1
# v2 = 2
# After one jump, they are both at x = 3, (x1 + v1 = 2 + 1, x2 + v2 = 1 + 2), so the answer is YES

# Other solution
# def kangaroo(x1, v1, x2, v2):
#     if (v1<=v2):
#         return "NO"
#     return("YES" if (x2-x1)%(v2-v1)==0 else "NO")

def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1:
        return 'NO'

    jump = 1

    while jump < 1000:
        if (x1 + (v1*jump)) == (x2 + (v2*jump)):
            print(jump)
            return 'YES'
        jump += 1

    return 'NO'


parameters = (4523, 8092, 9419, 8076)

x1, v1, x2, v2 = parameters

print(kangaroo(x1, v1, x2, v2))
