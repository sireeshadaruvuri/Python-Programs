import numpy as np
from numpy.random import randn
# -2 -- -1 -- 0 -- 1 -- 2
randn()
x = randn()
answer = None
if x > 1:
    answer = "x is greater than 1"
else:
    answer = "x is less than 1"
print(x)
print(answer)
#nested loops - else if statements
# -2 -- -1 -- 0 -- 1 -- 2
if x > 1:
    ans = "x is greater than 1"
else:
    if x >= -1:
        ans = "x is in between -1 and 1"
    else:
        ans = "x is less than -1 "
print(x)
print(ans)
#chained statements to reduce more lines of code (properly alligned n else if is called in python as elif)
if x > 1:
    ans = "x is greater than 1"
elif x >= -1:
    ans = "x is in between -1 and 1"
else:
    ans = "x is less than -1 "
print(x)
print(ans)