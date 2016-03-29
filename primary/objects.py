#!/usr/bin/python3

# how we can create different objects in python


class Egg:

    def __init__(self, kind = 'fired'):
        self.kind = kind

    def whatkind(self):
        return self.kind

def main():
    fried = Egg()
    print(fried.whatkind())
    scrambled = Egg('scrambled')
    print(scrambled.whatkind())

if __name__ == "__main__":
    main()