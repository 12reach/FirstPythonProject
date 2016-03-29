#!/usr/bin/python3

# why we need a main script
# we will how it comes to our help in the later part when we write modules
# but first of all we can call any function inside it and never care where we declare that function

# let us see an example first

def name():
    print("this will output name.")

# now to execute this function properly, we need to call it after we defined it

# like:

name()

# the output is : this will output name.

# remember we can not call it before the function definition
# if we try to do that this error message will show up in your console

# Traceback (most recent call last):
#   File "/home/sanjib/PycharmProjects/FirstProject/primary/main_script.py", line 8, in <module>
#     name()
# NameError: name 'name' is not defined

# to solve this problem we can create a main() function like this:


# if we run our program it gives us a nice output like this:

# This is main function.

# now we can call our name() function inside it and the output is:

# This is main function.
# this will output name.

# let us define another function now


def main():
    print("This is main function.")
    name()
    age()


def age():
    print("this is age.")



if __name__ == "__main__":main()

# and we have an output like this:

# This is main function.
# this will output name.
# this is age.

x = 0
print(id(x))
y = 0
print(id(y))

if x is y:
    print("true")
else:
    print("false")

a = 3
print(id(a))