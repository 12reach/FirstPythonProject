#!/usr/bin/python3

def main():

    x = 3
    print(x)
    print(id(x))
    print(type(x))
    print("*********")

    x = 3 /2

    print(x)
    print(id(x))
    print(type(x))
    print("*********")

    x = round(42 / 9)

    print(x)
    print(id(x))
    print(type(x))
    print("*********")

    # we want to round it up
    x = 42 // 9

    print(x)
    print(id(x))
    print(type(x))
    print("*********")

    # how many digits we want to round to
    x = round(42 / 9, 3)

    print(x)
    print(id(x))
    print(type(x))
    print("*********")

    x = 43 % 7

    print(x)
    print(id(x))
    print(type(x))
    print("*********")

    x = int(34.78)

    print(x)
    print(id(x))
    print(type(x))
    print("*********")

    x = float(23)

    print(x)
    print(id(x))
    print(type(x))

    print("*********")


if __name__ == "__main__":
    main()