#!/usr/bin/python3

import sys, os, urllib.request, random, datetime

def PyVer():
    print("This is Python Version : {}.{}.{}".format(*sys.version_info))

def main():
    PyVer()
    # print("This is Python Version : {}.{}.{}".format(*sys.version_info))

    # os module
    # print(os.name)
    # print(os.getenv('PATH'))
    # print(os.getcwd())
    # print(os.urandom(52))

    #urllib module
    # page = urllib.request.urlopen('http://arshinagar.in/')
    # for line in page:
    #     print(str(line, encoding='utf-8'), end='')

    # random module

    # print(random.randint(1, 1000))
    #
    # x = list(range(25))
    # print(x)
    # random.shuffle(x)
    # print(x)
    # random.shuffle(x)
    # print(x)
    # random.shuffle(x)
    # print(x)

    #datetime module

    PresentTime = datetime.datetime.now()
    print(PresentTime)
    print(PresentTime.year, PresentTime.month, PresentTime.day, PresentTime.hour, PresentTime.minute,
          PresentTime.second, PresentTime.microsecond)

if __name__ == "__main__":
    main()