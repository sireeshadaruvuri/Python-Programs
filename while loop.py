# indentation is very important in python as there are no curly braces
# in while loop it executes till indentation and moves to next line if the condition is false
# syntax

a = 3
b = 2
while a == b:
    print('it is true')
print('it is not true')
# avoid running infinite loops as the system will stuck
# if i give true condition in while loop it keeps running until it is false

age = 10
while age < 20:
    print(age)
    age = age + 1
print('false')

i = 0
while i < 5:
    print(i)
    i += 1
print('it is done')

# using break loop can be stopped even if the condition is true
i = 1
while i < 4:
    print(i)
    if i == 2:
        break
    i += 1

i = 4
while i == 4:
    print(i)
    break

#continue statement stops current interation and continue with the next

#using hash multiple lines of code cannot be commented
#multi lines of code can be commented using triple quotes,
# as the string is not assigned to any variable python won't execture the code
"""
i = 1
while i < 6:
    i += 1
    if(i == 3):
        continue
    print(i)
"""

i = 0
while i < 6:
    print(i)
    i += 1
else:
    print("i is not less than 6")