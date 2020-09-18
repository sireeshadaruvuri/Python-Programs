import numpy as np

# arange function
mydata = np.arange(0, 20)
print(mydata)
# use reshape function
# syntax is first one is data second is dimensions third is the format same as C language (rows first and columns next)
matrix1 = np.reshape(mydata, (5, 4), order='c')
print(matrix1)
# print number 10
c = matrix1[2, 2]
print(c)
# order f - first put data in columns n then rows
matrix2 = np.reshape(mydata, (5, 4), order='f')
print(matrix2)
d = matrix2[0, 2]
print(d)
# Object Oriented programming concept
# as mydata is array (becasue it is created with arange function)
# instead of using np to call reshape function we can use mydata object to call it
m1 = mydata.reshape((5, 4))
print(m1)
#------------------
#create 3 lists
l1 = ["I", "am", "happy", "today"]
l2 = ["y", "am", "I", "happy"]
l3 = [1,2,3,4]
l4 =[l1, l2, l3]
print(l4)
#use np.array function to conver list l4 to array
l5 = np.array(l4)
print(l5)