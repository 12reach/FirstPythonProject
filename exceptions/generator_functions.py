#!/usr/bin/python3

def main():
    GetARangeOfNumber()


def GetARangeOfNumber():
    for index in IteratingStepByStep(1,123, 7):
        print(index, end=' ')

def IteratingStepByStep(start, stop, step):
    number = start
    while number <= stop:
        # print(number)
        yield number
        number += step



if __name__ == "__main__":
    main()