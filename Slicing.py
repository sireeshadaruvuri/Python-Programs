list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#index 0 1 2 3 4 5 6 7 8 9
#negative index -9 -8 -7 -6 -5 -4 -3 -2 -1
#slicing includes colon with indexes
#advanced slicing uses two colons and third number is number of steps in between(same as range function)
print(list[:])
print(list[2:7])
print(list[2:9:2]) #advanced slicing
print(list[-8:-4])
print(list[2:])
print(list[:7])
print(list[-9:])
print(list[:-1])
print(list[::3])
print(list[::-1]) #result is order in reverse
print(list[::1])
print(list[::-4])
print(list[::-9])
print(list[2:7:-1]) #result is nothing
print(list[7:2:-1]) #in negative indexation we can only go to the left