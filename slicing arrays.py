import numpy as np

a = np.array([12, 34, 56, 78])
print(a)
print(a[:2])
#while working on arrays we r not making the copy of an array
#in lists it creates the copy of a list
print(a[2:4])
b = a[2:4]
print(b)
print(b[0])
#change values of b
b[:]=211
print(b)
print(a)
#b doesn't copy array a, it just creates the view of a
#it takes lots of space to create copies of arrays
#to copy array copy method can be used
c = a.copy()
print(c)
c[0]=10
print(c)
print(a)