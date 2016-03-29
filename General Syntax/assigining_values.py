#!/usr/bin/python3

b = 4
a = "This is a string."

x, y = 2, 5

x ,y  = y, x

tuples = (1, 2, 34, 89)

lists = [1, "Goutam Budhdha", 4, 90]

dictionaries = {'a' : 4, 'b' : "Debansu is a good boy and his friend lives in Bombay Harbour.", 'c' : 8}

def main():
    print(type(b))
    print(type(a))
    print(type(tuples))
    print(type(lists))
    print(type(dictionaries))

if __name__ == '__main__':
    main()


