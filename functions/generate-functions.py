#!/usr/bin/python3

def main():
    for index in RangeFunctions(15, 1025, 102):
        print(index, end=' ')
    print("*******")
    for index in AnotherRangeFunctions(5, 25, 5):
        print(index, end=' ')


def RangeFunctions(start, stop, step):

    i = start
    while i <= stop:
        yield i
        i += step

def AnotherRangeFunctions(*args):
    numberOfArguments = len(args)
    if numberOfArguments < 1: raise TypeError('At least one argument is required.')
    elif numberOfArguments == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numberOfArguments == 2:
        # start and stop will be tuple
        (start, stop) = args
        step = 1
    elif numberOfArguments == 3:
        # all start and stop and step will be tuple
        (start, stop, step) = args
    else: raise TypeError("Maximum three arguments. You gave {}".format(numberOfArguments))

    i = start
    while i <= stop:
        yield i
        i += step





if __name__ == "__main__":
    main()