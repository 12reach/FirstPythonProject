#!/usr/bin/python3

class Human:

    def __init__(self, kind = "Good"):
        self.kind = kind

    def whatKind(self):
        return self.kind

def main():

    GoodHuman = Human()
    print(GoodHuman.whatKind())
    BadHuman = Human("Bad")
    print(BadHuman.whatKind())



if __name__ == "__main__":
    main()