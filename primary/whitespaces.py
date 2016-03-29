#!/usr/bin/python3

# whitespace or indentation is extremely important in python

# the reason is : there is no {} or any thing else that can define the block or space of the code
# in a text editor this whitespace or indentation is pre-formatted and comes by default
# but what you will do if you use nano or VIM or gedit or leafpad or pyscript or anything that does not have it?
# you have to maintain a regular whitespace or indentation.

# look at this
def main():
    print("This is main function.")
    print("This is another function.")

if __name__ == "__main__":main()

# here is the output
#
# This is main function.
# This is another function.
#

# now look at this code

def main():
    print("This is main function.")

print("This is another function.")

if __name__ == "__main__":main()

# the output changes
####################
# This is another function.
# This is main function.
####################
# it happens because python interpreter reads this first: print("This is another function.")
# and then call the main() function

# but this rule breaks only when there is one line of function like this

def main():print("This is main function.")

if __name__ == "__main__":main()

# there is no whitespace but it runs properly
