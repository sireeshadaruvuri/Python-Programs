# In Python a function is defined using the def keyword
def myfun():
    print("this is a function")


# function will run only when it is called
# To call a function, use the function name followed by parenthesis
myfun()


# Information can be passed into functions as arguments
def myfunction(fname):
    print(fname + " Daruvuri")


myfunction("Annapurna")
myfunction("Sireesha")
myfunction("phanith")
myfunction("sreekanth")


# with two arguments
def myf(fname, lname):
    print(fname + " " + lname)


myf("sireesha", "daruvuri")
myf("purni", "daruvuri")
# try calling function with less or more args than given
#myf("phanith")  # error is myf() missing 1 required positional argument: 'lname'


# -----------
# If you do not know how many arguments that will be passed into your function
# add a * before the parameter name in the function definition
# This way the function will receive a tuple of arguments, and can access the items accordingly
def func(*names):
    print("name is " + names[2])

func("siri", "anvi", "arun")
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter
def fn(name1, name2, name3):
    print("name is " + name1)
fn(name1 = "siri", name2 = "arun", name3 = "anvi")
#If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition
def fn1(**names):
    print("lname is " + names["lname"])
fn1(fname = "siri", lname = "daruvuri")
#The following example shows how to use a default parameter value
#If we call the function without argument, it uses the default value
def fn2(name = "siri"):
    print("my name is " + name)
fn2("anvi")
fn2()
fn2("arun")
#passing a list an argument
#if you send a List as an argument, it will still be a List when it reaches the function
def fn3(names):
    for i in names:
        print(i)
fname = ["siri","abhi","akki"]
fn3(fname)
#To let a function return a value, use the return statement
def fn4(f):
    return 5 * f
print(fn4(10))
print(fn4(15))
#function definitions cannot be empty, but if you for some reason have a function definition
# with no content, put in the pass statement to avoid getting an error
def fn5():
    pass
#recursion
#Python also accepts function recursion, which means a defined function can call itself.
#Recursion is a common mathematical and programming concept. It means that a function calls itself
#This has the benefit of meaning that you can loop through data to reach a result.
"""
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
"""
def fn6(j):
    if(j > 0):
        res = j + fn6(j-1)
        print(res)
    else:
        res = 0
    return res
fn6(6)
#range, length, type, max, min are some functions