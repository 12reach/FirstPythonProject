#!/usr/bin/python3

# in python everything is object
# a varable is a reference to an object
# each object has an identity or an ID

x = 1

print(type(x))
print(id(x))

##################
# <class 'int'>
# 139113568
##################

# number, string, tuple -> immutable
# list, dictionary -> mutable

x = 1
y = 1
print(type(x))
print(id(x))
print(type(y))
print(id(y))
if x == y:
    print("True")
else:
    print("False")

if x is y:
    print("True")
else:
    print("False")
##################
# see the last two lines, both are true
# <class 'int'>
# 139113568
# <class 'int'>
# 139113568
# True
# True
##################


a = dict(x = 1, y = 1)
print(type(a))
print(id(a))
b = dict(x = 1, y = 1)
print(id(b))
if a == b:
    print("True")
else:
    print("False")

if a is b:
    print("True")
else:
    print("False")

##################
    # see the last two lines, one is true but the id is not same so it is false
# <class 'dict'>
# 3072650252
# 3072692524
# True
# False
##################

for i in range(0, 3):
    print(i, "=", id(i))


##################
# 0 = 139113552
# 1 = 139113568
# 2 = 139113584
##################