#!/usr/bin/python3

class Human:

    def __init__(self):
        pass

    # accessor

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

def main():
    ramu = Human()
    # ramu.height = 5.11 # it is called side effect and hard to track
    ramu.set_height(5.12)
    print(ramu.get_height())


if __name__ == "__main__":
    main()



