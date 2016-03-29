#!/usr/bin/python3

def main():
    for index in ReturnValues():
        print(index, end=" ")


def ReturnValues():
    #return "Returning string."
    #return 56
    return range(10)


if __name__ == "__main__":
    main()