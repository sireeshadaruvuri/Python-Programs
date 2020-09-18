# variables can be numericals or alphabets
# they can start with underscore
# they should not start with numbers
# they should not have any other special characters other than underscore
# variables are case sensitive

# Legal variable names:
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

import math

# int
age = 3
print(type(age))

# float
y = 2.5
print(type(y))

# string
a = "hello"
print(type(a))
b = '2'
print(type(b))

# logical/boolean
c = True
print(type(c))

# how to use variables
A = 10
B = 5
C = A + B
print(C)

D = B / A
print(D)
#import math for arithmetic functions like squareroot
E = math.sqrt(A)
print(round(E)) #make a round off of the number
#direct printing
print(math.sqrt(16))

#combine two strings
AB = "Hello"
CD = "Siri"
EF = AB + " " + CD
print(EF)

#error unsupported operand type(s) for /: 'str' and 'int'
ab = "Hello"
ej = 3
y = ab / ej
print(y)

#error saying unsupported operand type(s) for +: 'bool' and 'str'
o = True
p = "Siri"
l = o + " " + p
print(l)
"""
# Python allows you to assign values to multiple variables in one line:
# And you can assign the same value to multiple variables in one line:
from _ast import Global

"""
x, y, z = 2, "banana", "cherry"
print(x, y, z)
x = y = z = "orange"
print(x, y, z)

#python uses + character to combine both text and the variable

x = "oranges"
print("My baby loves " +x)
"""
# global variables - variables which are created outside the function - can be used anywhere by anyone

x = "oranges"

def myfunc():
    print("my baby loves " + x)

myfunc()

#local varibale - which is created inside the function and can be used only within the function

x = "oranges"
def myfunc():
    x = "bananas"
    print("my baby loves " +x)
myfunc()
print("my baby loves " +x)

#global keyword can be used to create global variable inside the function

def myfunc():
    global x
    x = "oranges"
    print("my baby loves " +x)
myfunc()
print("my baby likes " +x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)