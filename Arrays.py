import numpy as np
list = [2,3,45,67,89,90]
print(list)
a = np.array(list)
print(a)
#arrays won't accept different datatypes while lists accept diff datatypes in the list
list.pop()
print(list)
#there are very powerful functions available inside arrays
b = a.mean()
print(b)
print(a.sum())