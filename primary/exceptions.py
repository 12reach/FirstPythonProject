#!/usr/bin/python3

# files = open('file.txt')
#
# for line in files:
#     print(line.strip())

# you can read lines this way

try:
    files = open('files.txt')
    # we check if the file name is wrong
except IOError as e:
    print("Error Message.", e)
    # if it is wrong give an error message
    # it works like if logic so an else follows
else:
    for line in files:
        print(line.strip())

# if the file name or path is wrong we get an error message
# Error Message. [Errno 2] No such file or directory: 'files.txt'
# otherwise it sails through nicely

# the same program can be written as if-else logic

try:
    # we check if the file name is wrong
    files = open('file.txt')
    for line in files:
        print(line.strip())
# else it gives an error message
except IOError as e:
    print("Error Message.", e)

# there are other error libraries in python also

def main():

    fileNameCheck('files.txt') # Error message [Errno 2] No such file or directory: 'files.txt'
    fileExtensionCheck('x.doc') # Error message Bad filename.

def fileNameCheck(filename):
    try:
        files = open(filename)
        for line in files:
            print(line.strip())
    except IOError as e:
        print("Error message", e)


def fileExtensionCheck(filename):
    try:
        if filename.endswith('txt'):
            files = open(filename)
        else:
            raise ValueError("Bad filename.")
            print(files.read())
    except ValueError as e:
        print("Error message :", e)

if __name__ == '__main__':
    main()


