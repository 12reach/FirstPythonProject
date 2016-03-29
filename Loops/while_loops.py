#!/usr/bin/python3

# simple fibonacci series
# sum of two numbers define the next set

a, b = 0, 1

while b < 30:
    print("a = ", a, "and" , "b = ", b, "," , end=' ')
    a, b = b, a + b

print("***********")

a, b = 0, 1

while b < 30:
    print("a = ", a, "and" , "b = ", b, "," , end=' ')
    a = b
    b = a + b


