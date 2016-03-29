#!/usr/bin/python3

x = (1, 2, 3, 4)

print(x)
print(type(x))

for i in x:
    print(i)


a = [1, 2, 3, 4]

print(a)
print(type(a))

a.append(x)
print(a)

a.insert(0, x)
print(a)

for i in a:
    print(i)

strings = "string."

print(strings[1:3])

for WeWillIterateThroughIt in strings:
    print(WeWillIterateThroughIt)



