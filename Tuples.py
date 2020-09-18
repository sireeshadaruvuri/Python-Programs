#tuple is immutable list (immutable sequence of values)
t1 = (12,34,56) #use paranthesis instead of square brackets like lists
print(t1[2])
print(t1[0:2])
#t1[0] = 23 #tuples cannot be changed they are immutable

#to add one item in tuple we should comma after one item, otherwise python wouldn't recognise it as a tuple
mytuple = ('a')
print(type(mytuple))
mytu = ('b',)
print(type(mytu))

#tuples cannot be changes but there is a workaorund
#they can be converted to lists, then change the values, then again change it back to tuples
myt2 = ('apple','banana','cherry')
y = list(myt2)
y[1]='kiwi'
myt2 = tuple(y)
print(myt2)

#tuples with loops
for g in myt2:
    print(g)
if "mango" in myt2:
    print('mango is present in myt2')
else:
    print('mango is not present')
#as tuples are unchangeble we cannot remove items in the tuple, but tuple can be removed completely
#del mytu
#print(mytu) #error saying it no longer exists
#join two tuples
t1 = ('a','b')
t2 = (1,2)
t3 = t1+t2
print(t3)
#tuple constructor can be used to make it as a tuple
t4 = tuple((4,5))
print(t4)
#t4[1]=3
#tuple methods count() and index()
#count gives the number of times a specific value is present in the tuple
#syntax tuple.count(value)
t5 = (2,3,4,5,6,2,3,4)
print(t5.count(2))
#The index() method finds the first occurrence of the specified value
#The index() method raises an exception if the value is not found
print(t5.index(3))
#print(t5.index(7)) error saying 7 is not in tuple