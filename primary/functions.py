#!/usr/bin/python3

# functions and parameters are two important part of a program
# a function do the repetitive job so that we need not write same thing more and more
# functions do many things
# we will see it later in our detailed functions series

# let us define a function that pass two parameters and those parameters can be taken from the users
# we just want to make more interesting

def main():
    print("This is main function.")

    for_loops(2, 6)
    print("--------")
    for_loops(3, 7)
    print("--------")
    for_loops(5, 9)
    print("--------")
    for_loops(0, 5)

def for_loops(a, b):
    for i in range(a, b):
        print(i)

if __name__ == "__main__":main()

# and the output looks like

# This is main function.
# 2
# 3
# 4
# 5
# --------
# 3
# 4
# 5
# 6
# --------
# 5
# 6
# 7
# 8
# --------
# 0
# 1
# 2
# 3
# 4

# now we can have default values of two parameters so that if user does not pass any value the function runs
# first we need to change the above code

def main():
    print("This is main function.")

    for_loops(2, 6)
    print("--------")
    for_loops(3, 7)
    print("--------")
    for_loops(5, 9)
    print("--------")
    for_loops()

def for_loops(a = 0, b = 10):
    for i in range(a, b):
        print(i)

if __name__ == "__main__":main()

# in the last call we did not pass any value and see what happens
#####################
# This is main function.
# 2
# 3
# 4
# 5
# --------
# 3
# 4
# 5
# 6
# --------
# 5
# 6
# 7
# 8
# --------
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

#####################

# in the last section output has been changed by the default values