#!/usr/bin/python3

tuples1 = 1, 2, 3, 4

print(type(tuples1))
print(id(tuples1))

tuples2 = (1, 2, 3, 4)

print(type(tuples2))
print(id(tuples2))

print(tuples1[0])
print(tuples2[0])

# it will give the last item
print(tuples2[-1])

print(type(tuples1[0]))
print(type(tuples2[0]))
print(id(tuples1[0]))
print(id(tuples2[0]))

# tuple is immutable we can not change any value
# 'tuple' object does not support item assignment

# tuples2[0] = 120
# print(tuples2)

# to make an integer tuple you need to add comma separator
IsItTuple = (1)
print(type(IsItTuple))
IsItTuple = (1,)
print(type(IsItTuple))

# let us see how list behaves
list1 = [1, 2, 3, 4]

print(type(list1))
print(id(list1))

# first item
print(list1[0])
# last item
print(list1[-1])

# we can change the value of a list item
list1[0] = 120
print(list1) # output: [120, 2, 3, 4]




