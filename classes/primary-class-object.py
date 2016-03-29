#!/usr/bin/python3

class Human:

    def __init__(self, kind = "good"):
        self.kind = kind

    def WhatKind(self):
        return self.kind


def main():

    good = Human()
    bad = Human("bad")
    print(good.WhatKind())
    print(bad.WhatKind())


if __name__ == "__main__":
    main()