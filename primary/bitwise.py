#!/usr/bin/python3

# bitwise operators are available in python

def binaries(n):
    print('{:08b}'.format(n))

binaries(2)
# 00000010
# 8 bits = 1 byte, 00000010 = 2

x = binaries(1)
y = binaries(2)
z = binaries(3)

print(id(x))
print(id(y))
print(id(z))

#################
# 138716908
# 138716908
# 138716908
#################