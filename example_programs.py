# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
from pip._vendor.distlib.compat import raw_input

a = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        a.append(str(i))
print(a)


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


x = int(raw_input())
print(fact(x))
