#!/usr/bin/python3

class MySelf:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def Eat(self):
        print(self.name, "eats", self.quantity, "bananas each day.")


def main():
    hagu = MySelf("Hagu", 2)
    mutu = MySelf("Mutu", 3)
    hagu.Eat()
    mutu.Eat()


if __name__ == "__main__":
    main()