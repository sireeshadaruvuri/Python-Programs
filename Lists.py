# List can contain mixed datatypes
# idex start from 0 in lists
mylist = [10, 2, 4, 5]
print(mylist)
myfirstlist = ["siri", 2.5, True, mylist]
print(myfirstlist)
# range
print(range(15))
print(list(range(15)))
print(list(range(2, 15)))
a = list(range(300, 320))
print(a)
print(list(range(100, 150, 2)))
b = list(range(200, 260, 10))
print(b)

# usage of square brackets
n = ['a', 'b', 'c', 'd']
print(len(n))
print(n[0])
# negative indexation -4 -3 -2 -1 (start last num at -1)
print(n[-3])
n[2] = 'siri'
print(n)
print(n[6]) #(error out of range)
