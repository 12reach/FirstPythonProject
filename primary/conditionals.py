#!/usr/bin/python3

# there are two forms of conditionals in python
# conditional executions and conditional expressions or values

def conditionals_exec():

    a, b = 1, 3

    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")

conditionals_exec()

# a is less than b

# now we can write this statement in a different way

# # conditional expressions or values

def conditional_values():
    a, b = 1, 2
    statements = "less than " if a < b else " not less than."
    print(statements)

conditional_values()

# these functions can be written more conveniently and neatly with the main() functions now

def main():
    print("This is main function.")
    conditionals_exec()
    conditional_values()

def conditionals_exec():

    a, b = 1, 3

    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")

def conditional_values():
    a, b = 1, 2
    statements = "less than " if a < b else " not less than."
    print(statements)

if __name__ == "__main__":main()

# now if we run this program now, the output will be
#########################
# This is main function.
# less than
# a is less than b
#########################
# now we can change the place of conditional_values(), and conditionals_exec() and the output will change accordingly
#########################
# This is main function.
# a is less than b
# less than
#########################

choices = dict(
    one = 'first',
    two = 'second',
    three = 'third'
)

v = 'other'
print(choices.get(v, 'other')) # other

v = 'one'
print(choices.get(v, 'other')) # first

# this whole bunch is called suite of codes
# for loop is the most common loop and is used for iterating objects

files = open('file.txt')

for line in files.read():
    print(line, end='')
print("\n\t#############")

print(type(files))
print(id(files))
#########################
# <class '_io.TextIOWrapper'>
# 3073248708
#########################
files.close()
files = open('file.txt')
# for enumerating lines and to get the indexes
for index, line in enumerate(files.readline()):
    print(index, line, end='\n')

#########################
# 0 f
# 1 i
# 2 r
# 3 s
# 4 t
# 5 - blank space
# 6 l
# 7 i
# 8 n
# 9 e
# 10 - blank space
#########################

s = 'string'
for c in s:
    if c == 's':
        continue # it will continue without s and give output of the rest part
        # break # it will stop since in the first line it finds s
    print(c)
# fibonachi
a, b = 0, 1
while a < 10:
    print(a)
    a = a + b

i = 0
while i < len(s):
    print(s[i])
    i = i + 1
#########################
# s
# t
# r
# i
# n
# g
#########################

