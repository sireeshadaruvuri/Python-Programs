for i in range(5):
    print("python is easy to learn")
    # display range values
    print("python is easy to learn: ", i)
    # range from to to value from 0 to 5
    print(range(5))
    # use list to display the values in range 0,1,2,3,4
    print(list(range(5)))
#range from 2 to 6 but not including 6
for i in range(2,6):
    print(i)
#The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter
#now the i value will be incremented to 3 everytime till 30 like 2, 5, 8, 11, ..
for i in range(2,30,3):
    print(i)
for i in range(2,30,3):
    print(i)
# create a list for values, for loop iterates for the vales in mylist
mylist = [1, 2, 3, 4, 5]
for j in mylist:
    print("values: ", j)
# practice exercise: display values till i less than 10
a = 0
while (a < 10):
    print(a)
    a += 1

for b in range(10):
    print(b)
    print(list(range(10)))
#using list
newlist = [0,1,2,3,4,5,6,7,8,9]
for n in newlist:
    print("values of n are: ", n)

#looping through string values
#Even strings are iterable objects, they contain a sequence of characters:
x = ["anvi","abhi","akki","arun"]
for y in x:
    print(y)
for y in "abhi":
    print(y)
#break statement usage in for loop
x = ["anvi","abhi","akki","arun"]
for y in x:
    if y == "akki":
        break
    print(y)
#give print before break
x = ["anvi","abhi","akki","arun"]
for y in x:
    if y == "akki":
        print(y)
        break
#With the continue statement we can stop the current iteration of the loop, and continue with the next
x = ["anvi","abhi","akki","arun"]
for y in x:
    if y == "akki":
        continue
    print(y)
#else statement in for loop
s = ["a","b","c","d","e"]
for w in s:
    print(s)
else:
    print("list has ended")
#nested loop - A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop":
x = ["siri","arun","anvi"]
y = ["purni","abhi","akki"]
for jj in x:
    for kk in y:
        print(jj,kk)
#pass statement
#for loops cannot be empty, but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.
for u in [0,1,2]:
    pass
