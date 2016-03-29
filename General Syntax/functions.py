#!/usr/bin/python3

def main():

    loops(0)
    loops()
    loops(3)
    #print("This is main function")

def loops(a = 4):
    for i in range(a, 6):
        print(i, " ")
    print("*************")


if __name__ == "__main__":
    main()