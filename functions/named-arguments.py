#!/usr/bin/python3

def main():
    NamedArguments(name = 'Sanjib', address = 'Pluto', hobby = "Gardening")
    DemarcationLine()
    AnotherNamedArguments('Hi', 1235, 1,2,3, one = 1, two = 2, three = 3)


def NamedArguments(**kwargs):
    for key in kwargs:
        print(key, "=", kwargs[key])

def AnotherNamedArguments(arg1, arg2, *args, **kwargs):
    print(arg1, arg2)
    for index in enumerate(args):
        for i in index:
            print(i, "=", end=' ')

    DemarcationLine()
    for keys in kwargs:
        print(keys, "=", kwargs[keys])

def DemarcationLine():
    print("********")


if __name__ == "__main__":
    main()